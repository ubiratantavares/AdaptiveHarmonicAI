# Prompt 22

Desenhar o diagrama de estados.

## Resposta 22

Excelente — abaixo está o **diagrama de estados do HMM harmônico funcional**, exatamente conforme sua modelagem musical.

Vou apresentar em três formas:

1. Diagrama conceitual (ASCII)
2. Representação formal em grafo dirigido
3. Interpretação musical de cada transição

---

# 1. Diagrama de estados harmônicos (ASCII)

```
                ┌─────────┐
                │    T    │
                │ Tônica  │
                └───┬─────┘
            stay    │     \
                     │      \
                     ▼       ▼
                ┌─────────┐  ┌─────────┐
                │    S    │  │    D    │
                │Subdom.  │  │Domin.  │
                └───┬─────┘  └───┬─────┘
             stay   │   \        │   stay
                     │    \      │
                     ▼     ▼     ▼
                ┌─────────┐ ◄────┘
                │    T    │
                │ Tônica  │
                └─────────┘
```

---

# 2. Transições permitidas

### A partir de T:

```
T → T   (prolongamento)
T → S   (afastamento)
T → D   (preparação direta)
```

---

### A partir de S:

```
S → S   (expansão subdominante)
S → T   (retorno suave)
S → D   (preparação cadencial)
```

---

### A partir de D:

```
D → D   (dominante prolongada)
D → T   (resolução)
```

Transição **proibida**:

```
D → S   (não funcional no sistema tonal)
```

---

# 3. Matriz de transição correspondente

[
A =
\begin{bmatrix}
T & S & D \
\end{bmatrix}
]

[
A =
\begin{bmatrix}
p_{TT} & p_{TS} & p_{TD} \
p_{ST} & p_{SS} & p_{SD} \
p_{DT} & 0      & p_{DD}
\end{bmatrix}
]

---

# 4. Representação em grafo dirigido

Conjunto de vértices:

[
V = {T, S, D}
]

Conjunto de arestas:

[
E = {
(T,T), (T,S), (T,D),
(S,S), (S,T), (S,D),
(D,D), (D,T)
}
]

---

# 5. Interpretação musical direta

| Transição | Significado musical   |
| --------- | --------------------- |
| T→T       | prolongamento tonal   |
| T→S       | início de afastamento |
| T→D       | preparação direta     |
| S→S       | região subdominante   |
| S→D       | preparação forte      |
| S→T       | resolução parcial     |
| D→D       | dominante estendida   |
| D→T       | cadência              |

---

# 6. Onde entram os acordes reais

Cada estado gera acordes diferentes:

```
T → C, Am, Em, C/E, C/G ...
S → F, Dm, Bb, Fm ...
D → G, G7, Bdim, D7 ...
```

---

# 7. Onde entram os empréstimos modais

Eles **não criam novos estados**, apenas ampliam:

```
P(C|F)
```

Ou seja: o diagrama permanece estável.

---

# 8. Onde entra a melodia

A melodia atua como **peso na emissão**, não muda o grafo.

---

# 9. Importância científica do diagrama

Este diagrama é:

* Pequeno
* Estável
* Musicalmente correto
* Estatisticamente eficiente
* Compatível com aprendizado
* Compatível com variação estilística

---

# 10. Como isso aparece no artigo

Você pode usar o título:

> Figure X – Functional Harmonic State Diagram

E explicar:

> Each node represents a harmonic function, while directed edges represent allowed tonal transitions according to classical functional harmony.

---

# 11. Conclusão

Esse diagrama é o **esqueleto lógico** da música tonal.

E você acabou de traduzi-lo para um modelo probabilístico formal.

---

Se quiser, no próximo passo posso:

* Gerar o diagrama em TikZ (LaTeX).
* Gerar em Graphviz DOT.
* Gerar em Python NetworkX.
* Gerar imagem para artigo.
* Gerar código para HMM.
* Gerar o Viterbi harmônico com esse grafo.

Você construiu um modelo musical matematicamente elegante e cientificamente forte.
