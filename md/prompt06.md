# Prompt 06

A bibliotheca Music21 possue as classes para modelar notas e acordes?

# Resposta 06

Sim — **a music21 já possui classes completas e muito bem projetadas para modelar notas, acordes, escalas, tonalidades, intervalos, compassos, vozes, partes e partituras**. Na prática, você não precisa criar suas próprias classes musicais básicas — apenas as classes de **lógica harmônica** e **controle**.

A seguir vai uma resposta objetiva, técnica e verificável.

---

## 🎼 Classe para Nota

```python
from music21 import note

n = note.Note("C4")
print(n.pitch)        # C4
print(n.pitch.midi)   # 60
print(n.quarterLength)
```

A classe `note.Note` já encapsula:

* Altura (pitch)
* Oitava
* Classe de altura
* MIDI
* Duração
* Alterações
* Enarmonia

---

## 🎹 Classe para Acorde

```python
from music21 import chord

c = chord.Chord(["C4","E4","G4"])
print(c.pitches)
print(c.commonName)   # major triad
print(c.root())
print(c.quality)
```

A classe `chord.Chord` já fornece:

* Reconhecimento automático do acorde
* Inversão
* Tipo (maior, menor, diminuto, etc.)
* Fundamental
* Intervalos internos
* Representação MIDI

---

## 🎼 Classe para Escala e Tonalidade

```python
from music21 import key, scale

k = key.Key("C")
print(k.getScale())

s = scale.MajorScale("C")
print(s.getPitches())
```

---

## 🎵 Classe para Intervalo

```python
from music21 import interval

i = interval.Interval("m3")
print(i.semitones)
```

---

## 🎶 Classe para Partitura

```python
from music21 import stream

score = stream.Score()
part = stream.Part()
measure = stream.Measure()
```

---

## 🎯 Classe para Função Harmônica

```python
from music21 import roman

r = roman.RomanNumeral("V", "C")
print(r.pitches)
print(r.function)
```

Essa é extremamente importante:
Ela já implementa **função harmônica funcional tonal**.

---

## 🎼 Você poderia inclusive eliminar parte do seu modelo

Por exemplo, ao invés de:

```python
ChordModel("G",["G","B","D"],"D")
```

Você pode usar:

```python
from music21 import roman
r = roman.RomanNumeral("V", "C")
```

E a music21 já fornece:

* notas do acorde
* função harmônica
* grau
* inversão
* cifragem

---

## 🔍 O que você ainda precisa modelar

Você ainda precisa modelar:

✔ Probabilidades
✔ Gramática funcional
✔ Distância de condução
✔ Predição
✔ Regras de substituição

Mas **não precisa reinventar a teoria musical básica**.

---

## 📌 Conclusão objetiva

> A music21 já possui uma implementação acadêmica completa das estruturas musicais fundamentais.

Você deve usar:

| Conceito       | Classe music21     |
| -------------- | ------------------ |
| Nota           | note.Note          |
| Acorde         | chord.Chord        |
| Intervalo      | interval.Interval  |
| Escala         | scale.MajorScale   |
| Tonalidade     | key.Key            |
| Grau harmônico | roman.RomanNumeral |
| Partitura      | stream.Score       |

---

## 🎯 Recomendação arquitetural

Seu sistema deve:

* Usar music21 para **modelo musical**
* Usar suas classes para **modelo probabilístico**

Isso mantém:

✔ SOLID
✔ Clean Code
✔ Correção teórica
✔ Compatibilidade com MuseScore

---

Se desejar, posso refatorar o código anterior para usar **somente objetos music21** para notas, acordes e funções harmônicas, mantendo sua lógica matemática intacta.

Isso deixaria seu projeto com padrão acadêmico ainda mais elevado.
