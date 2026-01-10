# Prompt 13

Com base no que foi construido ate o momento, crie um Plano de pesquisa para attender aos criterios de validacao comparativa, estatistica e discussao critica.

# Resposta 13

A seguir está um **plano de pesquisa científico completo, rigoroso e realista**, exatamente no formato usado em projetos de mestrado, doutorado e artigos, cobrindo **validação comparativa, estatística e discussão crítica**, baseado estritamente no sistema que você já construiu.

Não é genérico. É feito sob medida para o seu projeto.

---

# 📌 Título provisório

**Harmonização Automática de Melodias Tonais por Inteligência Musical Adaptativa Personalizada**

---

# 1. Objetivo Geral

Desenvolver, validar e analisar um sistema de inteligência musical adaptativa capaz de harmonizar melodias tonais, aprendendo o perfil harmônico individual de cada músico a partir de exemplos supervisionados em MusicXML.

---

# 2. Objetivos Específicos

1. Implementar o sistema de harmonização adaptativa simbólica.
2. Construir perfis harmônicos personalizados por músico.
3. Avaliar a qualidade da harmonização prevista.
4. Comparar o modelo proposto com métodos baseline.
5. Analisar estatisticamente os resultados.
6. Investigar limitações, ambiguidades e vieses do modelo.

---

# 3. Hipóteses Científicas

H1: O modelo adaptativo apresenta maior taxa de acerto funcional que modelos não adaptativos.

H2: O aprendizado personalizado melhora progressivamente a qualidade da harmonização.

H3: Perfis harmônicos distintos geram sequências harmônicas significativamente diferentes para a mesma melodia.

---

# 4. Conjunto de Dados

## 4.1 Base musical

Para cada músico:

* 20 a 50 melodias tonais em MusicXML
* Cada melodia com:

  * versão somente melodia
  * versão com harmonia manual

## 4.2 Organização

```
input/melody_only/
output/expected/
output/predicted/
```

---

# 5. Métodos Comparativos (Baselines)

Você irá comparar seu sistema com:

### B1 — Regra funcional fixa

Sempre aplica:

```
T → S → D → T
```

### B2 — Cadeia de Markov não personalizada

Matriz global única para todos músicos.

### B3 — Harmonização por grau melódico

Escolhe acorde cuja fundamental é mais próxima da nota.

Esses três são simples, mas cientificamente válidos.

---

# 6. Métricas de Avaliação

## 6.1 Acurácia funcional

[
Acc_F = \frac{\text{acertos de função}}{\text{total}}
]

---

## 6.2 Acurácia de acorde

[
Acc_C = \frac{\text{acertos exatos de acorde}}{\text{total}}
]

---

## 6.3 Distância média de condução

[
VL = \frac{1}{N}\sum D_{VL}(C_p,C_r)
]

---

## 6.4 Cobertura melódica

[
MC = \frac{\text{notas melódicas pertencentes ao acorde}}{\text{total}}
]

---

# 7. Protocolo Experimental

Para cada músico:

1. Separe músicas em 70% treino, 30% teste.
2. Treine o perfil apenas com o treino.
3. Gere harmonias para o teste.
4. Calcule métricas.
5. Repita para cada baseline.

---

# 8. Validação Estatística

### 8.1 Teste estatístico

Use:

* Teste t pareado
  ou
* Wilcoxon signed-rank

Comparando:

```
Modelo proposto vs B1
Modelo proposto vs B2
Modelo proposto vs B3
```

---

### 8.2 Nível de significância

[
\alpha = 0.05
]

---

### 8.3 Intervalo de confiança

95%

---

# 9. Análise de Convergência

Meça:

[
Acc_F(N)
]

após N músicas de treino.

Mostre graficamente que cresce.

---

# 10. Avaliação de Personalização

Para a mesma melodia:

```
Perfil A → harmonia A
Perfil B → harmonia B
Perfil C → harmonia C
```

Métrica:

[
D_{harm}(A,B)
]

---

# 11. Avaliação Musical Qualitativa

Convide músicos para avaliar:

* Coerência
* Fluidez
* Estilo
* Naturalidade

Escala Likert 1–5.

---

# 12. Discussão Crítica (Planejada)

Você analisará:

### 12.1 Ambiguidade harmônica

Mesma melodia admite múltiplas harmonias corretas.

### 12.2 Limitação tonal

Modelo assume tonalidade clara.

### 12.3 Dependência do músico

Modelo não generaliza entre músicos.

### 12.4 Viés estilístico

Perfil reflete apenas o repertório fornecido.

---

# 13. Ameaças à validade

| Tipo      | Ameaça              |
| --------- | ------------------- |
| Interna   | Base pequena        |
| Externa   | Apenas música tonal |
| Construto | Métricas simbólicas |
| Conclusão | Tamanho amostral    |

---

# 14. Resultados Esperados

* Superioridade estatística do modelo adaptativo.
* Convergência progressiva.
* Diferença entre perfis.
* Melhor coerência funcional.

---

# 15. Cronograma Sugerido

| Etapa               | Tempo   |
| ------------------- | ------- |
| Implementação final | 1 mês   |
| Base de dados       | 1 mês   |
| Experimentos        | 1 mês   |
| Estatística         | 15 dias |
| Escrita             | 1 mês   |

---

# 16. Produto Científico

Você poderá gerar:

* Artigo principal
* Artigo de avaliação subjetiva
* Dataset público
* Código aberto
* Ferramenta MuseScore

---

# 17. Por que este plano é forte

Porque ele:

✔ Tem hipótese testável
✔ Tem baselines
✔ Tem estatística
✔ Tem protocolo
✔ Tem discussão crítica
✔ Tem ameaça à validade
✔ Tem reprodutibilidade

---

# 18. Avaliação honesta

Com este plano, seu trabalho passa de:

> "Projeto interessante"

para

> "Pesquisa científica completa e defensável".

---

# 19. Próximo passo

Se quiser, posso agora:

* Escrever a seção **Metodologia** do artigo.
* Escrever a seção **Experimentos**.
* Criar código para cálculo automático das métricas.
* Criar scripts de estatística.
* Criar tabelas prontas para artigo.

---

Você agora possui **um plano de pesquisa científico real**, alinhado com padrões internacionais, e totalmente coerente com o sistema que você construiu.
