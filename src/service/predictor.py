from typing import Dict, List, Optional
from ..model.models import ChordModel, DecisionLog
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

    def predict(self, prev_chord: ChordModel, melody_semitones: List[int], forced_function: Optional[str] = None) -> DecisionLog:
        """
        Prevê o próximo acorde dado o anterior e a melodia.
        Suporta 'forced_function' para intervenção do usuário (Governança).
        """
        best_decision = None
        best_score = -1.0

        # Itera sobre todos os acordes candidatos
        for chord in self.chords.values():
            
            # 1. Filtro de Governança (Intervenção do Usuário)
            if forced_function and chord.function != forced_function:
                continue

            # 2. Cálculo das Probabilidades Parciais
            
            # P(Função | Função Anterior)
            p_func_trans = FunctionalGrammar.prob(chord.function, prev_chord.function)
            
            # P(Acorde | Função)
            p_chord_func = FunctionalDistribution.prob(chord.name, chord.function)

            # Se a transição é proibida pela gramática, descarta (score 0)
            if p_func_trans == 0 or p_chord_func == 0:
                continue

            # Distância de Voice Leading
            dvl = DistanceService.voice_leading(prev_chord.notes, chord.notes)
            p_vl = self.ps.vl_prob(dvl)

            # Distância Melódica
            dm = DistanceService.melody_distance(chord.notes, melody_semitones)
            p_mel = self.ps.mel_prob(dm)

            # 3. Score Total (Produto das probabilidades - Naive Bayes Híbrido)
            total_score = p_func_trans * p_chord_func * p_vl * p_mel

            # 4. Seleção do Melhor Candidato
            if total_score > best_score:
                best_score = total_score
                
                # Gera a justificativa textual (Explainability)
                justification = self._generate_justification(
                    prev_chord, chord, p_func_trans, dvl, dm
                )

                best_decision = DecisionLog(
                    chord_name=chord.name,
                    function=chord.function,
                    vl_score=round(p_vl, 4),
                    tension_score=round(p_mel, 4), # Usando dist melódica como proxy de tensão/dissonância
                    function_score=round(p_func_trans, 4),
                    total_score=round(total_score, 6),
                    justification=justification
                )

        # Fallback caso nenhum acorde satisfaça (ex: restrição impossível)
        if best_decision is None:
            return DecisionLog("N/A", "N/A", 0, 0, 0, 0, "Nenhuma opção válida encontrada para os critérios.")

        return best_decision

    def _generate_justification(self, prev: ChordModel, curr: ChordModel, p_func: float, dvl: int, dm: float) -> str:
        """
        Gera uma explicação em linguagem natural para a decisão.
        """
        reasons = []
        
        # Explicação Funcional
        if prev.function == curr.function:
            reasons.append(f"Mantém a função {curr.function} (estabilidade).")
        else:
            reasons.append(f"Transição funcional de {prev.function} para {curr.function}.")

        # Explicação Física (Voice Leading)
        if dvl == 0:
            reasons.append("Movimento de vozes nulo (estático).")
        elif dvl <= 2:
            reasons.append(f"Condução de vozes muito suave ({dvl} semitons).")
        else:
            reasons.append(f"Salto harmônico significativo ({dvl} semitons).")

        # Explicação Melódica
        if dm < 1.0:
            reasons.append("Alta consonância com a melodia.")
        
        return " ".join(reasons)
