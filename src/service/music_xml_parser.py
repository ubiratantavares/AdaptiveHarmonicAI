from music21 import converter, note, chord, stream
from typing import List, Union
from ..model.models import MelodyNote
import tempfile
import os

class MusicXMLParser:
    """
    Serviço responsável por ler arquivos MusicXML e extrair a melodia.
    """

    @staticmethod
    def parse(file_content: bytes) -> dict:
        """
        Lê o conteúdo binário de um arquivo MusicXML e retorna uma lista de compassos,
        onde cada compasso é uma lista de nomes de notas (ex: ["C", "D#"]).
        """
        # Music21 precisa de um arquivo físico ou string XML. 
        # Como recebemos bytes do Streamlit, vamos salvar num tempfile.
        with tempfile.NamedTemporaryFile(delete=False, suffix=".musicxml") as tmp:
            tmp.write(file_content)
            tmp_path = tmp.name

        try:
            # Carrega o score usando music21
            score = converter.parse(tmp_path)
            
            # Assume que a melodia está na primeira parte (Part 0)
            # Se houver múltiplas partes, pegamos a primeira (comportamento padrão MVP)
            parts = score.parts
            if not parts:
                # Se não tiver partes definidas, tenta pegar do stream plano
                melody_stream = score.flat
            else:
                melody_stream = parts[0]

            # Extrai compassos
            # O music21 organiza em Measures. Vamos iterar sobre eles.
            measures_data = []
            
            # makeMeasures() garante que temos a estrutura de compassos se for um stream plano
            if not melody_stream.hasMeasures():
                melody_stream = melody_stream.makeMeasures()

            # Tenta extrair a assinatura de tempo (TimeSignature)
            # Pega o primeiro TimeSignature encontrado
            ts = melody_stream.getTimeSignatures()[0] if melody_stream.getTimeSignatures() else None
            time_signature_str = ts.ratioString if ts else "4/4"

            for m in melody_stream.getElementsByClass('Measure'):
                notes_in_measure = []
                
                # Itera sobre as notas/acordes dentro do compasso
                for element in m.notesAndRests:
                    if isinstance(element, note.Note):
                        # Nota simples
                        notes_in_measure.append(MelodyNote(
                            name=element.name,
                            octave=element.octave,
                            duration=element.quarterLength,
                            is_rest=False
                        ))
                    elif isinstance(element, chord.Chord):
                        # Acorde: pega a nota mais aguda
                        top_note = max(element.notes, key=lambda n: n.pitch.ps)
                        notes_in_measure.append(MelodyNote(
                            name=top_note.name,
                            octave=top_note.octave,
                            duration=element.quarterLength,
                            is_rest=False
                        ))
                    elif isinstance(element, note.Rest):
                        notes_in_measure.append(MelodyNote(
                            name="R",
                            octave=0,
                            duration=element.quarterLength,
                            is_rest=True
                        ))
                
                measures_data.append(notes_in_measure)

            # Extrai Metadados
            title = "Harmonização Algorítmica"
            composer = "AdaptiveHarmonicAI"
            
            if score.metadata:
                if score.metadata.title:
                    title = score.metadata.title
                if score.metadata.composer:
                    composer = score.metadata.composer

            return {
                "measures": measures_data,
                "time_signature": time_signature_str,
                "title": title,
                "composer": composer
            }

        finally:
            # Limpa o arquivo temporário
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
