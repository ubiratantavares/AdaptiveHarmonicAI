# AdaptiveHarmonicAI

Um sistema de inteligência musical adaptativa para harmonização automática de melodias, baseado em harmonia funcional, modelos probabilísticos e física do movimento das vozes.

## 🌟 Funcionalidades Principais (MVP)

### 1. Glass Box Decision Engine 🧠

Diferente de IAs "caixa preta", o AdaptiveHarmonicAI explica cada decisão harmônica. O motor de decisão avalia 4 pilares críticos para cada acorde:

* **Gramática Funcional:** Respeita as regras de tensão e resolução (Tônica -> Subdominante -> Dominante).
* **Contexto Probabilístico:** Analisa a frequência de acordes dentro de cada função.
* **Presença Melódica:** Garante que o acorde suporte a nota da melodia.
* **Voice Leading (Física):** Calcula o esforço físico para mover as vozes do acorde anterior, usando aritmética modular (caminho mais curto).

### 2. Estratégia de Voicing Melódico 🎹

O sistema não escolhe apenas o acorde (ex: "Dó Maior"), mas a **inversão exata** que coloca a nota da melodia no topo (Soprano).

* *Exemplo:* Se a melodia é **Dó**, o sistema escolhe **C (1ª Inversão)** (E-G-C) em vez de C Fundamental, garantindo suporte melódico perfeito.

### 3. Governança e Intervenção 🎛️

O usuário tem controle total. É possível "forçar" uma função harmônica (T, S, D, Tr, etc.) em qualquer compasso. O sistema recalcula todo o caminho harmônico para acomodar a decisão do usuário sem quebrar as regras de condução de vozes.

### 4. Exportação Profissional 🎼

Gera arquivos **MusicXML** prontos para softwares de notação (MuseScore, Finale, Sibelius), preservando exatamente os voicings e inversões escolhidos pela IA.

## 🚀 Como Executar

1. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

2. **Execute a Interface Web (Streamlit):**

    ```bash
    streamlit run src/app.py
    ```

3. **Teste no Terminal:**

    ```bash
    python src/main_terminal.py
    ```

## 📂 Estrutura do Projeto

* `src/model`: Modelos de dados (Nota, Acorde, Gramática).
* `src/service`: Lógica de predição, cálculo de distâncias e probabilidades.
* `src/controller`: Orquestração do fluxo de harmonização.
* `src/view`: Interface gráfica e geração de partituras.
