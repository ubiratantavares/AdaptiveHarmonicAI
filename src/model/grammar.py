from typing import Dict

class FunctionalGrammar:
    """
    Define as regras de transição entre funções harmônicas (Markov).
    """
    TRANSITION = {
        "T": {"T": 0.10, "S": 0.45, "D": 0.45},
        "S": {"T": 0.30, "S": 0.00, "D": 0.70},
        "D": {"T": 0.95, "S": 0.00, "D": 0.05}
    }

    @staticmethod
    def prob(next_func: str, prev_func: str) -> float:
        return FunctionalGrammar.TRANSITION.get(prev_func, {}).get(next_func, 0.0)

class FunctionalDistribution:
    """
    Define a probabilidade de um acorde específico dado sua função.
    """
    MAP = {
        "T": {"C": 0.5, "Am": 0.3, "Em": 0.2},
        "S": {"F": 0.5, "Dm": 0.3, "Am": 0.2},
        "D": {"G": 0.7, "Bdim": 0.3}
    }

    @staticmethod
    def prob(chord_name: str, function: str) -> float:
        return FunctionalDistribution.MAP.get(function, {}).get(chord_name, 0.0)
