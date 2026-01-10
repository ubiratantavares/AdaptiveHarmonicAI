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
    def get_macro_function(func: str) -> str:
        """
        Mapeia sub-funções (Tr, Ta, Sr, Sa, D*) para as funções fundamentais (T, S, D).
        """
        if func in ["T", "Tr", "Ta"]: return "T"
        if func in ["S", "Sr", "Sa"]: return "S"
        if func in ["D", "D*"]: return "D"
        return "T" # Fallback seguro

    @staticmethod
    def prob(next_func: str, prev_func: str) -> float:
        # Normaliza para macro-funções antes de consultar a matriz de Markov
        prev_macro = FunctionalGrammar.get_macro_function(prev_func)
        next_macro = FunctionalGrammar.get_macro_function(next_func)
        return FunctionalGrammar.TRANSITION.get(prev_macro, {}).get(next_macro, 0.0)

class FunctionalDistribution:
    """
    Define a probabilidade de um acorde específico dado sua função.
    Agora suporta a nomenclatura detalhada (Tr, Ta, etc).
    """
    MAP = {
        "T": {"C": 0.6, "Am": 0.2, "Em": 0.2}, # Am(Tr), Em(Ta)
        "S": {"F": 0.6, "Dm": 0.2, "Am": 0.2}, # Dm(Sr), Am(Sa)
        "D": {"G": 0.7, "Bdim": 0.3}           # Bdim(D*)
    }

    @staticmethod
    def prob(chord_name: str, function: str) -> float:
        # A distribuição é baseada na MACRO função.
        # Ex: Se o acorde é Am com função 'Tr', qual a prob de 'Am' dado que estamos no estado 'T'?
        macro_func = FunctionalGrammar.get_macro_function(function)
        
        # Remove sufixos de visualização se houver (ex: "Am(Tr)" -> "Am")
        clean_name = chord_name.split("(")[0]
        
        return FunctionalDistribution.MAP.get(macro_func, {}).get(clean_name, 0.0)
