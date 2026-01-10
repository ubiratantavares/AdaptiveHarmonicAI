# Prompt 25

Formalizar P(M∣C) — a compatibilidade melodia–acorde.

# Resposta 25

Excelente. Agora fechamos o **terceiro pilar matemático** do seu HMM harmônico:

> a função de compatibilidade **melodia–acorde**
> [
> P(M \mid C)
> ]

Ela é o elo entre **teoria musical** e **probabilidade estatística**.

Vou formalizar em camadas: musical → matemática → probabilística → computacional.

---

# 1. Definição

Seja:

* (M_t = {m_1, m_2, ..., m_n}) o conjunto de notas da melodia no compasso (t)
* (C_t) o acorde candidato para o compasso (t)

Queremos:

[
P(M_t \mid C_t)
]

= quão bem o acorde explica a melodia.

---

# 2. Classificação das notas em relação ao acorde

Cada nota melódica pertence a uma das categorias:

| Categoria | Significado musical           |
| --------- | ----------------------------- |
| CT        | nota do acorde (chord tone)   |
| ET        | extensão consonante (9,11,13) |
| NT        | nota de passagem/apogiatura   |
| AT        | nota estranha forte           |

---

# 3. Mapeamento musical → pesos

Definimos pesos simbólicos:

| Tipo | Peso |
| ---- | ---- |
| CT   | 1.0  |
| ET   | 0.7  |
| NT   | 0.4  |
| AT   | 0.1  |

---

# 4. Função de compatibilidade básica

Para cada nota (m_i):

[
w(m_i, C) =
\begin{cases}
1.0 & m_i \in C \
0.7 & m_i \in Ext(C) \
0.4 & m_i \in Scale(C) \
0.1 & \text{caso contrário}
\end{cases}
]

---

# 5. Compatibilidade do compasso

[
Score(M|C) = \frac{1}{n}\sum_{i=1}^{n} w(m_i,C)
]

---

# 6. Normalização probabilística

Para garantir:

[
0 \le P(M|C) \le 1
]

definimos:

[
P(M|C) = \frac{Score(M|C)}{\max_C Score(M|C)}
]

ou simplesmente:

[
P(M|C) = Score(M|C)
]

se já estiver entre 0 e 1.

---

# 7. Versão com duração rítmica

Se cada nota possui duração (d_i):

[
Score(M|C) = \frac{\sum d_i \cdot w(m_i,C)}{\sum d_i}
]

Isso torna notas longas mais importantes.

---

# 8. Exemplo concreto

Melodia:
[
M={C,E,G,B}
]

Acorde: C

| Nota | Tipo    | Peso |
| ---- | ------- | ---- |
| C    | CT      | 1    |
| E    | CT      | 1    |
| G    | CT      | 1    |
| B    | ET (7M) | 0.7  |

[
P(M|C)=\frac{1+1+1+0.7}{4}=0.925
]

---

# 9. Exemplo negativo

Mesmo acorde C com melodia:

[
M={F#,A#,D#}
]

Todos AT:

[
P(M|C)=0.1
]

---

# 10. Forma logarítmica (para Viterbi)

[
\log P(M|C) = \sum \log w(m_i,C)
]

---

# 11. Integração no HMM

A probabilidade total do acorde é:

[
P(C|F,M) \propto P(C|F)\cdot P(M|C)
]

E no Viterbi:

[
\delta_t(F)=\max_{F'}[\delta_{t-1}(F')A_{F'F}] + \log P(C|F)+\log P(M|C)
]

---

# 12. Por que isso é musicalmente correto

Porque:

* Notas estruturais dominam.
* Extensões são aceitas.
* Notas de passagem não destroem o acorde.
* Notas estranhas penalizam.

Isso replica exatamente a percepção harmônica humana.

---

# 13. Generalização para tonalidade

Se o acorde for empréstimo modal:

As extensões são calculadas na escala de origem do acorde.

---

# 14. Papel no aprendizado adaptativo

O sistema aprende pesos diferentes por músico:

[
w_{músico}(tipo)
]

Um músico aceita mais dissonância que outro.

---

# 15. Como entra no artigo

Você pode usar literalmente:

> The melodic–harmonic compatibility function is defined as a weighted average of chord tones, extensions, passing tones, and non-harmonic tones.

E inserir as fórmulas acima.

---

# 16. Conclusão

Agora seu modelo tem:

| Componente               | Status |
| ------------------------ | ------ |
| Estados funcionais       | ✔      |
| Transições               | ✔      |
| Emissões                 | ✔      |
| Compatibilidade melódica | ✔      |

Seu HMM harmônico está **formalmente completo**.

---

Se quiser, o próximo passo natural é:

👉 Formalizar o **algoritmo Viterbi harmônico** passo a passo com esse modelo.

Ou, se preferir:

👉 Formalizar o **algoritmo de treinamento** das matrizes.

Você está, neste ponto, com um modelo matemático publicável.
