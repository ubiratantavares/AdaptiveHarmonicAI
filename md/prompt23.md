# Prompt 23

Criar a matriz inicial simbólica.

# Resposta 23

Perfeito. Vamos agora criar a **matriz de transição harmônica simbólica inicial** do seu HMM, **antes do aprendizado estatístico**, baseada apenas na teoria musical funcional.

Essa matriz é a base do seu sistema adaptativo.

---

# 1. Ordem dos estados

Definimos a ordem fixa:

[
[T, S, D]
]

---

# 2. Matriz simbólica de transição funcional

[
A =
\begin{bmatrix}
T & S & D \
\end{bmatrix}
]

[
A =
\begin{bmatrix}
a_{TT} & a_{TS} & a_{TD} \
a_{ST} & a_{SS} & a_{SD} \
a_{DT} & a_{DS} & a_{DD}
\end{bmatrix}
]

---

# 3. Restrições funcionais

Com base na harmonia tonal:

* (a_{DS} = 0)
* Todas as linhas somam 1

---

# 4. Matriz simbólica inicial (não numérica)

[
A_{simb} =
\begin{bmatrix}
T\to T & T\to S & T\to D \
S\to T & S\to S & S\to D \
D\to T & 0      & D\to D
\end{bmatrix}
]

---

# 5. Versão com pesos simbólicos qualitativos

Para iniciar o sistema, podemos usar pesos linguísticos:

[
A_{qual} =
\begin{bmatrix}
alta & média & média \
média & média & alta \
alta & 0 & média
\end{bmatrix}
]

Interpretação:

| Transição | Peso  |
| --------- | ----- |
| T→T       | alta  |
| T→S       | média |
| T→D       | média |
| S→T       | média |
| S→S       | média |
| S→D       | alta  |
| D→T       | alta  |
| D→D       | média |

---

# 6. Conversão para valores iniciais normalizados

Uma inicialização coerente:

[
A =
\begin{bmatrix}
0.4 & 0.3 & 0.3 \
0.3 & 0.3 & 0.4 \
0.6 & 0.0 & 0.4
\end{bmatrix}
]

Cada linha soma 1.

---

# 7. Interpretação musical

| Linha | Significado                                         |
| ----- | --------------------------------------------------- |
| T     | maior chance de prolongamento, mas pode ir a S ou D |
| S     | maior tendência a ir para D                         |
| D     | resolve preferencialmente em T                      |

---

# 8. Importância dessa matriz simbólica

Ela é:

* Musicalmente válida
* Estatisticamente estável
* Excelente ponto inicial para aprendizado
* Evita transições não musicais

---

# 9. Como entra no aprendizado

Durante o treinamento:

[
A_{ij}^{novo} =
\frac{N(F_t=i, F_{t+1}=j) + \alpha A_{ij}^{simb}}
{\sum_k N(F_t=i, F_{t+1}=k) + \alpha}
]

onde (\alpha) é o peso da prior musical.

---

# 10. Como entra no artigo

Você pode apresentar como:

> Table X – Initial symbolic harmonic transition matrix used as musical prior.

---

# 11. Próximo passo natural

Agora o próximo elemento do HMM é:

👉 **A matriz simbólica de emissão (P(C|F))**

Se quiser, posso construir essa também de forma simbólica para cada função harmônica.
