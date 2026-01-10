import sys
import os

# Adiciona o diretório raiz ao path para permitir imports relativos/absolutos corretamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.model.models import ChordModel, MelodyModel
from src.service.math_services import ProbabilityService
from src.service.predictor import HarmonyPredictor
from src.controller.harmony_controller import HarmonyController

def main():
    # 1. Setup do Universo Harmônico (Bootstrap)
    chords_db = {
        "C": ChordModel.create("C", ["C", "E", "G"], "T"),
        "Dm": ChordModel.create("Dm", ["D", "F", "A"], "Sr"),
        "Em": ChordModel.create("Em", ["E", "G", "B"], "Ta"),
        "F": ChordModel.create("F", ["F", "A", "C"], "S"),
        "G": ChordModel.create("G", ["G", "B", "D"], "D"),
        "Am(Tr)": ChordModel.create("Am", ["A", "C", "E"], "Tr"),
        "Am(Sa)": ChordModel.create("Am", ["A", "C", "E"], "Sa"),
        "Bdim": ChordModel.create("Bdim", ["B", "D", "F"], "D*")
    }

    # 2. Input (Melodia de Teste - Prompt 15)
    # Compasso 1: C (T) -> Compasso 2: B (D?)
    melody_raw = [
        ["C"],      # Compasso 0 (Melodia sobre C)
        ["B"],      # Compasso 1 (Melodia sobre ?)
        ["A"],      # Compasso 2
        ["G"]       # Compasso 3
    ]
    melody = MelodyModel(melody_raw)

    # 3. Inicialização do Core
    prob_service = ProbabilityService()
    predictor = HarmonyPredictor(chords_db, prob_service)
    controller = HarmonyController(predictor)

    # 4. Execução 1: Modo Automático (Sem intervenção)
    print("\n--- MODO AUTOMÁTICO (Glass Box) ---")
    initial_context = chords_db["C"] # Começa assumindo C anterior
    timeline_auto = controller.harmonize(melody, initial_context)

    for i, decision in enumerate(timeline_auto):
        print(f"Compasso {i+1}: {decision.chord_name} ({decision.function})")
        print(f"   Voices: {decision.chord_notes}")
        print(f"   Justificativa: {decision.justification}")
        print(f"   Matriz de Decisão:")
        print(f"     - Gramática: {decision.grammar_score:.4f}")
        print(f"     - Presença Melódica: {decision.melody_presence_score:.4f}")
        print(f"     - Voice Leading: {decision.voice_leading_score:.4f}")
        print(f"   Score Total: {decision.total_score:.6f}")
        print("-" * 40)

    # 5. Execução 2: Modo Governança (Intervenção no Compasso 2)
    print("\n--- MODO GOVERNANÇA (Forçando Subdominante no Compasso 2) ---")
    # Forçar 'S' (Subdominante) no índice 1 (Compasso 2)
    interventions = {1: "S"} 
    timeline_gov = controller.harmonize(melody, initial_context, forced_functions=interventions)

    for i, decision in enumerate(timeline_gov):
        tag = "[INTERVENÇÃO]" if i in interventions else ""
        print(f"Compasso {i+1} {tag}: {decision.chord_name} ({decision.function})")
        print(f"   Justificativa: {decision.justification}")
        print("-" * 40)

if __name__ == "__main__":
    main()
