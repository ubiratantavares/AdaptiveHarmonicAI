import math
import itertools
from typing import List
from ..model.models import ChordModel

class DistanceService:
    """
    Serviço responsável por cálculos de distância física e melódica.
    """

    @staticmethod
    def voice_leading(chord1_notes: List[int], chord2_notes: List[int]) -> int:
        """
        Calcula a distância mínima de condução de vozes (Voice Leading)
        de forma estrita (voz a voz) e modular (menor caminho na oitava).
        """
        # Se os acordes tiverem tamanhos diferentes, ajusta para a menor cardinalidade
        min_len = min(len(chord1_notes), len(chord2_notes))
        c1 = chord1_notes[:min_len]
        c2 = chord2_notes[:min_len]

        total_dist = 0
        for n1, n2 in zip(c1, c2):
            diff = abs(n1 - n2)
            # Distância modular (menor caminho no relógio de 12 notas)
            # Ex: 0 (C) -> 11 (B) = min(11, 12-11) = 1
            dist = min(diff, 12 - diff)
            total_dist += dist

        return total_dist

    @staticmethod
    def melody_distance(chord_notes: List[int], melody_notes: List[int]) -> float:
        """
        Calcula a distância média entre as notas da melodia e as notas do acorde.
        """
        if not melody_notes:
            return 0.0
        
        total_dist = 0
        for m in melody_notes:
            # Distância mínima da nota melódica para qualquer nota do acorde
            # (considerando equivalência de oitava simplificada aqui para semitons puros)
            min_d = min(abs(m - c) for c in chord_notes)
            total_dist += min_d
            
        return total_dist / len(melody_notes)

class ProbabilityService:
    """
    Converte distâncias em probabilidades usando decaimento exponencial.
    """

    def __init__(self, alpha: float = 0.4, beta: float = 0.6):
        self.alpha = alpha
        self.beta = beta

    def vl_prob(self, distance: int) -> float:
        return math.exp(-self.alpha * distance)

    def mel_prob(self, distance: float) -> float:
        return math.exp(-self.beta * distance)
