from dataclasses import dataclass
from typing import List, Optional

@dataclass
class NoteModel:
    name: str
    semitone: int

    MAP = {
        "C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3,
        "E": 4, "F": 5, "F#": 6, "Gb": 6, "G": 7, "G#": 8,
        "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11
    }

    @staticmethod
    def from_name(name: str) -> 'NoteModel':
        return NoteModel(name, NoteModel.MAP[name])

    @staticmethod
    def from_semitone(semitone: int) -> str:
        # Mapa reverso simplificado (prefere sustenidos por padrão)
        REVERSE_MAP = {
            0: "C", 1: "C#", 2: "D", 3: "D#", 4: "E", 5: "F",
            6: "F#", 7: "G", 8: "G#", 9: "A", 10: "A#", 11: "B"
        }
        return REVERSE_MAP.get(semitone % 12, "?")

@dataclass
class ChordModel:
    name: str
    notes_name: List[str]
    function: str
    notes: List[int]
    inversion: int = 0 # 0=Root, 1=1st, 2=2nd

    @staticmethod
    def create(name: str, notes: List[str], function: str) -> 'ChordModel':
        semitones = [NoteModel.MAP[n] for n in notes]
        return ChordModel(name, notes, function, semitones)

    def generate_inversions(self) -> List['ChordModel']:
        """
        Gera as 3 inversões da tríade.
        Retorna uma lista de novos ChordModels com as notas permutadas.
        """
        inversions = []
        
        # Fundamental (Root): [0, 1, 2] -> Topo é o índice 2
        inversions.append(self) 
        
        # 1ª Inversão: [1, 2, 0] (Terça no baixo, Fundamental no topo) -> Topo é índice 0 (na nova lista)
        # Ex: C-E-G -> E-G-C
        inv1_notes = self.notes_name[1:] + self.notes_name[:1]
        inv1_semitones = self.notes[1:] + self.notes[:1]
        inversions.append(ChordModel(f"{self.name} (1ª Inv)", inv1_notes, self.function, inv1_semitones, 1))
        
        # 2ª Inversão: [2, 0, 1] (Quinta no baixo, Terça no topo) -> Topo é índice 1
        # Ex: C-E-G -> G-C-E
        inv2_notes = self.notes_name[2:] + self.notes_name[:2]
        inv2_semitones = self.notes[2:] + self.notes[:2]
        inversions.append(ChordModel(f"{self.name} (2ª Inv)", inv2_notes, self.function, inv2_semitones, 2))
        
        return inversions

@dataclass
class DecisionLog:
    """
    Estrutura rica para armazenar a decisão harmônica e sua justificativa.
    Essencial para o conceito 'Glass Box'.
    """
    chord_name: str
    chord_key: str # Chave única no dicionário (ex: "Am(Tr)") para lookup correto
    function: str
    chord_notes: List[str] # Voices do acorde (ex: ["C", "E", "G"])
    vl_score: float
    tension_score: float
    function_score: float
    total_score: float
    justification: str
    # Detailed Factors (Critical Thinking)
    grammar_score: float = 0.0
    melody_presence_score: float = 0.0
    voice_leading_score: float = 0.0

@dataclass
class MelodyModel:
    measures: List[List[str]]

    def get_measure_semitones(self, index: int) -> List[int]:
        return [NoteModel.MAP[n] for n in self.measures[index]]
