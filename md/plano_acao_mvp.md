# Plano de Ação Imediato: MVP AdaptiveHarmonicAI (Glass Box)

Este documento detalha o plano tático para os próximos 60 dias, focado exclusivamente na materialização e validação do MVP (Minimum Viable Product) conforme definido nas consultorias de Estratégia, Inovação e Prototipagem.

**Objetivo Central:** Transformar o motor matemático atual em uma interface web interativa que prove a tese de "Governança da Criatividade Musical" para educadores e produtores.

## 📅 Cronograma Geral (60 Dias)

| Fase | Duração | Foco Principal | Entregável Final |
| :--- | :--- | :--- | :--- |
| **1. Engenharia (Build)** | Semanas 1-4 | Frontend Explicável + Refatoração Core | WebApp Funcional (Streamlit) |
| **2. Validação (Measure)** | Semanas 5-6 | Testes com Educadores | Relatório de Validação de UVP |
| **3. Consolidação (Learn)** | Semana 7-8 | Ajustes e Pitch Deck | Roadmap V2 + Deck de Investimento |

## 🛠️ Fase 1: Engenharia do MVP (Semanas 1-4)

**Meta:** Criar uma experiência de uso onde o usuário possa ver a decisão harmônica, ler a justificativa e intervir no resultado.

### Semana 1: Refatoração do Core para Explicabilidade

* **[x] Tarefa 1.1:** Adaptar a classe `HarmonyPredictor` para retornar um objeto rico de decisão, não apenas o acorde.
  * *Output:* JSON contendo `{acorde, função, score_voice_leading, score_tensão, justificativa_texto}`.
* **[x] Tarefa 1.2:** Implementar lógica de "Intervenção Forçada".
  * *Funcionalidade:* Permitir que o algoritmo recalcule o melhor acorde dado uma restrição imposta pelo usuário (ex: `force_function='S'`).

### Semana 2: Desenvolvimento do Frontend (Interface Glass Box)

* **[x] Tarefa 2.1:** Configurar ambiente Streamlit (Python).
* **[x] Tarefa 2.2:** Criar componentes de UI:
  * Input de Melodia (Piano Roll simples ou Upload MIDI).
  * Visualização de Partitura (integração music21 ou biblioteca JS).
  * **Painel de Decisão (O Diferencial):** Área lateral que exibe os dados do JSON de decisão em linguagem natural.

### Semana 3: Integração e Interatividade

* **[x] Tarefa 3.1:** Conectar Frontend ao Backend.
* **[x] Tarefa 3.2:** Implementar o fluxo de "Governança":
  * Usuário clica em um compasso -> Vê a explicação -> Seleciona "Mudar para Subdominante" -> Sistema atualiza.
* **[x] Tarefa 3.3:** Exportação básica (MusicXML/MIDI) para fechar o ciclo de valor.

### Semana 4: Polimento e Deploy

* **[x] Tarefa 4.1:** Testes de usabilidade internos (dogfooding).
* **[ ] Tarefa 4.2:** Deploy em ambiente acessível (ex: Streamlit Cloud ou servidor próprio).
* **[x] Tarefa 4.3:** Preparação dos dados de demonstração (as melodias "controladas" definidas no Prompt 15).

## 🧪 Fase 2: Validação de Mercado (Semanas 5-6)

**Meta:** Confirmar se a "explicabilidade" gera confiança e se há sinal de compra.

### Semana 5: Recrutamento e Preparação

* **Tarefa 5.1:** Selecionar 5-10 "Parceiros Beta" (foco em Educadores Musicais).
* **Tarefa 5.2:** Criar o Roteiro de Teste (baseado no `prompts_prototipacao.md`).
* **Tarefa 5.3:** Preparar formulário de feedback focado em métricas de confiança (não apenas satisfação).

### Semana 6: Execução dos Testes (The Mom Test)

* **Tarefa 6.1:** Realizar sessões guiadas (remotas ou presenciais).
* **Tarefa 6.2:** Coletar métricas chave:
  * Taxa de aceitação da sugestão.
  * Frequência de uso da intervenção.
  * Tentativas de exportação (sinal de compra).

## 💼 Fase 3: Consolidação Institucional (Semanas 7-8)

**Meta:** Transformar o aprendizado técnico e de mercado em ativos de negócio.

### Semana 7: Análise e Refinamento

* **Tarefa 7.1:** Analisar feedback dos testes.
* **Tarefa 7.2:** Priorizar backlog para a V2 (o que faltou? o que sobrou?).
* **Tarefa 7.3:** Ajustar a UVP (Proposta de Valor Única) com base na linguagem real usada pelos usuários.

### Semana 8: Artefatos de Negócio

* **Tarefa 8.1:** Criar Pitch Deck (10 slides) baseado no *Project Charter*.
* **Tarefa 8.2:** Definir identidade visual básica (Logo e Paleta "Glass Box").
* **Tarefa 8.3:** Planejamento do próximo ciclo (Integração VST/DAW).
