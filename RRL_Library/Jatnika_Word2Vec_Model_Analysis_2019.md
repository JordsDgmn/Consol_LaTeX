# Word2Vec Model Analysis for Semantic Similarities in English Words
**Derry Jatnika, Moch Arif Bijaksana, Arie Ardiyanti Suryani**  
School of Computing, Telkom University, Bandung, Indonesia

Published in *Procedia Computer Science 157 (2019), 160–167*  
Open Access under CC BY-NC-ND 4.0

---

## Abstract
This study examines similarity calculation between English words using Word2Vec.  
The model is trained on **320,000 English Wikipedia articles**, then cosine similarity is used to calculate similarity.  
Evaluation uses **WordSim-353** (353 pairs) and **SimLex-999** (999 pairs), comparing model output with human-rated similarity via **Pearson Correlation**.

Best results:  
- **WordSim-353:** 0.665  
- **SimLex-999:** 0.284  
(using window size 9, vector size 300)

---

## Keywords
Word2Vec · Cosine Similarity · Pearson Correlation

---

# 1. Introduction
Semantic similarity is important in linguistics and NLP.  
Two words may differ syntactically yet share meaning (e.g., *me* vs. *I*).

NLP allows computers to process human language and compute similarity between words using embeddings.  
Word2Vec converts words into vectors, and cosine similarity computes similarity scores.

Window size and vector dimension significantly affect Word2Vec model quality.  
This study evaluates multiple configurations to determine the best-performing model.

---

# 2. Related Work
Previous Word2Vec studies evaluated:

- **CBOW**  
- **Skip-Gram**

Using 120,000 Wikipedia articles with minimal preprocessing.

Four models were built:  
- FW-CBOW  
- FW-SG  
- SW-CBOW  
- SW-SG  

Compared with Google News Skip-Gram (300d, window 5).

FW-CBOW performed best.

---

This study expands configurations using:  
- Window sizes: **3, 6, 9**  
- Vector dimensions: **50, 150, 300**  
- Dataset: **320,000 English Wikipedia articles**  
- Evaluation: **Pearson correlation** on WordSim-353 and SimLex-999.

---

# 3. Methodology

## 3.1 Semantic Similarity
Semantic similarity measures meaning overlap between words, phrases, or documents.

Applications:
- Text classification  
- Clustering  
- Summarization  

Examples include similarity between bicycle–motorcycle or car–horse.

### Table 1. Examples of Word Pair Relationships (from Mikolov)
| Relationship | Example 1 | Example 2 |
|-------------|-----------|-----------|
| France – Paris | Italy : Rome | Apple : iPhone |
| Big – Bigger | Small : Larger | Kona : Hawaii |
| Miami – Florida | Baltimore : Maryland | USA : Pizza |
| Einstein – Scientist | Messi : Midfielder | Obama : Barack |
| Sarkozy – France | Google : Android | Quick : Quicker |

---

## 3.2 System Overview

Workflow (Figure 1 in PDF):
1. Raw Wikipedia Corpus  
2. Preprocessing  
3. Word2Vec Training  
4. Cosine Similarity  
5. Pearson Correlation  
6. Finish

---

## 3.3 Word Embeddings
Word embeddings represent words as real-valued vectors.

Words appearing in similar contexts have similar vectors.

Word2Vec supports:
- **CBOW** (predict target from context)
- **Skip-Gram** (predict context from target)

Similarity ranges from **−1 to 1** via cosine similarity.

(Figure 2 & 3: Example vector spaces, CBOW/Skip-Gram architecture)

---

## 3.4 Dataset
Training data:
- **320,000 English Wikipedia XML articles**

Testing datasets:
- **WordSim-353** — 353 word pairs, similarity 0–10  
- **SimLex-999** — 999 pairs, focusing strictly on similarity (not relatedness)

Preprocessing:
- Tokenization  
- Case folding (e.g., *COMPUTER* → *computer*)

---

## 3.5 Word2Vec Configuration Setup
Models tested with:

**Window sizes:** 3, 6, 9  
**Vector dimensions:** 50, 150, 300  

Similarity uses cosine similarity:

### Formula (1): Cosine Similarity
```
similarity = cos(θ) = (x · y) / (||x|| ||y||)
```

Pearson correlation evaluates similarity quality:

### Formula (2): Pearson Correlation
```
corr = [ nΣxy – (Σx)(Σy) ] / sqrt( [nΣx² – (Σx)²][nΣy² – (Σy)²] )
```

### Table 2. Correlation Criteria
| r-value | Interpretation |
|--------|----------------|
| 0 | No correlation |
| 0–0.5 | Weak |
| 0.5–0.8 | Moderate |
| 0.8–1 | Strong |
| 1 | Perfect |

---

# 4. Evaluation

## 4.1 Testing Setup
9 total configurations:

### Table 3. Word2Vec Configurations
| Study | Window | Vector Dim |
|-------|---------|-------------|
| 1 | 3 | 50 |
| 2 | 3 | 150 |
| 3 | 3 | 300 |
| 4 | 6 | 50 |
| 5 | 6 | 150 |
| 6 | 6 | 300 |
| 7 | 9 | 50 |
| 8 | 9 | 150 |
| 9 | 9 | 300 |

---

## 4.2 Test Results

### Table 4. WordSim-353 Pearson Correlation
| Window | 50d | 150d | 300d |
|--------|------|--------|----------|
| 3 | 0.6005 | 0.6262 | 0.6225 |
| 6 | 0.6336 | 0.6463 | 0.6484 |
| 9 | 0.6478 | 0.6628 | **0.6653** |

**Best:** window 9, vector 300

---

### Table 5. SimLex-999 Pearson Correlation
| Window | 50d | 150d | 300d |
|--------|-------|--------|----------|
| 3 | 0.2369 | 0.2723 | 0.2633 |
| 6 | 0.2281 | 0.2560 | 0.2651 |
| 9 | 0.2279 | 0.2540 | **0.2845** |

**Best:** window 9, vector 300

---

### Table 6. Sample Similarity: WordSim-353
| Word Pair | Gold | Win=3 | Win=6 | Win=9 |
|-----------|-------|-----------|-----------|-----------|
| coast–shore | 9.10 | 0.8010 / 0.6577 / 0.6128 | 0.7900 / 0.6651 / 0.6374 | 0.7954 / 0.6787 / 0.6140 |
| book–paper | 7.46 | 0.5667 / 0.4807 / 0.4104 | … | … |

---

### Table 7. Sample Similarity: SimLex-999
| Word Pair | Gold | Win=3 | Win=6 | Win=9 |
|-----------|--------|-------------------------|---------------------------|---------------------------|
| fast–rapid | 9.85 | 0.5847 / 0.5092 / 0.3910 | 0.5481 / 0.4515 / 0.4168 | 0.5038 / 0.4753 / 0.4134 |
| happy–glad | 9.39 | 0.7375 / 0.6629 / 0.6371 | … | … |

---

# 5. Conclusion and Future Work

### Findings
1. **Best configuration:**  
   - Window size **9**  
   - Vector dimension **300**

2. **Performance:**
   - WordSim-353: **0.665** (moderate)  
   - SimLex-999: **0.284** (weak)

3. SimLex-999 scores lower because it measures **pure semantic similarity**, while WordSim-353 includes **relatedness**.

4. Larger window sizes and vector dimensions tend to improve correlation, but excessively large windows dilute meaningful context.

### Future Work
- Training on extremely large corpora is slow → parallelization recommended.

---

# References
(Handler 2014; Jin & Schuler 2015; Mikolov et al. 2013; Agirre et al. 2012; Mihalcea et al. 2006; Kliegr & Zamazal 2018; Hill et al. 2015; Lai et al. 2016; Rong 2014)

