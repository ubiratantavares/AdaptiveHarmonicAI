import streamlit as st
import sys
import os
import tempfile
from music21 import stream, note, chord, metadata, environment

# Adiciona o diretório raiz ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.model.models import ChordModel, MelodyModel
from src.service.math_services import ProbabilityService
from src.service.predictor import HarmonyPredictor
from src.controller.harmony_controller import HarmonyController

# Configuração da Página
st.set_page_config(
    page_title="AdaptiveHarmonicAI - Glass Box",
    page_icon="🎹",
    layout="wide"
)

# Configuração do Music21 para usar o MuseScore (se disponível) ou apenas gerar XML
# Em ambiente cloud/headless, a renderização visual direta é complexa.
# Vamos focar em gerar o MusicXML e exibir os dados textuais primeiro.
# Para visualização web real, idealmente usaríamos uma lib JS como VexFlow ou OSMD.
# Para este MVP Streamlit, vamos usar uma abordagem simplificada de "Card de Decisão".

def get_bootstrap_data():
    """Inicializa o banco de dados de acordes (Mock)"""
    return {
        "C": ChordModel.create("C", ["C", "E", "G"], "T"),
        "Dm": ChordModel.create("Dm", ["D", "F", "A"], "S"),
        "Em": ChordModel.create("Em", ["E", "G", "B"], "T"),
        "F": ChordModel.create("F", ["F", "A", "C"], "S"),
        "G": ChordModel.create("G", ["G", "B", "D"], "D"),
        "Am": ChordModel.create("Am", ["A", "C", "E"], "T"),
        "Bdim": ChordModel.create("Bdim", ["B", "D", "F"], "D")
    }

def main():
    st.title("🎹 AdaptiveHarmonicAI: Glass Box MVP")
    st.markdown("""
    **Governança da Criatividade Musical:** Este protótipo demonstra como a IA toma decisões harmônicas explicáveis.
    """)

    # --- SIDEBAR: CONFIGURAÇÃO ---
    with st.sidebar:
        st.header("🎛️ Configurações")
        alpha = st.slider("Peso Voice Leading (Física)", 0.0, 1.0, 0.4, help="Quanto maior, mais a IA prefere movimentos suaves.")
        beta = st.slider("Peso Melódico (Tensão)", 0.0, 1.0, 0.6, help="Quanto maior, mais a IA prefere notas da melodia no acorde.")
        
        st.divider()
        st.info("Melodia de Teste (C Major)")
        # Input simplificado de melodia (Lista de notas por compasso)
        # Futuro: Input MIDI real
        melody_input = [
            ["C"], ["B"], ["A"], ["G"]
        ]
        st.write(melody_input)

    # --- CORE LOGIC ---
    chords_db = get_bootstrap_data()
    prob_service = ProbabilityService(alpha=alpha, beta=beta)
    predictor = HarmonyPredictor(chords_db, prob_service)
    controller = HarmonyController(predictor)
    melody = MelodyModel(melody_input)
    initial_context = chords_db["C"]

    # --- INTERFACE DE GOVERNANÇA ---
    
    # Estado da Sessão para Intervenções
    if 'interventions' not in st.session_state:
        st.session_state.interventions = {}

    # Executa Harmonização
    timeline = controller.harmonize(melody, initial_context, forced_functions=st.session_state.interventions)

    # --- VISUALIZAÇÃO (TIMELINE) ---
    st.subheader("🎼 Timeline de Decisão Harmônica")
    
    cols = st.columns(len(timeline))
    
    for i, decision in enumerate(timeline):
        with cols[i]:
            # Cabeçalho do Compasso
            st.markdown(f"**Compasso {i+1}**")
            st.caption(f"Melodia: {melody_input[i]}")
            
            # Card de Decisão
            is_forced = i in st.session_state.interventions
            card_style = "border: 2px solid #4CAF50;" if is_forced else "border: 1px solid #ddd;"
            
            with st.container(border=True):
                # Acorde Principal
                st.markdown(f"### {decision.chord_name}")
                st.markdown(f"**Função:** `{decision.function}`")
                
                # Scores (Glass Box)
                col_a, col_b = st.columns(2)
                col_a.metric("Voice Leading", f"{decision.vl_score:.2f}")
                col_b.metric("Funcional", f"{decision.function_score:.2f}")
                
                # Justificativa
                st.markdown("---")
                st.caption(f"🤖 *{decision.justification}*")
                
                # Intervenção (Governança)
                st.markdown("---")
                current_func = st.session_state.interventions.get(i, "Auto")
                new_func = st.selectbox(
                    "Forçar Função:",
                    ["Auto", "T", "S", "D"],
                    key=f"func_{i}",
                    index=["Auto", "T", "S", "D"].index(current_func)
                )
                
                # Atualiza intervenção se mudou
                if new_func != current_func:
                    if new_func == "Auto":
                        if i in st.session_state.interventions:
                            del st.session_state.interventions[i]
                    else:
                        st.session_state.interventions[i] = new_func
                    st.rerun()

    # --- EXPORTAÇÃO ---
    st.divider()
    st.subheader("📤 Exportar Resultado")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Gerar Partitura (MusicXML)"):
            from src.view.score_view import ScoreView
            
            # Gera o objeto Score
            score = ScoreView.create_score(melody, timeline)
            
            # Salva em arquivo temporário/output
            filepath = ScoreView.save_xml(score, "harmonizacao_glassbox.musicxml")
            
            # Lê o arquivo para permitir download
            with open(filepath, "rb") as f:
                file_bytes = f.read()
                
            st.download_button(
                label="⬇️ Baixar MusicXML",
                data=file_bytes,
                file_name="harmonizacao_glassbox.musicxml",
                mime="application/vnd.recordare.musicxml+xml"
            )
            st.success(f"Arquivo gerado! Clique acima para baixar.")

    with col2:
        # Debug JSON
        with st.expander("Ver JSON Bruto (Debug)"):
            st.json([d.__dict__ for d in timeline])

if __name__ == "__main__":
    main()
