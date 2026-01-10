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

@dataclass
class ChordModel:
    name: str
    notes_name: List[str]
    function: str
    notes: List[int]

    @staticmethod
    def create(name: str, notes: List[str], function: str) -> 'ChordModel':
        semitones = [NoteModel.MAP[n] for n in notes]
        return ChordModel(name, notes, function, semitones)

@dataclass
class DecisionLog:
    """
    Estrutura rica para armazenar a decisão harmônica e sua justificativa.
    Essencial para o conceito 'Glass Box'.
    """
    chord_name: str
    function: str
    vl_score: float
    tension_score: float
    function_score: float
    total_score: float
    justification: str

@dataclass
class MelodyModel:
    measures: List[List[str]]

    def get_measure_semitones(self, index: int) -> List[int]:
        return [NoteModel.MAP[n] for n in self.measures[index]]
