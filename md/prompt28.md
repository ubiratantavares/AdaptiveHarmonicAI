# Prompt 28

Formalizar a métrica de avaliação estatística.

# Resposta 28

Excelente. Agora formalizamos as **métricas estatísticas de avaliação** do seu HMM harmônico de forma rigorosa, musicalmente coerente e cientificamente publicável.

---

# 1. Objetivo da avaliação

Avaliar quão bem o modelo:

1. Prediz acordes coerentes com a melodia.
2. Respeita a gramática harmônica funcional.
3. Generaliza para músicas não vistas.
4. Preserva estilo harmônico.
5. Aprende empréstimos modais e dominantes secundárias.

---

# 2. Conjuntos de avaliação

Divisão:

* Treino: 70%
* Validação: 15%
* Teste: 15%

Ou validação cruzada K-fold.

---

# 3. Métrica fundamental: Log-Verossimilhança

Para uma música:

[
\mathcal{L} = \log P(O|\lambda)
]

onde:

[
O=(M,C)
]

Métrica global:

[
\bar{\mathcal{L}}=\frac{1}{N}\sum_{k=1}^N\log P(O^{(k)}|\lambda)
]

---

# 4. Perplexidade harmônica

[
Perplexidade = \exp\left(-\frac{1}{T}\sum_{t=1}^T \log P(O_t|\lambda)\right)
]

Menor → melhor.

---

# 5. Acurácia de previsão de acordes

[
Acc = \frac{#,acordes\ corretos}{#,total}
]

Com tolerâncias:

* Exata
* Mesma função
* Mesma tríade
* Mesma fundamental

---

# 6. Acurácia funcional

[
Acc_F=\frac{#,funções\ corretas}{#,total}
]

---

# 7. Distância harmônica

Baseada em círculo de quintas:

[
D(C_1,C_2)=|pos(C_1)-pos(C_2)|
]

Métrica média:

[
\bar D = \frac{1}{T}\sum_t D(\hat C_t,C_t)
]

---

# 8. Penalidade por quebra funcional

Defina:

[
Penalty = \frac{#,transições\ inválidas}{#,total}
]

---

# 9. Coerência melodia–harmonia

Usando sua função:

[
CMH=\frac{1}{T}\sum_t P(M_t|C_t)
]

---

# 10. Métrica F1 harmônica

Tratando cada acorde como classe:

[
F1=2\cdot\frac{precision\cdot recall}{precision+recall}
]

---

# 11. Similaridade estrutural de progressão

Usando distância de Levenshtein funcional:

[
Lev_F(F_{ref},F_{pred})
]

Normalizada.

---

# 12. Métrica de entropia harmônica

[
H=-\sum_C P(C)\log P(C)
]

Avalia diversidade aprendida.

---

# 13. Índice de criatividade controlada

[
Creat = \frac{H_{pred}}{H_{train}}
]

---

# 14. Score funcional global

Defina:

[
Score = w_1 Acc + w_2 Acc_F + w_3 CMH - w_4 D - w_5 Penalty
]

Pesos definidos por validação.

---

# 15. Teste estatístico

Comparação entre modelos:

* Teste t pareado
* Wilcoxon signed-rank
* Bootstrap

---

# 16. Curvas de aprendizado

Plot:

[
\bar{\mathcal{L}}(n)
]

---

# 17. Avaliação por músico

Matriz:

| Músico | Acc | CMH | D | Score |

---

# 18. Avaliação subjetiva musical

Opcional:

* Juízes músicos
* Likert 1–5

Correlação com métricas objetivas.

---

# 19. Critério de significância

[
p<0.05
]

---

# 20. Conclusão formal

O modelo é considerado musicalmente válido se:

[
Acc_F>0.85,\quad CMH>0.75,\quad Penalty<0.1
]

---

# 21. Nome científico

Você pode denominar:

> Harmonic Statistical Evaluation Framework (HSEF)

---

# 22. Próximo passo

Se desejar, posso:

* Criar código Python para cálculo dessas métricas.
* Criar scripts de validação cruzada.
* Gerar gráficos automáticos.
* Integrar com music21.
* Criar estrutura pronta para artigo científico.

---

Você agora possui **um sistema estatístico completo para validar cientificamente harmonia computacional funcional baseada em HMM**, alinhado com teoria musical e estatística moderna.
