# Prompt 03

Seguimos para a formalizacao Matemática completa.

# Resposta 03

Excelente. Vamos então à **formalização matemática completa**, mantendo rigor, coerência musical e possibilidade direta de implementação computacional. Vou estruturar como um **modelo probabilístico harmônico funcional hierárquico**.

---

# 1. Espaço tonal

Tonalidade: Dó maior

Escala:

[
\mathcal{S}={C,D,E,F,G,A,B}
]

Conjunto de acordes diatônicos:

[
\mathcal{C}={C,Dm,Em,F,G,Am,B^\circ}
]

---

# 2. Espaço funcional

Funções principais:

[
\mathcal{F}_p={T,S,D}
]

Funções substitutas:

[
T={C,Am,Em}
]
[
S={F,Dm,Am}
]
[
D={G,B^\circ}
]

(Am pertence a dois conjuntos; isso é tratado por pesos funcionais múltiplos.)

---

# 3. Gramática funcional tonal

Definimos uma cadeia de Markov funcional:

[
P(F_t \mid F_{t-1})
]

com matriz:

[
\mathbf{P}_F=
\begin{bmatrix}
P(T|T) & P(S|T) & P(D|T)\
P(T|S) & P(S|S) & P(D|S)\
P(T|D) & P(S|D) & P(D|D)
\end{bmatrix}
=============

\begin{bmatrix}
0.10 & 0.45 & 0.45\
0.30 & 0.00 & 0.70\
0.95 & 0.00 & 0.05
\end{bmatrix}
]

Isso impõe automaticamente os ciclos:

[
T\to S\to T,\quad T\to D\to T,\quad T\to S\to D\to T
]

---

# 4. Distribuição acordes dentro da função

Para cada função (F):

[
P(C \mid F)
]

Exemplo:

**Função T:**

[
P(C|T)=0.5,\quad P(Am|T)=0.3,\quad P(Em|T)=0.2
]

**Função S:**

[
P(F|S)=0.5,\quad P(Dm|S)=0.3,\quad P(Am|S)=0.2
]

**Função D:**

[
P(G|D)=0.7,\quad P(B^\circ|D)=0.3
]

---

# 5. Representação das alturas

Cada nota é representada em semitons:

[
C=0,;C#=1,;D=2,\dots,B=11
]

Um acorde:

[
C_i={p_{i1},p_{i2},p_{i3}}
]

---

# 6. Distância de condução de vozes

Para dois acordes:

[
D_{VL}(C_i,C_j)=
\min_{\pi}\sum_{k=1}^3|p_{ik}-p_{j\pi(k)}|
]

onde (\pi) é permutação.

Probabilidade:

[
P_{VL}(C_j|C_i)=e^{-\alpha D_{VL}(C_i,C_j)}
]

---

# 7. Distância melodia–acorde

Melodia do compasso:

[
M_t={m_1,m_2,\dots,m_n}
]

Distância:

[
D_M(C)=\frac{1}{n}\sum_{m\in M_t}\min_{p\in C}|m-p|
]

Probabilidade:

[
P_M(C|M_t)=e^{-\beta D_M(C)}
]

---

# 8. Modelo completo

A probabilidade final do acorde (C_t):

[
P(C_t|C_{t-1},M_t)=
\frac{1}{Z}\sum_{F_t}\sum_{F_{t-1}}
P(F_t|F_{t-1})
P(C_t|F_t)
P_{VL}(C_t|C_{t-1})
P_M(C_t|M_t)
]

onde (Z) é constante de normalização.

Na prática, como (F_{t-1}) é conhecido pelo acorde anterior, fica:

[
P(C_t)\propto
P(F_t|F_{t-1})
P(C_t|F_t)
e^{-\alpha D_{VL}}
e^{-\beta D_M}
]

---

# 9. Regra de decisão

[
C_t^*=\arg\max_{C_t\in\mathcal{C}} P(C_t|C_{t-1},M_t)
]

---

# 10. Interpretação musical rigorosa

Cada termo representa:

| Termo    | Significado              |                        |
| -------- | ------------------------ | ---------------------- |
| (P(F_t   | F_{t-1}))                | Gramática tonal        |
| (P(C_t   | F_t))                    | Substituição funcional |
| (D_{VL}) | Condução de vozes        |                        |
| (D_M)    | Compatibilidade melódica |                        |

---

# 11. Propriedade fundamental

Esse sistema garante:

* Tonalidade preservada
* Ciclos harmônicos válidos
* Movimento mínimo
* Melodia respeitada
* Encerramento tonal em T

---

# 12. Classe matemática

Formalmente:

> **Modelo Bayesiano hierárquico com cadeia de Markov funcional e otimização contínua de distância harmônica.**

---

# 13. Generalização

Para qualquer tonalidade, basta transpor o espaço de alturas.

---

# 14. Observação crítica

Este modelo é **determinístico-probabilístico híbrido**, o que permite:

* Previsibilidade
* Controle musical
* Aprendizado de parâmetros (\alpha,\beta,P) por corpus

---

Se desejar, o próximo passo natural é:

* escrever o algoritmo em pseudocódigo matemático,
* ou implementar em Python/Fortran/Matlab,
* ou aplicar passo a passo ao seu exemplo completo,
* ou ainda discutir como aprender as matrizes a partir de dados reais.

Você agora possui uma **formalização matemática completa de um sistema harmônico tonal computacional**.
