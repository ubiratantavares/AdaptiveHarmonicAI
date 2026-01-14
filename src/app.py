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
from src.service.music_xml_parser import MusicXMLParser
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
        "Dm": ChordModel.create("Dm", ["D", "F", "A"], "Sr"),
        "Em": ChordModel.create("Em", ["E", "G", "B"], "Ta"),
        "F": ChordModel.create("F", ["F", "A", "C"], "S"),
        "G": ChordModel.create("G", ["G", "B", "D"], "D"),
        "Am(Tr)": ChordModel.create("Am", ["A", "C", "E"], "Tr"), # Am como Tônica
        "Am(Sa)": ChordModel.create("Am", ["A", "C", "E"], "Sa"), # Am como Subdominante
        "Bdim": ChordModel.create("Bdim", ["B", "D", "F"], "D*")
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
        st.divider()
        st.info("Melodia (Input)")
        
        # Opção de Importação
        uploaded_file = st.file_uploader("Importar MusicXML (.musicxml, .xml)", type=["musicxml", "xml"])
        
        melody_input = None
        time_signature = "4/4"
        score_title = "Harmonização"
        score_composer = "AI"
        
        if uploaded_file is not None:
            try:
                # Lê o arquivo e extrai a melodia
                file_content = uploaded_file.read()
                parsed_data = MusicXMLParser.parse(file_content)
                melody_input = parsed_data["measures"]
                time_signature = parsed_data["time_signature"]
                score_title = parsed_data.get("title", "Harmonização")
                score_composer = parsed_data.get("composer", "AI")
                
                st.success(f"Arquivo importado! {len(melody_input)} compassos detectados. Compasso: {time_signature}")
            except Exception as e:
                st.error(f"Erro ao ler arquivo: {e}")
        else:
            st.info("Por favor, faça o upload de um arquivo MusicXML para começar.")
            st.stop()
        
        st.write(f"Melodia Atual ({len(melody_input)} compassos):")
        st.code(str(melody_input))

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
    
    for i, decision in enumerate(timeline):
        # Quebra linha a cada 4 compassos
        if i % 4 == 0:
            cols = st.columns(4)
            
        with cols[i % 4]:
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
                st.caption(f"🎹 Voices: {', '.join(decision.chord_notes)}")
                
                # Scores (Glass Box) - Matriz de Decisão Detalhada
                with st.expander("Matriz de Decisão"):
                    c1, c2 = st.columns(2)
                    c1.metric("Gramática", f"{decision.grammar_score:.2f}", help="Probabilidade da transição funcional (Diagrama)")
                    c2.metric("Presença Melódica", f"{decision.melody_presence_score:.2f}", help="Score baseado na presença da nota da melodia no acorde")
                    
                    c3, c4 = st.columns(2)
                    c3.metric("Voice Leading", f"{decision.voice_leading_score:.2f}", help="Suavidade do movimento das vozes (física)")
                    c4.metric("Score Total", f"{decision.total_score:.4f}")
                
                # Justificativa
                st.markdown("---")
                st.caption(f"🤖 *{decision.justification}*")
                
                # Intervenção (Governança)
                st.markdown("---")
                current_func = st.session_state.interventions.get(i, "Auto")
                new_func = st.selectbox(
                    "Forçar Função:",
                    ["Auto", "T", "Tr", "Ta", "S", "Sr", "Sa", "D", "D*"],
                    key=f"func_{i}",
                    index=["Auto", "T", "Tr", "Ta", "S", "Sr", "Sa", "D", "D*"].index(current_func)
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
            score = ScoreView.create_score(
                melody, 
                timeline, 
                time_signature=time_signature,
                title=score_title,
                composer=score_composer
            )
            
            # Gera nome do arquivo de saída
            # Ex: "minha_musica.xml" -> "minha_musica_harmonia.musicxml"
            input_name = uploaded_file.name
            base_name = input_name.rsplit('.', 1)[0]
            output_filename = f"{base_name}_harmonia.musicxml"
            
            # Salva em arquivo temporário/output
            filepath = ScoreView.save_xml(score, output_filename)
            
            # Lê o arquivo para permitir download
            with open(filepath, "rb") as f:
                file_bytes = f.read()
                
            st.download_button(
                label="⬇️ Baixar MusicXML",
                data=file_bytes,
                file_name=output_filename,
                mime="application/vnd.recordare.musicxml+xml"
            )
            st.success(f"Arquivo gerado! Clique acima para baixar.")

    with col2:
        # Debug JSON
        with st.expander("Ver JSON Bruto (Debug)"):
            st.json([d.__dict__ for d in timeline])

if __name__ == "__main__":
    main()
