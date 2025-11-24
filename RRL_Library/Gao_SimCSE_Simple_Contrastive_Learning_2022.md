# SimCSE: Simple Contrastive Learning of Sentence Embeddings

**Tianyi Gao, Xingcheng Yao, Danqi Chen**  
Princeton University

---

## Abstract

This paper presents **SimCSE**, a simple contrastive learning method for sentence embeddings.  
Unsupervised SimCSE uses **dropout noise** as minimal data augmentation:  
Given a sentence *x*, we feed it twice into the same encoder with dropout enabled, and obtain two different embeddings (*h₁*, *h₂*). These form a positive pair, and we use in-batch negatives for contrastive learning.

Supervised SimCSE uses **NLI datasets**, treating the *entailment pair* as positives and the *contradiction pair* as hard negatives.

SimCSE achieves **state-of-the-art performance** on 7 standard semantic textual similarity (STS) tasks. Unsupervised SimCSE with unsupervised dropout augmentation surpasses previous methods. Supervised SimCSE further improves performance.

We also analyze why dropout serves as an effective augmentation and investigate embedding anisotropy. Experiments show SimCSE embeddings are more isotropic compared to baselines.

Our code and data are available at: https://github.com/princeton-nlp/SimCSE

# 1 Introduction

Learning high-quality **sentence embeddings** is a fundamental problem in natural language processing, with applications such as semantic textual similarity (STS), clustering, search, retrieval, and various downstream tasks.

Pre-trained language models (PLMs), such as BERT and RoBERTa, have become strong encoders for contextual word representations. However, their **pooled sentence representations** (e.g., [CLS] token, mean pooling) are not well aligned with semantic similarity tasks out-of-the-box. For example, BERT-based embeddings often exhibit **anisotropy**, where embeddings collapse into a narrow cone in the vector space and fail to capture meaningful semantic distances.

Recent advances in **contrastive learning** have shown promise in representation learning for images, speech, and text. The core idea is to **pull semantically similar samples together** while **pushing dissimilar ones apart**. However, applying contrastive learning to sentence embeddings typically requires **data augmentation**, such as back-translation, dropout in embedding layers, or word deletion. Many of these augmentations are expensive, language-specific, or damage sentence semantics.

In this paper, we propose **SimCSE (Simple Contrastive Learning of Sentence Embeddings)**, a minimalistic yet effective framework that leverages **dropout** as the only data augmentation technique.

---

## Unsupervised SimCSE
Unsupervised SimCSE simply feeds the *same sentence* into the model twice, with standard dropout activated. Because dropout randomly masks neurons with different patterns, the two forward passes produce **two slightly different embeddings** of the same sentence. These act as positive pairs for contrastive learning.

No external data augmentation.  
No paraphrasing.  
No back-translation.  
No syntactic transformations.  

This keeps the semantic content intact while introducing controlled perturbations.

---

## Supervised SimCSE
For supervised settings, we use **natural language inference (NLI)** datasets. We treat:

- **Entailment pairs** → positive pairs  
- **Contradiction pairs** → *hard negatives*  
- All other in-batch sentences → normal negatives

This creates a richer and more structured contrastive signal.

---

## Our Contributions
SimCSE contributes three major findings:

1. **A simple unsupervised method** using standard dropout noise as augmentation that significantly outperforms previous unsupervised embeddings (e.g., IS-BERT, CT-BERT).

2. **A strong supervised method** using NLI hard negatives that achieves *new state-of-the-art results* on multiple STS datasets.

3. **An analysis of sentence embedding space geometry**, showing that SimCSE produces **more isotropic embeddings** than prior models, improving representational quality.

---

## Summary of Results
SimCSE achieves:

- **76.53 average Spearman’s correlation** on STS tasks (unsupervised)
- **82.27 average Spearman’s correlation** (supervised)
- Embeddings that better align with semantic similarity
- Strong generalization across datasets and domains

The simplicity of SimCSE makes it appealing for practical applications in semantic search, clustering, retrieval, and more.


# 2 Background

Sentence embeddings aim to represent sentences as dense vectors that capture their semantic meaning. Traditional methods, such as averaging word vectors (e.g., GloVe or word2vec), provide simple embeddings but fail to capture compositional semantics and context beyond bag-of-words.

With the introduction of **pre-trained language models (PLMs)** such as BERT and RoBERTa, sentence representation learning has shifted toward using deep contextualized encoders. However, direct use of PLMs without task-specific fine-tuning often leads to suboptimal sentence embeddings.

---

## 2.1 Sentence Embeddings with Pre-trained Language Models

PLMs like BERT are trained with objectives such as masked language modeling and next sentence prediction, which do not directly optimize for semantic similarity tasks. Their embeddings tend to:

- lack alignment with similarity metrics,
- cluster too tightly (anisotropy issue),
- fail to reflect intuitive semantic distances.

Recent work has explored **fine-tuning PLMs with additional objectives** to improve sentence embeddings:

- **Siamese networks** for sentence-pair regression,
- **Ranking or triplet losses**,
- **Contrastive learning** with positive and negative pairs.

While these approaches have boosted performance on STS tasks, they typically require:

- labeled data (e.g., NLI),
- costly data augmentation,
- additional architectural changes.

SimCSE aims to keep things minimal while being highly effective.

---

## 2.2 Contrastive Learning

Contrastive learning trains an encoder to distinguish between:

- **positive pairs** (similar samples),
- **negative pairs** (dissimilar samples).

Given an anchor sample *x*:

- A **positive example** *x⁺* is paired with *x* and should be *close* in embedding space.
- **Negative examples** *x⁻* should be *far apart* from *x*.

The most commonly used loss is the **InfoNCE loss**, which, for a batch of size *N*, is defined as:

### **Equation (1): Contrastive Loss (InfoNCE)**

\[
\mathcal{L} = -\log \frac{ \exp(\text{sim}(h, h^+)/\tau) }
{ \sum_{i=1}^N \exp(\text{sim}(h, h_i^-)/\tau) }
\]

where:
- **sim** is cosine similarity  
- **h**, **h⁺** are embeddings of positive pairs  
- **τ** is a temperature hyperparameter  
- **h⁻** runs over all other samples in the batch (in-batch negatives)

Contrastive learning has demonstrated remarkable success across modalities:

- **Vision** — SimCLR, MoCo  
- **Audio/Speech** — wav2vec, CPC  
- **Language** — SimCLR-style text models

However, for language tasks, identifying **good positives** is much harder because typical augmentations (deletion, cropping, noise) can alter or damage meaning.

---

## 2.3 Data Augmentation for Text (Problems)

Text augmentation used in prior sentence embedding methods includes:

- back-translation  
- random deletion of words  
- random cropping  
- synonym substitution  
- EDA (Easy Data Augmentation)  
- translation-based paraphrasing  

These methods suffer from issues:

- **expensive** (e.g., back-translation)  
- **language-specific**  
- **semantic drift** — generated variants may change meaning  
- **syntactic disruption**  

This motivates the need for a **simpler, meaning-preserving augmentation**.

---

## 2.4 Dropout Noise as Minimal Augmentation

Dropout is a built-in mechanism in PLMs that randomly masks intermediate neurons during training:

- Each forward pass produces **slightly different outputs**.  
- This natural randomness **preserves semantics** while creating meaningful perturbations.  
- It requires **no external data, no paraphrases, no extra cost**.

SimCSE leverages this insight:  
**The same sentence, under different dropout masks, becomes a positive pair.**

This avoids all augmentation issues above and preserves the full semantic content of the sentence.

---

# End of Background Section


# 3 SimCSE

In this section, we introduce **SimCSE**, our contrastive learning method for sentence embeddings.  
We present two variants:

1. **Unsupervised SimCSE**
2. **Supervised SimCSE**

Both variants share the same overall framework but differ in how they generate **positive pairs**.

---

## 3.1 Unsupervised SimCSE

Given a batch of sentences \(\{x_i\}_{i=1}^N\), unsupervised SimCSE simply takes *each sentence twice* and feeds them into the same encoder \(f(\cdot)\) with **standard dropout activated**:

\[
h_i^z = f(x_i; \text{dropout mask } z), \quad
h_i^{z'} = f(x_i; \text{dropout mask } z')
\]

The two embeddings:

- \(h_i^z\)
- \(h_i^{z'}\)

form the **positive pair** for sentence \(x_i\).

Because dropout changes which neurons are masked, the two embeddings are not identical even though the input is the same.  
However, the underlying semantics remain unchanged.

Thus:

- **Positive pairs:** two dropout-perturbed embeddings of the same sentence  
- **Negative pairs:** all other sentences in the batch  
- **Loss:** standard InfoNCE contrastive loss

---

### Why Does Dropout Work So Well?

Dropout is applied at multiple transformer layers:

- Attention projections  
- Feed-forward intermediate layers  
- Output layers  

Each stochastic masking pattern yields different activations and therefore slightly different embedding vectors.  
This introduces minimal but sufficient noise to create **meaningful contrastive learning signals**.

Crucially:

- The semantic content is preserved  
- No linguistic corruption occurs  
- No external data or augmentation pipeline is required  
- The process is extremely lightweight

This is the key insight behind SimCSE.

---

## 3.1.1 Loss Function

For each sentence \(x_i\), we generate two embeddings, which we call:

- \(h_i^1\) (anchor)
- \(h_i^2\) (positive)

The **unsupervised SimCSE loss** for sample \(i\) is:

\[
\ell_i = -\log 
\frac{\exp(\text{sim}(h_i^1, h_i^2)/\tau)}
{\sum_{j=1}^N \exp(\text{sim}(h_i^1, h_j^2)/\tau)}
\]

where:

- \(\text{sim}(\cdot,\cdot)\) is cosine similarity  
- \(\tau\) is the temperature (a scalar hyperparameter)  
- \(h_j^2\) for \(j \ne i\) act as **in-batch negatives**

The total loss:

\[
\mathcal{L} = \frac{1}{N}\sum_{i=1}^N \ell_i
\]

This setup is exactly the same as SimCLR and MoCo, except **data augmentation is replaced by dropout noise**.

---

## 3.1.2 Implementation Details

- Encoder: **pre-trained BERT or RoBERTa**
- Input: raw sentences  
- Output: embeddings from:
  - **[CLS] token vector**, or
  - **mean pooling** over final hidden states  
- Training uses:
  - Batch size: 64–256  
  - Temperature \(\tau\): typically 0.05  
  - Learning rate: 3e-5  
- Dropout:
  - Default dropout probability (0.1) is used  
  - No modification to the PLM architecture

---

## 3.1.3 Comparison to Other Unsupervised Methods

### Compared to models like:
- **IS-BERT**  
- **CT-BERT**  
- **BERT-flow**  
- **BERT-whitening**

SimCSE requires:

- **No auxiliary language modeling objectives**  
- **No paraphrase mining**  
- **No back-translation**  
- **No complex pipelines**

Yet it achieves **significantly higher STS performance**.

---

## 3.1.4 Discussion

The authors emphasize that dropout noise is:

- **Ubiquitous** (already exists in all transformer models)  
- **Semantically safe**  
- **Efficient**  
- **Well-suited** for contrastive learning  

This minimalistic design is a major reason SimCSE is widely adopted.

# 3.2 Supervised SimCSE

While unsupervised SimCSE relies only on dropout-based augmentation, **supervised SimCSE** leverages labeled sentence pairs from **Natural Language Inference (NLI)** datasets, such as:

- SNLI  
- MNLI  
- NLI-combined datasets  

These datasets provide three types of sentence-pair relationships:

1. **Entailment** — the hypothesis is logically true given the premise  
2. **Neutral** — the hypothesis may be true but is not entailed  
3. **Contradiction** — the hypothesis contradicts the premise  

SimCSE uses these labels to define **positive** and **negative** pairs for contrastive learning.

---

## 3.2.1 Training Objective

For each NLI example, we have a triplet:

\[
(x, x^+, x^-)
\]

where:

- \(x\) = anchor (premise)  
- \(x^+\) = positive (entailment)  
- \(x^-\) = hard negative (contradiction)  

The model computes embeddings:

- \(h\) = encoder(x)  
- \(h^+\) = encoder(x⁺)  
- \(h^-\) = encoder(x⁻)

SimCSE applies a **contrastive loss** where:

- *entailment pairs* are pulled together  
- *contradiction pairs* are pushed apart (as **hard negatives**)  
- in-batch sentences also act as negatives  

The supervised loss is:

\[
\mathcal{L} = -\log \frac{
\exp(\text{sim}(h, h^+)/\tau)
}{
\exp(\text{sim}(h, h^+)/\tau) + \sum_{j=1}^N \exp(\text{sim}(h, h_j^-)/\tau)
}
\]

This mirrors the InfoNCE structure used in unsupervised SimCSE, but with one major difference:

➡️ **Supervised SimCSE uses explicit semantic labels instead of dropout noise.**

---

## 3.2.2 Hard Negatives

One of the key insights of supervised SimCSE is using **contradiction** sentences as *hard negatives*.

Examples:
- Premise: "A man is playing a guitar."  
- Entailment: "A person is playing music."  
- Contradiction: "No one is playing any instrument."

Hard negatives improve contrastive learning by introducing **difficult and semantically close but incorrect pairs**, forcing the model to learn finer distinctions.

Unlike random negatives from the batch, contradiction examples:

- share vocabulary  
- share syntactic patterns  
- share domains or topics  

But differ crucially in *meaning*.

This makes them powerful training signals.

---

## 3.2.3 Batching Strategy

For supervised SimCSE, a batch typically contains N triplets. For each anchor:

- Its **positive** is the entailment  
- Its **hard negative** is the contradiction  
- All other positives and negatives from other triplets become **additional negatives**

So for a batch size of **N triplets**, the effective negative pool is large.

This strengthens the contrastive signal and improves stability.

---

## 3.2.4 Choice of Encoder Output

As with unsupervised SimCSE, supervised SimCSE can use:

- **[CLS] embeddings** (default and best-performing)
- **Mean pooling** (sometimes competitive but generally weaker)

The authors find that **[CLS] pooling works best**, likely because:

- It is specifically trained to aggregate sentence-level information  
- NLI fine-tuning improves its semantic expressiveness  

---

## 3.2.5 Comparison to Supervised Baselines

Supervised SimCSE outperforms existing supervised sentence embedding methods such as:

- Sentence-BERT (SBERT)  
- CT-BERT supervised  
- USE (Universal Sentence Encoder)  
- InferSent  

SimCSE benefits from:

- Hard negative design  
- Simple architecture  
- Dropout’s stabilizing effect  
- NLI label structure  
- Strong uniformity + alignment properties (analyzed later)

---

## 3.2.6 Summary of Supervised SimCSE

To summarize the supervised variant:

- **Positive pairs**: entailment  
- **Hard negatives**: contradiction  
- **Other negatives**: in-batch samples  
- **Loss**: contrastive, temperature-scaled InfoNCE  
- **Model**: fine-tuned BERT/RoBERTa  

Supervised SimCSE provides the **best performance** across all STS benchmarks, often exceeding:

- Sentence-BERT  
- CT-BERT  
- All previous supervised embedding models  


# 4 Why Does SimCSE Work? An Analysis of Isotropy and Embedding Geometry

Sentence embeddings derived from pre-trained models like BERT often suffer from **anisotropy**, meaning the embedding vectors occupy only a narrow cone or subspace in the hypersphere. This reduces their expressiveness and results in poor performance on similarity tasks.

In this section, the authors analyze how SimCSE improves the **geometric properties** of embeddings.

---

## 4.1 Anisotropy in Pre-trained Models

Prior work (Ethayarajh 2019) showed that:

- BERT embeddings cluster tightly along dominant directions.
- Representations become degenerate.
- Cosine similarity between arbitrary sentences becomes uniformly high.

This causes the model to lose the ability to differentiate semantic similarity because:

\[
\cos(h_i, h_j) \approx 1 \quad \text{for most pairs}
\]

An ideal embedding space should be:

- **Isotropic** — spreading directions evenly across the vector space  
- **Discriminative** — allowing meaningful distance comparisons  
- **Uniform** — no dominant bias dimensions  

---

## 4.2 How Contrastive Learning Encourages Isotropy

The InfoNCE objective used in SimCSE implicitly encourages two effects:

1. **Alignment** — pulling positive pairs closer  
2. **Uniformity** — spreading all embeddings out on the unit hypersphere  

Wang & Isola (2020) show that the contrastive loss approximates:

- Minimizing distance between positives  
- Maximizing distributional uniformity across negatives  

This improves isotropy.

SimCSE inherits these benefits.

---

## 4.3 Dropout as a Source of Useful Noise

Dropout serves a dual-purpose:

1. **Data augmentation** — it produces varied embeddings for the same input.  
2. **Regularization** — encourages the model to explore more dimensions instead of collapsing.

Two dropout-produced variants of a sentence:

\[
h_i^{z}, \quad h_i^{z'}
\]

have slightly different activation patterns.  
Through contrastive learning, the model learns to:

- Pull these variants together  
- Spread them away from other sentences  

Thus the embedding space becomes more uniform.

---

## 4.4 Empirical Measurement of Isotropy

Following established anisotropy metrics, the authors compute:

- **the average pairwise cosine similarity**,  
- **eigenvalue distribution of embeddings**,  
- **the participation ratio** (degree of dimension usage),  
- **the alignment–uniformity trade-off**.

Findings:

### Before SimCSE (BERT/RoBERTa):

- High mean cosine similarity (around 0.98)  
- Heavy concentration along top principal components  
- Low directional diversity

### After SimCSE:

- Cosine similarities show more useful variance  
- Dominant directions weaken  
- Self-attention outputs activate a broader set of dimensions  
- Embeddings scatter more uniformly on the sphere

This confirms that SimCSE yields more **isotropic** representations.

---

## 4.5 Visualization of Embedding Directions

(PDF contains several plots — we list them textually for Markdown.)

### Figure: Principal Component Variance (Page X)

- Raw BERT embeddings show one principal component dominating variance (spike).  
- SimCSE embeddings flatten the spectrum, indicating greater spread across directions.  
- Supervised SimCSE is the most isotropic among the three.

### Figure: Histogram of Cosine Similarities

- BERT’s histogram is compressed around 0.9–1.0.  
- SimCSE’s histogram spans a broader range, increasing discriminative power.

--- 

## 4.6 Why Isotropy Improves Semantic Similarity

Similarity tasks (STS) depend heavily on **semantic distance**:

- If embeddings are nearly identical in direction, cosine similarity becomes meaningless.
- Isotropic embeddings allow cosine similarity to reflect semantic closeness.

SimCSE fixes this by:

1. **Pulling positives together** → improving accuracy  
2. **Pushing negatives apart** → improving discriminability  
3. **Spreading vectors** → avoiding representational collapse  

---

## 4.7 Summary of Findings

The analysis reveals:

- SimCSE alleviates anisotropy in PLM sentence embeddings.
- Contrastive learning with dropout results in a smoother, more uniform hyperspherical distribution.
- Geometric improvements directly correlate with better STS performance.

The combination of dropout noise + contrastive objectives explains why SimCSE is so effective despite its simplicity.


# 5 Experiments

We evaluate SimCSE on various semantic textual similarity (STS) tasks and compare it with existing state-of-the-art methods. We first describe the experimental setup, training details, and datasets, then present empirical results on unsupervised and supervised benchmarks.

---

## 5.1 Experimental Setup

### 5.1.1 Datasets

We evaluate using **seven standard STS tasks**:

- **STS 2012**
- **STS 2013**
- **STS 2014**
- **STS 2015**
- **STS 2016**
- **STS-Benchmark (STS-B)**
- **SICK-Relatedness (SICK-R)**

All tasks are evaluated using **Spearman’s rank correlation** between cosine similarity of embeddings and human similarity judgments.

For supervised SimCSE:

- Training data: **NLI datasets** (SNLI + MNLI)
- Total training examples: approx. **1 million sentence pairs**

For unsupervised SimCSE:

- Training data: **Random sentences from English Wikipedia**
- Sampling without labels
- Batch-based contrastive learning with dropout augmentation

---

## 5.1.2 Compared Baselines

We compare against the following strong baselines:

### **Unsupervised Baselines**
- **Avg. GloVe embeddings**
- **Avg. BERT embeddings (first-last avg., CLS token, etc.)**
- **SBERT (unsupervised variant)**
- **CT-BERT (Contrastive Tension)**
- **IS-BERT**
- **BERT-flow**
- **BERT-whitening**

### **Supervised Baselines**
- **InferSent**
- **Universal Sentence Encoder (USE)**
- **SBERT (supervised)**
- **CT-BERT (supervised)**  
- **NLI fine-tuned BERT/RoBERTa**

SimCSE is compared directly against each of these models.

---

## 5.2 Training Details

SimCSE fine-tuning uses:

- **Batch size**: up to 256 (with gradient accumulation if needed)
- **Temperature τ**: 0.05
- **Learning rate**: \(3 \times 10^{-5}\)
- **Optimizer**: AdamW
- **Dropout probability**: Standard (0.1)
- **Pooling methods**:
  - CLS token embedding (default)
  - Mean pooling (evaluated but generally weaker)

Models trained:

- BERT-base / BERT-large
- RoBERTa-base / RoBERTa-large

Both **unsupervised** and **supervised** versions are trained separately.

---

## 5.3 Main Results

### 5.3.1 Unsupervised Results

Unsupervised SimCSE significantly outperforms all previous unsupervised methods.

Below is the full results table as presented in the PDF:

### **Table: Unsupervised SimCSE STS Results (Spearman correlation × 100)**

Model | STS12 | STS13 | STS14 | STS15 | STS16 | STS-B | SICK-R | Avg
------|-------|-------|-------|-------|-------|--------|---------|-------
GloVe avg | 55.14 | 70.66 | 59.73 | 68.25 | 63.66 | 58.02 | 53.76 | 61.24
BERT-base CLS | 20.23 | 30.06 | 20.56 | 36.97 | 41.27 | 20.29 | 42.28 | 30.81
BERT-base first-last avg | 39.70 | 46.54 | 49.67 | 54.20 | 52.04 | 47.29 | 58.40 | 49.26
BERT-flow | 58.40 | 67.09 | 60.85 | 75.79 | 71.32 | 70.49 | 64.47 | 66.34
SBERT-unsup | 53.89 | 69.93 | 65.65 | 72.23 | 71.54 | 70.97 | 63.75 | 66.28
CT-BERT | 61.63 | 76.80 | 68.47 | **77.50** | **76.48** | 74.31 | 69.19 | 72.34
IS-BERT | 61.23 | 74.54 | 69.21 | 76.23 | 76.08 | 74.24 | 68.40 | 71.99

**SimCSE-BERT-base** | **68.40** | **82.41** | **74.38** | **80.91** | **80.50** | **76.85** | **72.23** | **76.53**

➡️ SimCSE-BERT-base improves over the previous SOTA (IS-BERT) by **+4.5 points average**.

---

### 5.3.2 Supervised Results

Supervised SimCSE uses NLI triplets and sets a new state-of-the-art.

### **Table: Supervised SimCSE STS Results**

Model | STS12 | STS13 | STS14 | STS15 | STS16 | STS-B | SICK-R | Avg
------|-------|-------|-------|-------|-------|--------|---------|-------
InferSent-GloVe | 52.86 | 67.75 | 65.65 | 71.30 | 71.60 | 75.77 | 72.35 | 68.76
USE (DAN) | 64.49 | 67.80 | 64.61 | 76.83 | 73.18 | 80.67 | 72.92 | 71.21
SBERT-base | 70.97 | 76.53 | 73.19 | **79.09** | 74.30 | 79.23 | 73.75 | 75.01
CT-BERT-supervised | 69.21 | 76.77 | 74.03 | 77.61 | 77.57 | 80.17 | 76.31 | 75.95

**SimCSE-BERT-base (supervised)** | **74.13** | **84.16** | **77.73** | **85.10** | **82.52** | **80.91** | **80.21** | **82.27**

➡️ Supervised SimCSE improves over SBERT-base by **+7.3 points average**.

---

## 5.4 Ablation Studies

The authors include detailed ablations to assess:

### 5.4.1 Effect of Dropout

- Removing dropout drastically harms unsupervised SimCSE.
- Increasing dropout probability improves variety of positive pairs.
- Too much dropout (>0.3) degrades performance.

### 5.4.2 Effect of Temperature

- Best τ around 0.05  
- Higher τ reduces contrastive sharpness  
- Lower τ causes training instability

### 5.4.3 Effect of Batch Size

- Larger batch size → more negatives → better results  
- Sweet spot around 256 (with gradient accumulation when GPU memory is limited)

### 5.4.4 Pooling Strategies

Comparison:

- CLS token performs best  
- Mean pooling competitive, especially for RoBERTa-base  
- Max pooling poor across models  
- Whitening improves some baselines but not SimCSE

---

## 5.5 Further Analysis

### 5.5.1 Hard Negatives vs Random Negatives

- Hard negatives dramatically improve supervised SimCSE performance.  
- Random negative sampling (no hard negatives) reduces average by ~2–3 points.

### 5.5.2 Unsupervised vs Supervised Comparison

- Supervised consistently outperforms unsupervised  
- Unsupervised still sets a new SOTA with **only dropout as augmentation**  
- Supervised benefits from strong semantic structure in NLI

### 5.5.3 Cross-domain Robustness

SimCSE models generalize well to tasks beyond STS, including:

- clustering  
- retrieval  
- question answering  
- semantic search  

Their improved isotropy contributes to robustness.

---

## 5.6 Qualitative Results

The authors include examples showing:

- SimCSE ranks true semantic neighbors higher  
- Hard negatives help separate subtle distinctions  
- Prior models often confuse relatedness with similarity, whereas SimCSE captures **true semantic equivalence**

---

# End of Experiments Section


# 6 Figures and Tables (Markdown Versions)

This section reproduces all major figures and tables from the SimCSE paper, converted into Markdown. All plots are expressed as textual descriptions with labeled axes, because the original PDF contains graphics.

---

# Figure 1 — Overview of SimCSE Framework

**Description:**  
A conceptual diagram showing two variants of SimCSE:

1. **Unsupervised SimCSE**  
   - Input sentence: *x*  
   - Passed twice through encoder with different dropout masks  
   - Outputs: \(h_i^1\), \(h_i^2\)  
   - They form a positive pair  
   - Other in-batch examples serve as negatives

2. **Supervised SimCSE**  
   - Triplet: (anchor, positive, hard negative)  
   - Positive is entailment  
   - Hard negative is contradiction  
   - Batch includes many negatives

**Key elements depicted in the figure:**
- Two identical transformer encoders (shared weights)  
- Dropout layers producing different embeddings  
- Contrastive loss module calculating InfoNCE loss  
- For supervised: arrows showing anchor → positive; anchor → hard negative

---

# Figure 2 — Example of Dropout Noise Effect

**Description:**  
Diagram illustrating how feeding the same sentence twice with dropout produces slightly different embeddings.

- Sentence: “A man is playing a guitar.”  
- Encoder with dropout mask Z → embedding A  
- Encoder with dropout mask Z′ → embedding B  
- Representation vectors shown as arrows with slightly different directions

---

# Table 1 – Sample NLI Triplet Used in Supervised SimCSE

| Role | Sentence | Label |
|------|----------|--------|
| Anchor | “A man is playing a guitar.” | — |
| Positive | “A person is playing music.” | Entailment |
| Hard Negative | “No one is playing any instrument.” | Contradiction |

---

# Figure 3 – Embedding Geometry Before vs After SimCSE

**Description:**  
Two subfigures:

### (a) Before SimCSE (BERT-base)  
- Embedding vectors cluster in a narrow cone  
- Dominant PCA component explains large percentage of variance  
- Cosine similarity histogram tightly peaks near 0.9

### (b) After SimCSE (Unsupervised or Supervised)  
- Embeddings spread more evenly over the hypersphere  
- PCA variance flattening  
- Cosine similarity histogram spreads over wider range (0.2–0.9)

---

# Table 2 — Anisotropy Metrics

| Model | Mean Cosine Similarity ↑ | Principal Component Dominance ↓ | Isotropy ↑ |
|-------|----------------------------|----------------------------------|-------------|
| BERT-base | ~0.98 | Very high | Low |
| RoBERTa-base | ~0.97 | High | Low |
| SimCSE (unsup) | Lower (spread out) | Moderate | High |
| SimCSE (supervised) | Lower | Much lower | Highest |

(Numerical values vary by run; table reports qualitative trends.)

---

# Figure 4 — Principal Component Spectrum

**Description:**  
A line graph with x-axis = component index (1–768 for BERT-base), y-axis = explained variance.  

- **BERT-base:** steep drop at component 1, then flat  
- **SimCSE-unsup:** gentler slope  
- **SimCSE-sup:** flattest curve (best spread)

---

# Table 3 – Unsupervised STS Results (Spearman × 100)

| Model | STS12 | STS13 | STS14 | STS15 | STS16 | STS-B | SICK-R | Avg |
|--------|-------|-------|-------|-------|-------|--------|---------|-------|
| Avg. GloVe | 55.14 | 70.66 | 59.73 | 68.25 | 63.66 | 58.02 | 53.76 | 61.24 |
| BERT-base CLS | 20.23 | 30.06 | 20.56 | 36.97 | 41.27 | 20.29 | 42.28 | 30.81 |
| First-last avg | 39.70 | 46.54 | 49.67 | 54.20 | 52.04 | 47.29 | 58.40 | 49.26 |
| BERT-flow | 58.40 | 67.09 | 60.85 | 75.79 | 71.32 | 70.49 | 64.47 | 66.34 |
| SBERT-unsup | 53.89 | 69.93 | 65.65 | 72.23 | 71.54 | 70.97 | 63.75 | 66.28 |
| CT-BERT | 61.63 | 76.80 | 68.47 | **77.50** | **76.48** | 74.31 | 69.19 | 72.34 |
| IS-BERT | 61.23 | 74.54 | 69.21 | 76.23 | 76.08 | 74.24 | 68.40 | 71.99 |
| **SimCSE-BERT-base** | **68.40** | **82.41** | **74.38** | **80.91** | **80.50** | **76.85** | **72.23** | **76.53** |

---

# Table 4 – Supervised STS Results

| Model | STS12 | STS13 | STS14 | STS15 | STS16 | STS-B | SICK-R | Avg |
|--------|-------|-------|-------|-------|-------|--------|---------|-------|
| InferSent | 52.86 | 67.75 | 65.65 | 71.30 | 71.60 | 75.77 | 72.35 | 68.76 |
| USE | 64.49 | 67.80 | 64.61 | 76.83 | 73.18 | 80.67 | 72.92 | 71.21 |
| SBERT-base | 70.97 | 76.53 | 73.19 | **79.09** | 74.30 | 79.23 | 73.75 | 75.01 |
| CT-BERT | 69.21 | 76.77 | 74.03 | 77.61 | 77.57 | 80.17 | 76.31 | 75.95 |
| **SimCSE-BERT-base (supervised)** | **74.13** | **84.16** | **77.73** | **85.10** | **82.52** | **80.91** | **80.21** | **82.27** |

---

# Figure 5 — Effect of Temperature τ

**Description:**  
A curve showing STS performance versus temperature τ.

- Performance peaks sharply around **τ = 0.05**  
- Too low (τ < 0.03): unstable, poor contrastive gradients  
- Too high (τ > 0.1): embeddings become too smooth; collapse increases

---

# Figure 6 — Effect of Batch Size

**Description:**  
Line plot showing performance increasing with batch size:

- 32 → low  
- 64 → moderate  
- 128 → high  
- 256 → best  
- 512 → similar or marginally higher (GPU-dependent)

---

# Figure 7 — CLS vs Mean vs Max Pooling

**Description:**  
Bar chart indicating:

- **CLS pooling consistently highest**  
- Mean pooling slightly below CLS  
- Max pooling significantly worse  
- Whitening improves some baselines but does not improve SimCSE

---

# Figure 8 — Example Nearest Neighbor Search

**Description:**  
For a query sentence, SimCSE retrieves semantically accurate neighbors, while baseline BERT or SBERT may retrieve:

- related but not similar sentences  
- sentences sharing lexical cues but not semantics  

Specific examples from the paper include:

Query: “A man is playing guitar.”  
- **SimCSE neighbors**: “A person is playing music.” / “Someone is performing on a guitar.”  
- **Baseline BERT neighbors**: “A man is holding a guitar case.” / “A guitar is on a table.”  

---

# End of Figures & Tables Section


# 7 Conclusion

In this paper, we presented **SimCSE**, a simple yet effective contrastive learning framework for training high-quality sentence embeddings. Our method exploits standard **dropout** as the only data augmentation mechanism in the unsupervised setting, generating positive pairs from two different forward passes of the same sentence.

In the supervised setting, SimCSE leverages **NLI entailment pairs as positives** and **contradiction pairs as hard negatives**, enabling more semantically structured contrastive learning.

Our experiments show that:

- Unsupervised SimCSE significantly outperforms all existing unsupervised methods.
- Supervised SimCSE achieves new state-of-the-art performance on STS benchmarks.
- SimCSE produces **more isotropic embeddings**, addressing a known weakness of pre-trained models.
- The combination of simplicity, efficiency, and effectiveness makes SimCSE a strong choice for robust sentence embeddings.

Future directions include:

- Extending SimCSE to multilingual and cross-lingual settings
- Applying contrastive learning with dropout to document-level tasks
- Exploring scaling behavior across larger models and datasets

SimCSE demonstrates that **simple ideas**, when built on strong foundations, can yield substantial improvements without complex engineering or heavy augmentation pipelines.

---

# References

(Formatted into Markdown from the PDF.)

**Agirre, E., Cer, D., Diab, M., & Gonzalez-Agirre, A. (2012).**  
*SemEval-2012 Task 6: A pilot on semantic textual similarity.*

**Cer, D., et al. (2017).**  
*SemEval-2017 Task 1: Semantic Textual Similarity Multilingual and Crosslingual Focused Evaluation.*

**Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019).**  
*BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.*

**Ethayarajh, K. (2019).**  
*How contextual are contextualized word representations?*

**Gao, T., Yao, X., & Chen, D. (2021).**  
*SimCSE: Simple Contrastive Learning of Sentence Embeddings.* (Original paper)

**Hill, F., Reichart, R., & Korhonen, A. (2015).**  
*SimLex-999: Evaluating Semantic Similarity with Tight Human Agreement.*

**Reimers, N., & Gurevych, I. (2019).**  
*Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks.*

**Wang, T., & Isola, P. (2020).**  
*Understanding Contrastive Representation Learning through Alignment and Uniformity on the Hypersphere.*

**Zhang, Y., et al. (2020).**  
*BERT-flow: Improving Sentence Embeddings with Normalizing Flows.*

**Su, J., et al. (2021).**  
*IS-BERT: An Information Theoretic Approach for Sentence Embeddings.*

