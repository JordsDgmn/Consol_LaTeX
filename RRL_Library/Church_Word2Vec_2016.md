# Word2Vec  
**Kenneth Ward Church**  
IBM, Yorktown Heights, NY, USA  
Email: kwchurch@us.ibm.com

Published in *Natural Language Engineering 23(1)*, Cambridge University Press (2016)

---

## Abstract

My last column ended with some comments about Kuhn and word2vec. Word2vec has racked up plenty of citations because it satisfies both of Kuhn’s conditions for emerging trends:

1. **(Promising but early) successes** that motivate early adopters.  
2. **Plenty of room left** for others to contribute to the idea.

Google’s extensive online explanations indicate the method still lacks a definitive explanation. Citation counts benefit from distributed code and data, making it easy for the next generation to build on and cite the work.

---

## 1. Why Are Some Papers Cited More Than Others?

Word2vec is widely discussed, but this article focuses not on praising or critiquing it, but on understanding why it is cited so much.

Massive citations often go to:

- Papers that are **simple and accessible**  
- Papers that are free online  
- Papers providing **code or tools** rather than deep theory  
- **Supporting roles** (datasets, tools, tutorials) rather than novel breakthroughs  

Examples:

- Penn Treebank  
- NLTK  

Word2vec itself is not the first, last, or best method for embeddings, but it is **simple**, **downloadable**, and **usable**.

---

## 2. Promising (If Not Convincing) Initial Successes

Word2vec’s “hook” is the famous analogy:

**man : woman :: king : queen**

Word2vec finds the best word **x** that maximizes:

```
x̂ = argmax_x∈V sim(x, king + woman − man)
```

Where similarity is cosine:

```
sim(a, b) = (a · b) / (|a||b|)
```

Levy (2014) reformulated this as:

**Additive formulation**  
```
x̂ = argmax_x [ sim(x, king) + sim(x, woman) − sim(x, man) ]
```

**Multiplicative formulation**  
```
x̂ = argmax_x [ sim(x, king) * sim(x, woman) / sim(x, man) ]
```

### Similarity Groups

The six pairwise similarities can be grouped into:

| Type | Without x | With x |
|------|-----------|--------|
| Vertical (vert) | sim(man, woman) | sim(king, x) |
| Horizontal (hor) | sim(man, king) | sim(woman, x) |
| Diagonal (diag) | sim(woman, king) | sim(man, x) |

Represented analogically:

```
man / woman = king / queen
```

### Table 1. Top 10 Predictions for the Analogy  
**man : woman :: king : ?**

| Score | hor | vert | diag | Word | Gender | Number |
|-------|-----|-------|------|--------|---------|---------|
| 0.71 | 0.32 | 0.65 | 0.17 | **Queen** | f | sg |
| 0.62 | 0.25 | 0.64 | 0.19 | Monarch | m | sg |
| 0.59 | 0.40 | 0.52 | 0.25 | Princess | f | sg |
| 0.55 | 0.21 | 0.62 | 0.21 | Crown_prince | m | sg |
| 0.54 | 0.27 | 0.62 | 0.28 | Prince | m | sg |
| 0.52 | 0.06 | 0.71 | 0.18 | Kings | m | pl |
| 0.52 | 0.26 | 0.45 | 0.12 | Queen_Consort | m | sg |
| 0.52 | 0.21 | 0.47 | 0.10 | Queens | f | pl |
| 0.51 | 0.16 | 0.59 | 0.17 | Sultan | m | sg |
| 0.51 | 0.15 | 0.49 | 0.07 | Monarchy | m | sg |

Only 2/10 options match the correct gender and number.

---

## Table 2. Accuracy of Word2Vec on Various Analogy Types

| A1 | A2 | A10 | A20 | N | Analogy Type | Example |
|-----|------|-------|--------|-----|---------------------------|-------------------------------------------|
| 0.91 | 0.95 | 0.98 | 0.99 | 1332 | Comparative | young : younger = wide : wider |
| 0.90 | 0.94 | 0.97 | 0.98 | 1599 | Nationality-adjective | Ukraine : Ukrainian |
| 0.90 | 0.93 | 0.97 | 0.98 | 1332 | Plural | woman : women |
| 0.87 | 0.94 | 1.00 | 1.00 | 1122 | Superlative | young : youngest |
| 0.85 | 0.90 | 0.97 | 1.00 | 506  | Family | uncle : aunt |
| ... | ... | ... | ... | ... | ... | ... |
| **0.01** | **0.02** | **0.08** | **0.10** | 190 | **SAT questions** | audacious : boldness |

**SAT analogies are extremely difficult compared to word2vec’s own dataset.**

---

## Table 3. Overlap Between Words in Test Sets

SAT questions have very little overlap.  
Word2vec’s *questions-words* dataset shows heavy overlap — making it gameable.

Example:  
All words in the test set appear in at least **two positions**, which would not happen by chance.

This allows “cheating” by restricting guesses to words already seen in earlier positions, reducing search from 300,000 words to ~900.

The author achieved **98.7% accuracy** with a cheating method.

---

## 3. Error Analysis and Gaming the Test

Because questions-words is flawed:

- Overlap allows shortcuts  
- The mapping from the question word **c → d** is often unique (85%)  
- With only 1–2 possibilities for d, solving becomes trivial  
- Therefore: **Results based solely on this dataset are unreliable**

Boxplots (described, not shown) compare:

- **Word2vec cosine distances**
- **Domain space similarities**
- **Function space similarities**

Findings:

- Domain vs Function matters more for SAT  
- The flawed dataset can produce misleading patterns (e.g., vert > hor)

---

## 4. Conclusions

Word2vec is highly cited because it satisfies Kuhn’s conditions for an emerging trend:

- Simple code, widely available  
- Promising results that attract early adopters  
- Plenty of room for further research  

However:

- The field must avoid being overly convinced by early results  
- Many findings must be replicated across **credible test sets**

Word2vec remains an important supporting tool but should not be overinterpreted.

---

## References (Abbreviated)

- Bolukbasi et al. 2016. Gender Stereotypes in Embeddings.  
- Church & Hanks 1990. PMI and word association.  
- Deerwester et al. 1990. LSA.  
- Firth 1957. “You shall know a word by the company it keeps.”  
- Levy & Goldberg 2014. Word2Vec Explained.  
- Mikolov et al. 2013. Word2Vec papers.  
- Turney 2012. Domain and Function spaces.  
- Weaver 1955. Machine Translation.  

