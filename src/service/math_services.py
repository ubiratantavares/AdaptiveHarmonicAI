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
        considerando todas as permutações possíveis das notas do segundo acorde.
        """
        # Se os acordes tiverem tamanhos diferentes, ajusta para a menor cardinalidade para evitar erro
        # (Numa implementação real, trataríamos voicings abertos/fechados)
        min_len = min(len(chord1_notes), len(chord2_notes))
        c1 = chord1_notes[:min_len]
        c2 = chord2_notes[:min_len]

        return min(
            sum(abs(a - b) for a, b in zip(c1, p))
            for p in itertools.permutations(c2)
        )

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
