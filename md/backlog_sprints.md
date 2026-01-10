# Backlog e Sprints: MVP AdaptiveHarmonicAI

Este documento estrutura o plano de ação do MVP utilizando metodologia ágil (Scrum/Kanban). Ele serve como a fonte única da verdade para o controle de atividades, definição de pronto (DoD) e monitoramento semanal.

## 🎯 Definição de Pronto (Definition of Done - DoD)

Para qualquer tarefa ser considerada concluída, ela deve atender aos seguintes critérios:

* [ ] Código implementado e funcional.
* [ ] Testes unitários básicos passando (quando aplicável).
* [ ] Documentação técnica atualizada (se houve mudança de arquitetura).
* [ ] Validado pelo "Product Owner" (neste caso, verificado contra os requisitos do prompt).

## 🏃 Sprint 1: Core Explicável (Semana 1)

**Objetivo:** Transformar o motor de harmonização de uma "caixa preta" que retorna acordes para uma "caixa de vidro" que retorna decisões estruturadas.

### User Stories

* **US01:** Como desenvolvedor, quero que o algoritmo retorne a justificativa da escolha do acorde para que eu possa exibi-la ao usuário.
* **US02:** Como usuário, quero poder forçar uma função harmônica específica para ver como o sistema reage.

### Tasks & Checklist

#### 1.1 Refatoração do `HarmonyPredictor`

* [x] Criar classe `DecisionLog` para estruturar o retorno (acorde, função, scores, texto).
* [x] Atualizar método `predict` para calcular e armazenar os scores individuais (Voice Leading, Tensão, Função).
* [x] Implementar gerador de texto de justificativa (template string baseado nos scores).
* [x] **Review:** Verificar se o JSON de saída está completo e legível.

#### 1.2 Implementação de Restrições (Intervenção)

* [x] Adicionar parâmetro `forced_function` no método `predict`.
* [x] Implementar lógica de filtro: se `forced_function` existe, ignorar candidatos de outras funções.
* [x] Tratar casos de erro (ex: função forçada não tem acordes válidos no contexto).
* [x] **Review:** Testar forçar uma "Subdominante" onde o natural seria "Dominante".

## 🏃 Sprint 2: Interface Glass Box (Semana 2)

**Objetivo:** Criar a primeira versão visual do produto, permitindo interação real sem código.

### User Stories

* **US03:** Como usuário, quero inserir uma melodia de forma simples para testar o sistema.
* **US04:** Como usuário, quero ver a partitura e a explicação da harmonia lado a lado.

### Tasks & Checklist

#### 2.1 Setup do Frontend (Streamlit)

* [x] Inicializar projeto Streamlit.
* [x] Configurar layout básico (Sidebar para configs, Main para visualização).
* [x] Criar componente de Input de Melodia (Upload MIDI ou Texto ABC/LiliPond simples).

#### 2.2 Visualização de Decisão

* [x] Integrar biblioteca de renderização de partitura (ex: `music21` gerando imagem ou `verovio` via componente customizado).
* [x] Criar "Card de Decisão": Componente UI que mostra o Acorde, a Função (T/S/D) e a Justificativa.
* [x] **Review:** A partitura é gerada corretamente a partir do input?

## 🏃 Sprint 3: Interatividade e Ciclo Completo (Semana 3)

**Objetivo:** Fechar o ciclo de "Governança", permitindo que a ação do usuário no Frontend altere o resultado do Backend.

### User Stories

* **US05:** Como usuário, quero alterar a função de um compasso e ver a harmonia mudar imediatamente.
* **US06:** Como usuário, quero exportar o resultado final para usar na minha DAW/Editor.

### Tasks & Checklist

#### 3.1 Conexão Front-Back (Governança)

* [x] Criar estado de sessão no Streamlit para armazenar a harmonização atual.
* [x] Implementar controles de UI (SelectBox/Botões) para cada compasso permitindo troca de função.
* [x] Ligar evento de troca de função -> Recálculo do `HarmonyPredictor` -> Atualização da Tela.

#### 3.2 Exportação

* [x] Implementar botão "Exportar MusicXML".
* [ ] Implementar botão "Exportar MIDI".
* [x] **Review:** O arquivo exportado abre corretamente no MuseScore?

## 🏃 Sprint 4: Polimento e Deploy (Semana 4)

**Objetivo:** Deixar o produto pronto para ser usado por terceiros (Educadores) sem supervisão técnica.

### User Stories

* **US07:** Como usuário beta, quero acessar a ferramenta via link sem instalar nada.
* **US08:** Como usuário beta, quero exemplos prontos para não precisar criar melodia do zero.

### Tasks & Checklist

#### 4.1 Usabilidade e Dogfooding

* [x] Testar fluxo completo como se fosse um usuário leigo.
* [x] Melhorar mensagens de erro e feedbacks visuais (ex: spinners de carregamento).
* [x] Adicionar "Tooltips" explicando termos técnicos (Voice Leading, etc).

#### 4.2 Deploy e Dados

* [ ] Carregar as melodias de teste (do Prompt 15) como exemplos selecionáveis.
* [ ] Realizar deploy (Streamlit Cloud ou similar).
* [ ] **Review Final:** O link está acessível publicamente?

## 🏃 Sprint 5: Validação (Semanas 5-6)

**Objetivo:** Executar os testes de mercado e coletar dados qualitativos/quantitativos.

### Tasks & Checklist

#### 5.1 Preparação do Teste

* [ ] Recrutar 5-10 educadores (Beta Testers).
* [ ] Agendar sessões de 30 min.
* [ ] Criar formulário de feedback (Google Forms/Typeform) focado nas métricas de confiança.

#### 5.2 Execução

* [ ] Rodar demos guiadas.
* [ ] Registrar observações: "Onde eles travaram?", "O que eles elogiaram?", "Eles tentaram exportar?".
* [ ] Compilar dados brutos.

## 🏃 Sprint 6: Consolidação (Semanas 7-8)

**Objetivo:** Transformar feedback em estratégia de negócio.

### Tasks & Checklist

#### 6.1 Análise

* [ ] Categorizar feedbacks (Bugs, Features, UX, Valor).
* [ ] Calcular métricas de sucesso (NPS, Taxa de Exportação).

#### 6.2 Artefatos Finais

* [ ] Atualizar Roadmap do Produto (V2).
* [ ] Criar Pitch Deck v1.0.
* [ ] Definir identidade visual "Glass Box".
* [ ] **Review Final do Ciclo:** Estamos prontos para buscar investimento ou parceiros?
