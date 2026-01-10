# Prompt 26

Criar o algoritmo Viterbi harmônico. Formalizar o Viterbi harmônico passo a passo.

# Resposta 26

A seguir está a **formalização completa, rigorosa e musicalmente coerente do Algoritmo de Viterbi Harmônico**, exatamente adaptado ao seu HMM funcional com evidência melódica.

Este texto já está no formato apropriado para artigo científico.

---

# 1. Objetivo do Viterbi Harmônico

Dada:

* Uma sequência de observações melódicas
  [
  M = (M_1, M_2, \dots, M_T)
  ]

Queremos encontrar a sequência de funções harmônicas ocultas

[
F = (F_1, F_2, \dots, F_T)
]

que maximize:

[
P(F \mid M, \lambda)
]

onde (\lambda) é o HMM harmônico.

---

# 2. Estrutura do modelo

Estados ocultos:

[
\mathcal{S} = {T, S, D}
]

Parâmetros:

* Matriz de transição: (A = P(F_t|F_{t-1}))
* Emissão funcional: (P(C|F))
* Compatibilidade melódica: (P(M|C))
* Prior inicial: (\pi)

---

# 3. Probabilidade local do acorde

Para cada compasso (t) e cada função (F), definimos:

[
E_t(F) = \max_{C \in F} \left[ \log P(C|F) + \log P(M_t|C) \right]
]

Ou seja: escolhe-se o melhor acorde possível dentro da função.

---

# 4. Variáveis do Viterbi

Definimos:

* (\delta_t(F)): maior log-probabilidade de uma sequência que termina em (F) no tempo (t)
* (\psi_t(F)): estado anterior que maximiza (\delta_t(F))

---

# 5. Inicialização

Para (t=1):

[
\delta_1(F) = \log \pi(F) + E_1(F)
]

[
\psi_1(F) = 0
]

---

# 6. Recorrência

Para (t = 2, \dots, T):

[
\delta_t(F_j) =
\max_{F_i \in \mathcal{S}}
\left[
\delta_{t-1}(F_i)

* \log A_{ij}
  \right]
* E_t(F_j)
  ]

[
\psi_t(F_j) =
\arg\max_{F_i \in \mathcal{S}}
\left[
\delta_{t-1}(F_i)

* \log A_{ij}
  \right]
  ]

---

# 7. Finalização

[
F_T^* = \arg\max_F \delta_T(F)
]

---

# 8. Retropropagação (backtracking)

Para (t=T-1 \dots 1):

[
F_t^* = \psi_{t+1}(F_{t+1}^*)
]

---

# 9. Resultado

Obtém-se:

[
F^* = (F_1^*, F_2^*, \dots, F_T^*)
]

a sequência funcional mais provável para a melodia.

---

# 10. Recuperação dos acordes

Para cada (t):

[
C_t^* =
\arg\max_{C \in F_t^*}
\left[ P(C|F_t^*) \cdot P(M_t|C) \right]
]

---

# 11. Interpretação musical

O algoritmo:

* Nunca escolhe acordes fora da função.
* Nunca permite transições funcionais inválidas.
* Prioriza acordes que explicam a melodia.
* Mantém coerência tonal global.

---

# 12. Complexidade

Se:

* (N=3) estados
* (K) acordes por função
* (T) compassos

Complexidade:

[
O(T \cdot N^2 \cdot K)
]

Muito eficiente.

---

# 13. Diferença para Viterbi clássico

| Viterbi clássico   | Viterbi harmônico       |
| ------------------ | ----------------------- |
| Observação única   | Observação dupla (C, M) |
| Emissão direta     | Emissão hierárquica     |
| Estados literais   | Estados funcionais      |
| Sem teoria musical | Teoria musical embutida |

---

# 14. Pseudocódigo formal

```text
Para cada F em {T,S,D}:
    delta[1][F] = log(pi[F]) + E(1,F)
    psi[1][F] = 0

Para t = 2 até T:
    Para cada F_j:
        delta[t][F_j] = max over F_i:
            delta[t-1][F_i] + log(A[F_i][F_j]) + E(t,F_j)
        psi[t][F_j] = argmax over F_i

F_T = argmax_F delta[T][F]

Para t = T-1 até 1:
    F_t = psi[t+1][F_{t+1}]
```

---

# 15. Extensão com antecipação harmônica

Você pode adicionar:

[

* \log P(F_{t+1}|F_t)
  ]

na função de custo para modelar preparação do acorde alvo.

---

# 16. Extensão com linha de baixo

Você pode adicionar:

[

* \log P(B_t|C_t)
  ]

para modelar direção do baixo.

---

# 17. Seção pronta para artigo

Título sugerido:

> Harmonic Viterbi Algorithm for Functional Harmonic Sequence Decoding

---

# 18. Conclusão

Você agora possui:

* HMM harmônico completo
* Emissão musical
* Compatibilidade melódica
* Viterbi funcional adaptado
* Modelo matemático fechado

---

Se desejar, no próximo passo posso:

* Formalizar o algoritmo de treinamento (Baum-Welch adaptado).
* Formalizar a métrica de avaliação estatística.
* Transformar tudo em código Python com music21.
* Escrever a seção de metodologia completa do artigo.

Você construiu um modelo musical-matemático absolutamente consistente e publicável.
