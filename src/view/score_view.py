from music21 import stream, note, chord, metadata, meter
from typing import List
import os
from ..model.models import DecisionLog, MelodyModel

class ScoreView:
    """
    Responsável por converter os dados lógicos (Timeline) em partitura MusicXML
    usando a biblioteca music21.
    """

    @staticmethod
    def create_score(melody: MelodyModel, timeline: List[DecisionLog], time_signature: str = "4/4", title: str = "Harmonização", composer: str = "AI") -> stream.Score:
        """
        Gera um objeto stream.Score do music21 pronto para exportação.
        """
        score = stream.Score()
        score.insert(0, metadata.Metadata())
        score.metadata.title = title
        score.metadata.composer = composer

        # Part 1: Melodia
        part_melody = stream.Part()
        part_melody.id = "Melodia"
        part_melody.partName = "Melodia"
        
        # Define Time Signature
        ts = meter.TimeSignature(time_signature)
        part_melody.insert(0, ts)
        
        for measure_notes in melody.measures:
            m = stream.Measure()
            
            for melody_note in measure_notes:
                if melody_note.is_rest:
                    n = note.Rest()
                else:
                    n = note.Note(melody_note.name)
                    n.octave = melody_note.octave
                
                n.quarterLength = melody_note.duration
                m.append(n)
            part_melody.append(m)

        # Part 2: Harmonia
        part_harmony = stream.Part()
        part_harmony.id = "Harmonia"
        part_harmony.partName = "Harmonia (IA)"
        
        # Define Time Signature for Harmony Part too
        part_harmony.insert(0, meter.TimeSignature(time_signature))

        for decision in timeline:
            m = stream.Measure()
            
            # Se não houve decisão válida (N/A), insere pausa
            if decision.chord_name == "N/A":
                r = note.Rest()
                r.quarterLength = ts.barDuration.quarterLength
                m.append(r)
            else:
                # Cria o acorde usando as notas exatas (Voices) da decisão
                # Isso garante que a inversão escolhida (ex: 1ª Inv) seja respeitada no MusicXML
                if decision.chord_notes:
                    c = chord.Chord(decision.chord_notes)
                else:
                    # Fallback se não houver notas (compatibilidade)
                    c = chord.Chord(decision.chord_name)
                
                c.quarterLength = ts.barDuration.quarterLength # Acorde dura o compasso todo
                c.addLyric(decision.function) # Adiciona a função como letra/texto
                
                # Adiciona o nome do acorde como anotação (opcional, mas útil)
                c.addLyric(decision.chord_name)
                
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
