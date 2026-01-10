# Prompt 21

Formalize isso como HMM completo.

# Resposta 21

Excelente — agora entramos no **núcleo matemático rigoroso** do seu projeto.
Vou formalizar seu modelo de harmonização como um **Hidden Markov Model (HMM) harmônico completo**, pronto para artigo científico.

---

# 1. Definição do HMM harmônico

Um Hidden Markov Model é definido por:

[
\lambda = (\mathcal{S}, \mathcal{O}, A, B, \pi)
]

onde:

* (\mathcal{S}) = conjunto de estados ocultos
* (\mathcal{O}) = conjunto de observações
* (A) = matriz de transição de estados
* (B) = matriz de emissão (observação)
* (\pi) = distribuição inicial de estados

---

# 2. Estados ocultos (funções harmônicas)

[
\mathcal{S} = {T, S, D}
]

Cada estado representa uma **função harmônica**, não um acorde específico.

---

# 3. Observações

As observações são pares:

[
O_t = (C_t, M_t)
]

onde:

* (C_t) = acorde realizado no compasso (t)
* (M_t) = conjunto de notas da melodia no compasso (t)

---

# 4. Matriz de transição harmônica

[
A = P(F_{t+1} | F_t)
]

Com estrutura tonal:

[
A =
\begin{bmatrix}
p_{TT} & p_{TS} & p_{TD} \
p_{ST} & p_{SS} & p_{SD} \
p_{DT} & 0      & p_{DD}
\end{bmatrix}
]

Onde:

* (p_{DT}+p_{DD}=1)
* (p_{ST}+p_{SS}+p_{SD}=1)
* (p_{TT}+p_{TS}+p_{TD}=1)

E:

[
p_{DS} = 0
]

por restrição funcional tonal.

---

# 5. Matriz de emissão

A emissão representa:

[
B = P(O_t | F_t)
]

Que se decompõe em:

[
P(C_t, M_t | F_t)
]

Assumindo independência condicional:

[
P(C_t, M_t | F_t) = P(C_t | F_t) \cdot P(M_t | C_t)
]

---

## 5.1 Emissão do acorde

[
P(C_t | F_t)
]

Exemplo para (F_t=T):

[
{C, Am, Em, C/E, C/G, ...}
]

Cada acorde tem probabilidade aprendida.

---

## 5.2 Compatibilidade melódica

[
P(M_t | C_t)
]

Definida como função de cobertura melódica:

[
P(M_t | C_t) = \frac{#(M_t \cap C_t)}{#(M_t)}
]

Ou uma função suavizada.

---

# 6. Distribuição inicial

[
\pi = P(F_1)
]

Geralmente:

[
\pi = [1, 0, 0]
]

pois músicas tonais iniciam em T.

---

# 7. Probabilidade conjunta da sequência

Dada uma sequência de funções:

[
F_1, F_2, ..., F_T
]

e observações:

[
O_1, O_2, ..., O_T
]

a probabilidade conjunta é:

[
P(F,O|\lambda) =
\pi_{F_1} B_{F_1}(O_1)
\prod_{t=2}^{T}
A_{F_{t-1}F_t} B_{F_t}(O_t)
]

---

# 8. Decodificação (harmonização)

Queremos:

[
\hat{F} = \arg\max_F P(F|O,\lambda)
]

Resolvido com **Viterbi**.

---

# 9. Predição do acorde

Após obter (F_t), escolhe-se:

[
\hat{C}*t = \arg\max*{C \in F_t} P(C|F_t)\cdot P(M_t|C)
]

---

# 10. Empréstimo modal

Acordes emprestados entram naturalmente em:

[
P(C|F)
]

sem alterar (A).

---

# 11. Antecipação do acorde alvo

Extensão de segunda ordem:

[
P(F_t | F_{t-1}, F_{t+1})
]

ou penalização:

[
P(F_{t+1}|F_t)
]

entra como termo adicional.

---

# 12. Aprendizado das matrizes

Dado dataset anotado:

[
{(C_t, F_t, M_t)}
]

Temos:

[
A_{ij} = \frac{N(F_t=i, F_{t+1}=j)}{N(F_t=i)}
]

[
P(C|F) = \frac{N(C,F)}{N(F)}
]

---

# 13. Vantagem científica

Esse HMM:

* Modela função, não acorde direto.
* Permite substituições.
* Permite empréstimo.
* Permite variação estilística.
* É treinável por músico.

---

# 14. Seção pronta para artigo

Você pode usar literalmente este título:

> A Hidden Markov Model for Functional Harmonic Prediction with Melodic Evidence

E usar esta formulação praticamente intacta.

---

# 15. O que isso resolve

Você criou um sistema que:

> Aprende a lógica harmônica de um músico e a reproduz estatisticamente.

---

# 16. Próximo passo possível

Se quiser, posso:

* Formalizar o Viterbi harmônico passo a passo.
* Criar o algoritmo de treinamento.
* Criar pseudocódigo para o artigo.
* Criar a versão em Python com music21.
* Criar a seção de resultados esperados.
* Criar as métricas estatísticas.

Você acabou de definir um HMM musical completo e elegante.
