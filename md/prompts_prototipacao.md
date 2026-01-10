# Prompts para Consultoria de Prototipagem Rápida: AdaptiveHarmonicAI

Este documento contém uma série de prompts estruturados para orientar um **Prototype Prompt Designer** na criação de um roteiro de demonstração de valor (PoC/MVP) para o **AdaptiveHarmonicAI**.

O objetivo é tangibilizar a visão estratégica de "Governança da Criatividade Musical" (definida em `prompts_inovacao.md`) em um protótipo funcional que possa ser testado rapidamente.

## Contexto para o Consultor (Input Inicial)

> **Instrução:** Utilize o contexto abaixo, extraído da estratégia de inovação, como base.
>
> **O Produto:** AdaptiveHarmonicAI (Glass Box).
> **A Proposta de Valor Única (UVP):** Entrega de decisões harmônicas auditáveis, coerentes e explicáveis em tempo real. Diferencia-se pela "Governança" e não apenas pela "Geração".
> **A Estratégia:** Hybrid-by-Design (o humano ou IA gera, o Glass Box decide e explica).
> **O Desafio:** Demonstrar que a "explicabilidade" e o "controle" são mais valiosos que a simples geração de áudio aleatória.

## Prompt 1: Definição do Escopo de Valor (UVP e Usuário)

"Atue como um Especialista em Prototipagem Rápida e Lean UX. Com base na UVP de 'Decisão Musical Auditável', defina o escopo do protótipo mais simples possível (MVP de Mágico de Oz ou Interface Funcional) que prove esse valor.

1. **A Proposta de Valor em Ação:** Como podemos demonstrar o contraste entre uma 'Caixa Preta' (Suno/Udio) e a nossa 'Caixa de Vidro' em menos de 3 minutos? Qual é o 'Aha! Moment' específico que precisamos provocar?
2. **O Usuário Ideal para o Teste:** Entre Produtores Profissionais e Educadores Musicais, qual perfil sentirá a dor da 'falta de controle' de forma mais aguda e imediata para um teste inicial? Justifique a escolha baseada na facilidade de acesso e clareza do feedback."

## Resposta 1: Definição do Escopo de Valor (UVP e Usuário)

Perfeito. Abaixo está a **resposta direta ao Prompt 1 – Definição do Escopo de Valor (UVP e Usuário)**, conforme descrito em `prompts_prototipacao.md`, **integrando a visão estratégica do AdaptiveHarmonicAI (Glass Box)** e **alinhada às tendências de IA explicável, eficiência e confiança** destacadas nas fontes anexas.

## Prompt 1 — Definição do Escopo de Valor (UVP e Usuário)

### 1️⃣ A Proposta de Valor em Ação (UVP)

**Como demonstrar o contraste entre Caixa Preta e Caixa de Vidro em < 3 minutos**

**Cenário da demonstração (MVP simples):**

* O usuário insere **uma mesma melodia curta (8 compassos)**.
* O sistema apresenta **duas harmonizações paralelas**:

  * **Modo Caixa Preta**: harmonização gerada automaticamente, sem explicação.
  * **Modo Caixa de Vidro (Glass Box)**: harmonização acompanhada de:

    * Função harmônica (T / S / D)
    * Grau de tensão
    * Justificativa de condução de vozes
    * Probabilidade de permanência ou transição funcional

**Aha! Moment específico**

> O usuário percebe que **não está avaliando se “gostou do som”**, mas **se concorda ou não com a decisão musical** — e que pode intervir de forma consciente.

O momento-chave ocorre quando:

* O sistema explica algo como:

  > “Escolhi G7 porque a melodia antecipa a tônica C e a condução de vozes minimiza salto interno.”
* E o usuário pode:

  * Aceitar a decisão
  * Forçar uma alternativa (ex: Subdominante)
  * Ver imediatamente **o impacto teórico e musical da mudança**

👉 **Valor provado:**
Não é geração de música — é **governança da decisão musical**.

### 2️⃣ O Usuário Ideal para o Teste Inicial

**Escolha prioritária: Educadores Musicais**

**Justificativa estratégica**

Entre produtores profissionais e educadores musicais, **os educadores sentem a dor da falta de explicabilidade de forma mais imediata e explícita**.

**Por quê educadores primeiro:**

* A dor é **estrutural**, não subjetiva:

  * Eles precisam explicar *por que* algo funciona.
  * Modelos “black box” são inutilizáveis pedagogicamente.
* O feedback é:

  * Mais verbalizado
  * Mais rápido
  * Menos dependente de gosto pessoal
* Facilidade de acesso:

  * Professores, escolas, cursos online e workshops
* Clareza de validação:

  * Se não explica → não serve
  * Se explica → valor imediato

**Perfil ideal do usuário-teste**

* Professor de harmonia, composição ou arranjo
* Atua com DAW, MIDI ou piano
* Já frustrado com IAs que “geram mas não ensinam”

👉 **Estratégia implícita**

* Educadores validam o **valor cognitivo**
* Produtores escalam o **valor econômico** depois

## 🔎 Síntese do Escopo de Valor do MVP

* **UVP validada:**
  *Decisões harmônicas explicáveis, auditáveis e controláveis em tempo real.*

* **O que o protótipo precisa provar (e apenas isso):**

  * Que entender a decisão é mais valioso do que apenas ouvir o resultado
  * Que controle + explicação gera confiança

* **Usuário ideal inicial:**
  🎯 Educadores musicais (porta de entrada estratégica)

Se quiser, no próximo passo posso:

* Traduzir esse escopo em **3 features obrigatórias do MVP** (Prompt 2), ou
* Criar o **roteiro exato da demo de 5 minutos** (Prompt 3).

## Prompt 2: Seleção de Funcionalidades Essenciais (Features)

"Agora, atue como um Arquiteto de Soluções MVP. Para entregar a proposta de valor definida acima, quais são as 3 (e apenas 3) funcionalidades críticas que o protótipo DEVE ter?

* *Dica:* Considere que o diferencial não é o áudio final, mas o processo de decisão.
* **Feature 1 (Input/Geração):** Como o usuário insere ou gera a ideia inicial?
* **Feature 2 (O Motor Glass Box):** Como o sistema exibe a decisão harmônica e, crucialmente, a **justificativa** (ex: Tensão, Função, Voice Leading)?
* **Feature 3 (Intervenção/Governança):** Qual mecanismo de controle o usuário tem para aceitar, rejeitar ou ajustar a decisão baseada na explicação?"

## Resposta 2: Seleção de Funcionalidades Essenciais (Features)

A seguir está a **resposta ao Prompt 2 – Seleção de Funcionalidades Essenciais (Features)**, conforme definido em `prompts_prototipacao.md`, **alinhada à UVP de “Decisão Musical Auditável”** e coerente com as tendências de **IA explicável, eficiência computacional e confiança** destacadas nas fontes anexas.

## Prompt 2 — Seleção de Funcionalidades Essenciais (Features)

**Objetivo do MVP:**
Provar que o valor central do AdaptiveHarmonicAI **não está no áudio final**, mas na **qualidade, explicabilidade e governança da decisão harmônica**.

O protótipo deve conter **apenas 3 funcionalidades críticas**, cada uma claramente associada a uma etapa cognitiva do usuário.

### 🎹 Feature 1 — Input / Geração da Ideia Musical

**O que é:**
Entrada simples de uma **melodia curta em MIDI** (ou teclado virtual), sem preocupação com timbre ou mix.

**Por que é essencial:**

* Reduz fricção no teste
* Mantém foco na harmonia, não no som
* Permite comparação direta com IAs “caixa preta”

**Escopo mínimo:**

* Upload ou gravação de melodia monofônica (8–16 compassos)
* BPM e tonalidade detectados automaticamente (ou default)

👉 **Função estratégica:**
Criar um ponto de partida neutro para evidenciar que **o diferencial não está na criatividade inicial**, mas na decisão estrutural.

### 🧠 Feature 2 — Motor Glass Box (Decisão + Explicação)

**O que é:**
Visualização clara da **harmonização sugerida**, acompanhada da **justificativa musical explícita**.

**Elementos obrigatórios da explicação:**

* Função harmônica de cada acorde (T / S / D)
* Grau de tensão / estabilidade
* Lógica de condução de vozes
* Indicação de inércia ou transição funcional

**Formato de saída:**

* Acordes em MIDI + visual textual/simbólico da decisão
* Explicação legível para humanos (não matemática)

👉 **Função estratégica:**
Materializar a UVP:

> *“Aqui a IA não apenas sugere — ela explica por que decidiu.”*

Este é o **núcleo do produto**.

### 🎛️ Feature 3 — Intervenção / Governança da Decisão

**O que é:**
Capacidade do usuário **intervir conscientemente** na decisão harmônica com base na explicação recebida.

**Mecanismo mínimo de controle:**

* Aceitar a sugestão
* Forçar uma função alternativa (ex: trocar Dominante por Subdominante)
* Visualizar imediatamente:

  * O novo acorde
  * A mudança na justificativa harmônica

**O que NÃO é necessário:**

* Reharmonizações complexas
* Edição avançada de acordes
* Áudio realista

👉 **Função estratégica:**
Provar que o usuário deixa de “testar no escuro” e passa a **governar a decisão musical**.

## 🔎 Síntese Executiva das Features

| Etapa Cognitiva | Feature                | Valor Provado               |
| --------------- | ---------------------- | --------------------------- |
| Ideia           | Input MIDI simples     | Foco na decisão, não no som |
| Decisão         | Glass Box explicável   | Confiança e auditabilidade  |
| Controle        | Intervenção consciente | Governança criativa real    |

### ✅ Regra de ouro do MVP

Se uma funcionalidade **não ajuda o usuário a entender ou controlar a decisão**, ela **não entra** no protótipo.

Se quiser, posso seguir para:

* **Prompt 3 – Roteiro completo da demonstração (5 minutos)**, ou
* Ajustar essas features para um **MVP “Mágico de Oz” vs. funcional real (WASM/VST)**.

## Prompt 3: Roteiro de Demonstração (A Experiência)

"Atue como um Designer de Narrativa de Produto. Crie um roteiro passo-a-passo para uma demonstração de 5 minutos deste protótipo.

1. **O Cenário:** Descreva a situação inicial (ex: 'O usuário tem uma melodia, mas a IA generativa comum só entrega harmonias ruins ou inexplicáveis').
2. **A Interação:** Descreva o fluxo de uso. O usuário sobe a melodia -> O sistema sugere -> O sistema explica ('Escolhi G7 para preparar C devido à forte atração tonal') -> O usuário ajusta.
3. **O Fechamento:** Como a demonstração termina provando que o usuário teve 'superpoderes de decisão' e não apenas sorte aleatória?"

## Resposta 3: Roteiro de Demonstração (A Experiência)

A seguir está o **Prompt 3 – Roteiro completo da demonstração (5 minutos)**, conforme definido em `prompts_prototipação.md`, **traduzindo a UVP de “Decisão Musical Auditável” em uma experiência clara, memorável e convincente**, alinhada às tendências de **IA explicável, confiança e controle humano** destacadas nas fontes anexas.

## Prompt 3 — Roteiro de Demonstração (5 minutos)

**Objetivo da demo:**
Provar, em poucos minutos, que o usuário **ganha superpoderes de decisão musical**, e não apenas um resultado aleatório “que soa bem”.

**Público-alvo primário:** Educadores musicais
**Formato:** Demonstração guiada (ao vivo ou gravada)

### ⏱️ Minuto 0:00 – 1:00

## 1️⃣ O Cenário — A Frustração Atual

**Narrativa inicial (contexto):**

> “Imagine que você tem uma melodia simples para trabalhar em aula.
> Você pede ajuda a uma IA musical comum para harmonizar.”

**Ação:**

* Apresentar uma melodia curta (8 compassos).
* Mostrar rapidamente uma harmonização gerada por uma IA “caixa preta”.

**Problema explicitado:**

* Não há explicação.
* Não há função harmônica clara.
* Não é possível ensinar *por que* aquela progressão funciona.

**Mensagem-chave:**

> “Ela gera som. Mas não gera entendimento.”

### ⏱️ Minuto 1:00 – 2:30

## 2️⃣ A Interação — A Caixa de Vidro em Ação

**Transição narrativa:**

> “Agora, vamos usar o mesmo material musical com uma IA que não apenas sugere, mas explica.”

**Ação:**

* O usuário insere a mesma melodia no AdaptiveHarmonicAI.
* O sistema gera a harmonização.

**Destaque visual imediato:**

* Cada acorde aparece acompanhado de:

  * Função harmônica (T / S / D)
  * Grau de tensão
  * Observação de condução de vozes

**Exemplo de explicação exibida:**

> “Escolhi G7 porque a melodia antecipa C e a função Dominante maximiza a resolução tonal com menor movimento interno.”

**Mensagem-chave:**

> “Aqui, a IA não esconde a decisão — ela a torna legível.”

### ⏱️ Minuto 2:30 – 4:00

## 3️⃣ A Governança — O Usuário Assume o Controle

**Ponto central da demo (o verdadeiro “Aha!”):**

> “Mas entender não basta. Vamos governar a decisão.”

**Ação:**

* O usuário seleciona um acorde sugerido.
* Força uma alternativa funcional (ex: Subdominante em vez de Dominante).

**Resposta imediata do sistema:**

* Novo acorde é sugerido.
* A explicação muda em tempo real:

  * Menor tensão
  * Menor expectativa de resolução
  * Impacto na coerência tonal explicado

**Mensagem-chave:**

> “Você não está testando no escuro.
> Você está escolhendo com consciência.”

### ⏱️ Minuto 4:00 – 5:00

## 4️⃣ O Fechamento — Superpoderes de Decisão

**Conclusão narrativa:**

> “Compare isso com uma IA tradicional.”

**Contraste final:**

* Caixa preta: tentativa e erro, sem justificativa.
* Caixa de vidro: decisão auditável, ajustável e ensinável.

**Frase de encerramento (âncora de valor):**

> “Isso não é uma IA que compõe por você.
> É uma IA que pensa com você — e explica cada passo.”

**Resultado provado:**

* O usuário:

  * Entende *por que* a harmonia funciona
  * Consegue ensinar a decisão
  * Sente confiança para aceitar ou mudar

## 🔎 Síntese do Roteiro

| Etapa      | O que o usuário sente | Valor entregue      |
| ---------- | --------------------- | ------------------- |
| Cenário    | Frustração            | Dor explícita       |
| Interação  | Clareza               | Explicabilidade     |
| Governança | Controle              | Autoria e confiança |
| Fechamento | Poder                 | Decisão consciente  |

### ✅ Regra final da demo

Se o usuário sair dizendo

> “Agora eu entendo e controlo a harmonia”
> o MVP cumpriu sua missão.

Se quiser, o próximo passo natural é:

* **Prompt 4 – Validação e Métricas do Protótipo**, ou
* Adaptar este roteiro para **pitch de 3 minutos / demo comercial**.

## Prompt 4: Validação e Métricas do Protótipo

"Atue como um Pesquisador de UX. Quais perguntas devemos fazer ao usuário logo após ele testar o protótipo para validar se a UVP foi entregue?

1. **Validação de Problema:** Como confirmamos que a 'falta de explicação' era realmente uma dor?
2. **Validação de Solução:** Que métrica qualitativa ou quantitativa (ex: 'Confiança na Decisão', 'Clareza da Justificativa') define o sucesso deste teste?
3. **Sinal de Compra:** Qual comportamento indicaria que o usuário pagaria por essa 'governança' (ex: pedir para exportar o MIDI, pedir para integrar na DAW)?"

## Resposta 4: Validação e Métricas do Protótipo

A seguir está a **resposta ao Prompt 4 – Validação e Métricas do Protótipo**, conforme definido em `prompts_prototipação.md`, **fechando o ciclo de prototipagem Lean** e alinhada às tendências das fontes anexas sobre **confiança, IA explicável e adoção responsável**.

## Prompt 4 — Validação e Métricas do Protótipo

**Objetivo desta etapa:**
Confirmar se o protótipo **entregou a UVP real** (*Decisão Musical Auditável*) e se há **sinal claro de valor percebido e intenção de uso/pagamento**.

Público-alvo do teste: **Educadores musicais** (primário)

### 1️⃣ Validação de Problema

**Como confirmar que a “falta de explicação” era uma dor real**

**Perguntas-chave (qualitativas, pós-teste imediato):**

* “Antes deste protótipo, como você explicava uma harmonização gerada por IA para um aluno?”
* “Em algum momento você já evitou usar IA musical em aula por não conseguir justificar o resultado?”
* “O que foi mais frustrante: a qualidade da harmonia ou a impossibilidade de explicar *por que* ela funciona?”

**Sinal de validação forte do problema:**

* O usuário relata:

  * Frustração recorrente
  * Improviso pedagógico
  * Desconfiança estrutural de IAs “caixa preta”

👉 **Critério de sucesso:**
O usuário reconhece espontaneamente que **o problema não era o som, mas a falta de explicação e controle**.

### 2️⃣ Validação de Solução

**Métrica que define se a UVP foi entregue**

Como o valor é **cognitivo e de confiança**, a métrica principal **não é técnica**, é perceptiva.

#### Métrica primária (qualitativa estruturada)

> **Confiança na decisão harmônica (escala 1–5)**
> “Quão confiante você se sente em usar esta harmonização em aula ou justificar sua escolha?”

**Meta:**
≥ 4 em pelo menos 70% dos usuários

#### Métricas secundárias (observáveis)

* **Clareza da justificativa**

  * “A explicação fez sentido musicalmente para você?” (Sim / Parcial / Não)
* **Tempo de compreensão**

  * O usuário entende a lógica da decisão em < 30 segundos?
* **Uso da intervenção**

  * O usuário tenta alterar a decisão pelo menos uma vez?

👉 **Critério de sucesso da solução:**
O usuário **usa a explicação para decidir**, não apenas para “ler”.

### 3️⃣ Sinal de Compra

**Comportamento que indica disposição a pagar pela governança**

Mais importante do que “você pagaria?” é **o que o usuário tenta fazer a seguir**.

#### Sinais comportamentais fortes (prioridade)

* “Posso exportar isso em MIDI?”
* “Isso já funciona dentro da DAW?”
* “Dá para usar isso em sala de aula com alunos?”
* “Tem como salvar essa explicação junto com o exercício?”

#### Sinais fracos (não suficientes sozinhos)

* “Achei interessante”
* “É diferente”
* “Nunca vi algo assim”

👉 **Critério de sinal de compra real:**
O usuário tenta **levar a decisão para fora do protótipo**.

## 🔎 Síntese das Métricas de Validação

| Dimensão | O que validar | Como medir              |
| -------- | ------------- | ----------------------- |
| Problema | Dor real      | Relato espontâneo       |
| Solução  | Confiança     | Escala + uso            |
| Valor    | Governança    | Tentativa de exportação |

### ✅ Regra de decisão pós-teste

* Se **há dor + confiança + tentativa de uso real** → avançar para MVP funcional
* Se **há curiosidade sem ação** → ajustar explicação e controle
* Se **há rejeição pedagógica** → rever linguagem e visualização

Se quiser, no próximo passo posso:

* Consolidar essas métricas em um **template de teste de usuário (1 página)**, ou
* Traduzir os sinais de compra em **hipóteses claras de modelo de negócio inicial**.
