from typing import List, Dict, Optional
from ..model.models import MelodyModel, ChordModel, DecisionLog
from ..service.predictor import HarmonyPredictor

class HarmonyController:
    """
    Controlador principal que orquestra o fluxo entre a Melodia (Input),
    o Preditor (Core) e a View (Output).
    """

    def __init__(self, predictor: HarmonyPredictor):
        self.predictor = predictor

    def harmonize(self, melody: MelodyModel, initial_chord: ChordModel, forced_functions: Optional[Dict[int, str]] = None) -> List[DecisionLog]:
        """
        Executa a harmonização completa da melodia.
        
        Args:
            melody: O objeto melodia.
            initial_chord: O acorde do compasso anterior ao início (contexto).
            forced_functions: Dicionário {indice_compasso: 'Função'} para intervenções manuais.
        """
        if forced_functions is None:
            forced_functions = {}

        timeline = []
        prev_chord = initial_chord

        # O primeiro item da timeline pode ser o contexto inicial ou a harmonização do primeiro compasso.
        # Aqui, vamos harmonizar compasso a compasso.
        
        for i in range(len(melody.measures)):
            measure_semitones = melody.get_measure_semitones(i)
            
            # Verifica se há intervenção do usuário para este compasso
            forced = forced_functions.get(i)

            # Regra Fundamental: O primeiro compasso (i=0) deve ser Tônica (T) por definição tonal,
            # a menos que o usuário force outra coisa explicitamente.
            if i == 0 and forced is None:
                forced = "T"

            # Pede ao oráculo (Predictor) a melhor decisão
            decision = self.predictor.predict(prev_chord, measure_semitones, forced_function=forced)
            
            timeline.append(decision)

            # Atualiza o acorde anterior para a próxima iteração
            # Usamos a chord_key para recuperar o objeto exato do dicionário (ex: "Am(Tr)")
            prev_chord = self.predictor.chords.get(decision.chord_key, prev_chord)

        return timeline
