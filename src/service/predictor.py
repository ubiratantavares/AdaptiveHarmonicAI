from typing import Dict, List, Optional
from ..model.models import ChordModel, DecisionLog, NoteModel
from ..model.grammar import FunctionalGrammar, FunctionalDistribution
from ..service.math_services import DistanceService, ProbabilityService

class HarmonyPredictor:
    """
    Motor central de decisão harmônica (Glass Box).
    Responsável por escolher o melhor acorde e justificar a escolha.
    """

    def __init__(self, chords: Dict[str, ChordModel], prob_service: ProbabilityService):
        self.chords = chords
        self.ps = prob_service

    def predict(self, prev_chord: ChordModel, melody_semitones: List[int], forced_function: Optional[str] = None, ignore_vl: bool = False) -> DecisionLog:
        """
        Prevê o próximo acorde seguindo o processo de pensamento crítico de 4 etapas:
        1. Análise do Diagrama (Gramática)
        2. Função/Contexto
        3. Análise da Nota do Próximo Compasso (Presença Melódica)
        4. Minimização do Esforço (Voice Leading)
        """
        best_decision = None
        best_score = -1.0
        # Itera sobre todos os acordes candidatos
        for key, base_chord in self.chords.items():
            
            # 0. Filtro de Governança
            if forced_function and base_chord.function != forced_function:
                continue

            # Gera inversões para avaliar qual voicing encaixa melhor na melodia
            candidates = base_chord.generate_inversions()

            for chord in candidates:
                # 1. Análise do Diagrama (Gramática) - Baseado na função do acorde base
                p_grammar = FunctionalGrammar.prob(chord.function, prev_chord.function)
                
                # Usa o nome base para probabilidade de distribuição (remove sufixos de inversão)
                base_name = chord.name.split(" (")[0]
                p_context = FunctionalDistribution.prob(base_name, chord.function)

                if p_grammar == 0 or p_context == 0:
                    continue

                # 2. Voice Leading (Minimização do Esforço)
                if ignore_vl:
                    dvl = 0
                    p_vl = 1.0
                else:
                    dvl = DistanceService.voice_leading(prev_chord.notes, chord.notes)
                    p_vl = self.ps.vl_prob(dvl)

                # 3. Análise da Nota do Próximo Compasso (Presença Melódica + Voicing)
                # Verifica explicitamente se as notas da melodia estão no acorde
                melody_notes_in_chord = [n for n in melody_semitones if n in chord.notes]
                presence_ratio = len(melody_notes_in_chord) / max(len(melody_semitones), 1)
                
                # CRÍTICO: Verifica se a NOTA MAIS AGUDA (última da lista de voices) é a nota da melodia
                # Isso implementa a estratégia de "Melodia no Soprano"
                top_voice = chord.notes[-1]
                is_melody_on_top = 1.0 if (melody_semitones and top_voice in melody_semitones) else 0.0
                
                # Distância melódica geral
                dm = DistanceService.melody_distance(chord.notes, melody_semitones)
                p_mel_dist = self.ps.mel_prob(dm)
                
                # Score Melódico Refinado:
                # Prioridade ABSOLUTA para Melodia no Topo (0.8)
                # Isso força o sistema a escolher a inversão correta mesmo com custo de VL
                p_melody = (presence_ratio * 0.2) + (is_melody_on_top * 0.8) + (p_mel_dist * 0.1)

                # Penalidade severa se a nota existe no acorde mas não está no topo
                if presence_ratio > 0 and is_melody_on_top == 0:
                    p_melody *= 0.3

                # 4. Score Total
                total_score = p_grammar * p_context * p_vl * p_melody

                if total_score > best_score:
                    best_score = total_score
                    
                    justification = self._generate_justification(
                        prev_chord, chord, p_grammar, dvl, melody_semitones, melody_notes_in_chord, is_melody_on_top
                    )

                    best_decision = DecisionLog(
                        chord_name=chord.name,
                        chord_key=key, # Mantém a chave original para lookup de contexto
                        function=chord.function,
                        chord_notes=chord.notes_name,
                        vl_score=round(p_vl, 4),
                        tension_score=round(p_melody, 4),
                        function_score=round(p_grammar, 4),
                        total_score=round(total_score, 6),
                        justification=justification,
                        # Detailed Factors
                        grammar_score=round(p_grammar, 4),
                        melody_presence_score=round(p_melody, 4),
                        voice_leading_score=round(p_vl, 4)
                    )

        if best_decision is None:
            return DecisionLog("N/A", "N/A", "N/A", [], 0, 0, 0, 0, "Nenhuma opção válida encontrada.", 0, 0, 0)

        return best_decision

    def _generate_justification(self, prev: ChordModel, curr: ChordModel, p_grammar: float, dvl: int, melody_notes: List[int], notes_in_chord: List[int], is_melody_on_top: float = 0.0) -> str:
        """
        Gera uma explicação narrativa focada nos 4 fatores críticos.
        """
        reasons = []
        
        # 1. Gramática
        if prev.function == curr.function:
            reasons.append(f"Mantém função {curr.function}.")
        else:
            reasons.append(f"Move de {prev.function} para {curr.function}.")

        # 2. Melodia (Crítico: Mencionar a nota)
        if notes_in_chord:
            if is_melody_on_top > 0:
                reasons.append(f"Melodia ({NoteModel.from_semitone(melody_notes[0])}) está no topo do voicing.")
            else:
                reasons.append(f"Nota(s) da melodia presente(s) no acorde.")
        else:
            reasons.append("Melodia gera tensão (não pertence ao acorde).")

        # 3. Voice Leading
        reasons.append(f"Movimento de {dvl} semitons.")
        
        return " ".join(reasons)
