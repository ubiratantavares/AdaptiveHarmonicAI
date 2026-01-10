from music21 import stream, note, chord, metadata
from typing import List
import os
from ..model.models import DecisionLog, MelodyModel

class ScoreView:
    """
    Responsável por converter os dados lógicos (Timeline) em partitura MusicXML
    usando a biblioteca music21.
    """

    @staticmethod
    def create_score(melody: MelodyModel, timeline: List[DecisionLog]) -> stream.Score:
        """
        Gera um objeto stream.Score do music21 pronto para exportação.
        """
        score = stream.Score()
        score.insert(0, metadata.Metadata())
        score.metadata.title = "Harmonização Algorítmica (Glass Box)"
        score.metadata.composer = "AdaptiveHarmonicAI"

        # Part 1: Melodia
        part_melody = stream.Part()
        part_melody.id = "Melodia"
        part_melody.partName = "Melodia"
        
        for measure_notes in melody.measures:
            m = stream.Measure()
            # Assume 4/4 e notas iguais para simplificar MVP (cada nota = 1 semínima se forem 4 notas)
            # Se a lista de notas for menor, ajusta a duração.
            # Ex: 1 nota = Semibreve (4.0), 2 notas = Mínimas (2.0), 4 notas = Semínimas (1.0)
            duration = 4.0 / max(len(measure_notes), 1)
            
            for n_name in measure_notes:
                n = note.Note(n_name)
                n.quarterLength = duration
                m.append(n)
            part_melody.append(m)

        # Part 2: Harmonia
        part_harmony = stream.Part()
        part_harmony.id = "Harmonia"
        part_harmony.partName = "Harmonia (IA)"

        for decision in timeline:
            m = stream.Measure()
            
            # Se não houve decisão válida (N/A), insere pausa
            if decision.chord_name == "N/A":
                r = note.Rest()
                r.quarterLength = 4.0
                m.append(r)
            else:
                # Cria o acorde
                # Precisamos das notas do acorde. O DecisionLog tem o nome.
                # No MVP, vamos recriar o acorde pelo nome simples ou passar as notas no DecisionLog.
                # Para simplificar sem refatorar tudo, vamos usar o music21 para inferir as notas pelo nome
                # OU (melhor) o DecisionLog deveria ter as notas.
                # Como o music21 é esperto, chord.Chord("C") funciona.
                
                c = chord.Chord(decision.chord_name)
                c.quarterLength = 4.0 # Acorde dura o compasso todo
                c.addLyric(decision.function) # Adiciona a função como letra/texto
                m.append(c)
            
            part_harmony.append(m)

        score.append(part_melody)
        score.append(part_harmony)
        
        return score

    @staticmethod
    def save_xml(score: stream.Score, filename: str = "harmonizacao.musicxml") -> str:
        """
        Salva o score em arquivo e retorna o caminho absoluto.
        """
        # Garante que o diretório de output existe
        output_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(output_dir, exist_ok=True)
        
        filepath = os.path.join(output_dir, filename)
        score.write("musicxml", fp=filepath)
        return filepath
