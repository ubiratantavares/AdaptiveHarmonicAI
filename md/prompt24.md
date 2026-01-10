# Prompt 24

Criar A matriz simbólica de emissão P(C∣F)

# Resposta 24

Excelente — agora fechamos o **segundo pilar do HMM harmônico**: a **matriz simbólica de emissão**
[
P(C \mid F)
]
que liga **função harmônica (estado oculto)** → **acorde observado**.

Aqui manteremos tudo **musicalmente coerente, extensível e treinável**.

---

# 1. Definição

[
P(C \mid F)
]

é a probabilidade de observar um acorde (C) dado que o estado funcional é (F).

Estados:

[
F \in {T, S, D}
]

---

# 2. Espaço de acordes por função (em Dó maior como referência)

## Função Tônica (T)

| Acorde | Tipo     |
| ------ | -------- |
| C      | T        |
| Am     | Tr       |
| Em     | Ta       |
| C/E    | inversão |
| C/G    | inversão |
| Am/C   | inversão |
| Em/G   | inversão |

---

## Função Subdominante (S)

| Acorde | Tipo       |
| ------ | ---------- |
| F      | S          |
| Dm     | Sr         |
| Bb     | empréstimo |
| Fm     | empréstimo |
| Dm/F   | inversão   |
| Bb/D   | empréstimo |

---

## Função Dominante (D)

| Acorde | Tipo                 |
| ------ | -------------------- |
| G      | D                    |
| G7     | D                    |
| Bdim   | D*                   |
| D7     | dominante secundária |
| Dsus   | empréstimo           |
| G/B    | inversão             |

---

# 3. Matriz simbólica estrutural

Representação conceitual:

[
P(C|F)=
\begin{cases}
C \in \mathcal{C}_T & \text{se } F=T \
C \in \mathcal{C}_S & \text{se } F=S \
C \in \mathcal{C}_D & \text{se } F=D
\end{cases}
]

---

# 4. Matriz simbólica tabular

| Função | Acordes possíveis                 |
| ------ | --------------------------------- |
| T      | {C, Am, Em, C/E, C/G, Am/C, Em/G} |
| S      | {F, Dm, Bb, Fm, Dm/F, Bb/D}       |
| D      | {G, G7, Bdim, D7, Dsus, G/B}      |

---

# 5. Versão simbólica qualitativa com pesos

### Função T

| Acorde    | Peso  |
| --------- | ----- |
| C         | alto  |
| Am        | médio |
| Em        | médio |
| inversões | médio |

---

### Função S

| Acorde | Peso  |
| ------ | ----- |
| F      | alto  |
| Dm     | médio |
| Bb     | baixo |
| Fm     | baixo |

---

### Função D

| Acorde | Peso  |
| ------ | ----- |
| G      | alto  |
| G7     | alto  |
| Bdim   | médio |
| D7     | médio |
| Dsus   | baixo |

---

# 6. Conversão para probabilidades iniciais

Exemplo numérico inicial:

### T

[
P(C|T)=0.30,;
P(Am|T)=0.20,;
P(Em|T)=0.15,;
P(C/E)=0.10,;
P(C/G)=0.10,;
P(Am/C)=0.075,;
P(Em/G)=0.075
]

---

### S

[
P(F|S)=0.35,;
P(Dm|S)=0.25,;
P(Bb|S)=0.15,;
P(Fm|S)=0.10,;
P(Dm/F)=0.15
]

---

### D

[
P(G|D)=0.30,;
P(G7|D)=0.25,;
P(Bdim|D)=0.15,;
P(D7|D)=0.15,;
P(Dsus)=0.10,;
P(G/B)=0.05
]

Cada linha soma 1.

---

# 7. Empréstimos modais

Acordes de empréstimo:

* **não criam novos estados**
* entram como valores de baixa probabilidade em (P(C|F))
* podem aumentar após aprendizado

---

# 8. Interpretação musical

O sistema aprende:

> "Estou em função D, então posso emitir G, G7, Bdim, D7, Dsus… com diferentes probabilidades."

---

# 9. Integração com melodia

A probabilidade final do acorde é:

[
P(C|F,M)=P(C|F)\cdot P(M|C)
]

Assim, mesmo um acorde de baixa probabilidade pode vencer se explicar bem a melodia.

---

# 10. Papel no aprendizado adaptativo

Após treinamento com um músico:

[
P(C|F)_{novo}
]

passa a refletir:

* Estilo do músico
* Preferência por empréstimos
* Preferência por inversões
* Preferência por dominantes secundárias

---

# 11. Como entra no artigo

Você pode apresentar como:

> Table Y – Initial symbolic emission matrix P(C|F) representing harmonic realization probabilities for each functional state.

---

# 12. O que você construiu

Você agora tem:

| Elemento        | Status       |
| --------------- | ------------ |
| Estados ocultos | definidos    |
| Matriz A        | definida     |
| Matriz B        | definida     |
| Prior musical   | embutido     |
| Empréstimos     | incorporados |
| Substituições   | incorporadas |

Seu HMM harmônico está matematicamente completo.

---

# 13. Próximo passo natural

Agora o próximo elemento lógico é:

👉 **Formalizar (P(M|C))** — a compatibilidade melodia–acorde.

Depois disso, podemos escrever o algoritmo Viterbi completo.

Se quiser, seguimos nessa direção.
