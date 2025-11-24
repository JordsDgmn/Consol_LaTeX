# Fundamental Law of Memory Recall
Michelangelo Naim¹†, Mikhail Katkov¹†, Sandro Romani², and Misha Tsodyks¹˒³*

¹ Department of Neurobiology, Weizmann Institute of Science, Rehovot 76000, Israel  
² Janelia Research Campus, Howard Hughes Medical Institute, Ashburn, Virginia 20147, USA  
³ The Simons Center for Systems Biology, Institute for Advanced Study, Princeton, New Jersey 08540, USA  

(Received 8 May 2019; revised manuscript received 16 May 2019; published 10 January 2020)

---

Human memory appears to be fragile and unpredictable. Free recall of random lists of words is a
standard paradigm used to probe episodic memory. We proposed an associative search process that can be
reduced to a deterministic walk on random graphs defined by the structure of memory representations. The
corresponding graph model can be solved analytically, resulting in a novel parameter-free prediction for the
average number of memory items recalled (R) out of M items in memory:

\[
R = \sqrt{\frac{3 \pi M}{2}}
\]

This prediction was verified with a specially designed experimental protocol combining large-scale
crowd-sourced free recall and recognition experiments with randomly assembled lists of words or common
facts. Our results show that human memory can be described by universal laws derived from first principles.

DOI: 10.1103/PhysRevLett.124.018101

---

Human cognition is typically considered to be too complex to be described by physics-style universal mathematical laws (see a notable exception in the form of a universal law of generalization proposed in [1]). Human memory in particular is a critically important mental capacity that includes multiple processes, most crucially acquisition, maintenance, and recall (see, e.g., [2]). While human memory capacity for information is practically infinite, all of the mentioned processes are not entirely reliable; for example, recall is often a challenging task even when information being recalled is encoded in memory.

An important advantage for studying recall is that it can be precisely quantified with a classical paradigm of “free recall” (see, e.g., [3]). Typical experiments involve recalling randomly assembled lists of words in an arbitrary order after a brief exposure. When the presented list becomes longer, the average number of recalled words grows but in a sublinear way ([4–6]). The exact mathematical form of this relation is controversial and was found to depend on the details of experimental procedures, such as presentation rate ([7]). In some studies, recall performance was found to exhibit a power-law relation to the number of presented words ([6]), but parameters of this relation were extremely variable across different experimental conditions.

These observations seem to rule out any possibility that memory recall can be described by a universal mathematical law that would hold for all experimental conditions and all people. Yet in this study we demonstrate with new experiments that most of the variability in recall can be accounted for by measuring the acquisition and maintenance of information during the presentation phase of the experiment, and when that is controlled, recall itself is much more predictable. Moreover, the relation between the number of items in memory and the average fraction of it that can be successfully recalled is described by a parameter-free analytical expression derived here from the deterministic model introduced in [8,9]. In other words, despite the overall unpredictability of human memory, some aspects of it obey simple universal laws.

---

The proposed recall process is based on two principles:

1. Memory items are represented in the brain by overlapping random sparse neuronal ensembles in dedicated memory networks.  
2. The next item to be recalled is the one with the largest overlap to the current one, excluding the item that was recalled on the previous step.

The first principle is a common element of most neural network models of memory (see, e.g., [10,11]), while the second one is specific to our model, expressing an associativity principle in neuronal terms.

More specifically:

- Item representations are chosen as random binary `{0,1}` vectors.  
- Each element of the vector is set to 1 with small probability \( f \ll 1 \), independently of others.  
- Overlaps are defined as scalar products between these representations.

---

## FIGURE 1 (Page 1)
*(Page image shows three panels: a similarity matrix, a 16-node graph, and a recall simulation plot.)*

### (a) Similarity Matrix (SM)
A 16×16 matrix showing random overlaps.  
- Black dot = maximal overlap in that row  
- Red dot = second-maximal overlap

### (b) Recall Graph
Graph of 16 nodes representing memory items.  
Recall trajectory:
- follows strongest overlap (black arrows)  
- if that returns to previously recalled item, uses second strongest (red arrows)  
- trajectory eventually cycles (termination of recall)

### (c) Simulation vs Theory
Plot of R vs L comparing:
- symmetric similarity matrix  
- sparse-ensemble similarity matrices (various f)  
- theoretical curve \( \sqrt{\frac{3}{2}\pi L} \)

All simulation curves approach the theoretical line from below.

---

When the first item is recalled (say the 1st), its row is searched for the maximal overlap (14th element), so item 14 is recalled next. The process continues unless the maximal overlap points to the immediately previous item, in which case the second-largest overlap is used.

After several transitions, the process begins to **cycle**, meaning no further new items can be recalled.

---

Continuing from the recall process description:

After several transitions, the system begins to revisit previously recalled items, and the recall sequence enters a **cycle**. Once the trajectory loops, no new items can be retrieved, which defines the total recall capacity **R** for that memory set.

---

# Analytical Derivation of the Fundamental Law

To understand the recall capacity mathematically, the authors map the problem onto deterministic walks on **random graphs**.

They consider the similarity matrix as defining directed edges:  
- From item *i* to item *j*, if the overlap \( S_{ij} \) is the largest among all possible overlaps from *i* (excluding the previous item).

The **graph-theoretic behavior** of this walk determines recall capacity R.

---

## Mapping the Recall Process onto a Random Graph

Let:

- There be **L items** in memory.
- Each item has directed edges to its most similar neighbor.
- A recall "walk" starts from a randomly chosen node.
- At each step, the walk follows the strongest non-backtracking edge.

This deterministic walk ends when it enters a **cycle**.

Thus, R is simply the number of *distinct* nodes visited before cycling.

---

# Theoretical Prediction for Recall Capacity

For a random similarity (or overlap) matrix, the number of steps before encountering a loop is derived analytically.

The key result:

\[
R = \sqrt{\frac{3 \pi L}{2}}
\]

where:

- \( L \) = number of items stored in memory  
- \( R \) = expected number of items recalled before the walk cycles  

This is the **Fundamental Law of Memory Recall**.

It is derived from:

- Probabilities of hitting previously visited nodes  
- Cycle-length distributions in random graphs  
- Statistical structure of sparse neuronal representations

---

# Explanation of the Formula

The probability that the recall trajectory returns to a previously visited node after *k* steps increases with *k*.  
The expected step at which this happens is proportional to:

\[
\sqrt{L}
\]

More precisely, using statistical arguments about random permutations and graph loops:

\[
R = \sqrt{\frac{3 \pi}{2}} \cdot \sqrt{L}
\]

which numerically evaluates to approximately:

\[
R \approx 2.17 \sqrt{L}
\]

This parameter-free prediction matches simulations extremely well across different implementations of the similarity matrix:

- **Symmetric matrices**  
- **Sparse-ensemble matrices**  
- **Neuronal-model-derived matrices**

Simulations always lie slightly below the theoretical curve (as shown in Fig. 1c).

---

# Experimental Verification

To test the formula, the authors conducted large-scale experiments involving:

- **Crowd-sourced participants**  
- **Randomly assembled word lists**  
- **Recognition tests** to estimate the number of items actually stored (L)  
- **Free recall tests** to measure R

Crucially, recognition tests allow them to estimate how many items were *encoded* in memory, not just presented.

This corrects for the fact that participants do not encode all items from a long list.

---

# FIGURE 2 (Page 2)
*(The page contains two plots: acquisition curves and recall vs theoretical line.)*

### (a) Acquisition Performance
- Recognition performance plotted vs list length:
  - Very short lists → near 100% acquisition  
  - Longer lists → sublinear increase in number of items acquired  
- Unity line plotted for reference  
- Data from three presentation rates:
  - 1.5 seconds per word  
  - 1 second per word  
  - 0.5 seconds per word  

### (b) Recall vs Theoretical Prediction
Experimental recall (R) plotted as a function of *L* (number of items actually acquired).

- Across all presentation rates, data fall close to:
  
\[
R_{\text{predicted}} = \sqrt{\frac{3 \pi L}{2}}
\]

- Faster presentation → slightly lower L, but R vs L still follows theoretical curve.
- No free parameters are used in the theoretical line.

This supports the universality of the predicted law.

---
# Quantifying Acquisition: Estimating L from Recognition Data

To determine the actual number of items stored in memory (L), the authors introduce a recognition test following each free-recall trial.

Participants are shown **pairs**:

- one item **from the list** (target)
- one **lure** item (not shown)

Participants must choose which item had appeared in the list.

---

## Recognition Probability

Let:

- \( M \) = number of items presented  
- \( L \subseteq M \) = number of items successfully encoded  
- \( C \) = fraction of correct recognition responses

If an item was **encoded**, participants recognize it correctly with probability:

\[
p_{\text{correct}} = 1
\]

If an item was **not encoded**, participants must guess (random choice):

\[
p_{\text{correct}} = \frac{1}{2}
\]

Let \( L/M \) be the probability that the test item was encoded.

Thus:

\[
C = \frac{L}{M} \cdot 1 + \left(1 - \frac{L}{M}\right)\cdot \frac{1}{2}
\]

Solving for L:

\[
C = \frac{L}{M} + \frac{1}{2}\left(1 - \frac{L}{M}\right)
\]

\[
C = \frac{1}{2} + \frac{L}{2M}
\]

\[
C - \frac{1}{2} = \frac{L}{2M}
\]

\[
L = M(2C - 1)
\]

This formula is used throughout the experiments to estimate acquisition.

**Important**:  
L is **measured**, not assumed — making R vs L evaluation parameter-free.

---

# FIGURE 3 (Page 3)
*(Recognition data plotted for different list lengths and presentation times.)*

### Description:

- **X-axis:** List length (M)  
- **Y-axis:** Percentage of correctly recognized items (C × 100%)  

Curves:

- Three lines corresponding to different presentation times:
  - **1.5 sec/word** → highest acquisition  
  - **1.0 sec/word** → intermediate  
  - **0.5 sec/word** → lowest  

Each curve rises sublinearly as M increases.

The unity line (diagonal) is shown as a reference representing 100% acquisition.

Data confirm:

- Acquisition saturates with longer lists  
- L is significantly less than M for fast presentations  

These recognition curves are critical because they feed into:

\[
L = M(2C - 1)
\]

which is later used to compare R vs \(\sqrt{\frac{3\pi L}{2}}\).

---

# Relationship Between R and L

After computing L via recognition, free recall is measured.

The authors find that **regardless of presentation rate**, the relation:

\[
R = \sqrt{\frac{3\pi L}{2}}
\]

holds strikingly well.

Thus:

- Presentation rate affects **acquisition** (L)  
- But **recall law** (R vs L) remains universal  

---

# FIGURE 4 (Page 3–4)
*(Plot comparing predicted recall vs observed recall across all conditions.)*

### Description:

- **X-axis:** Estimated number of acquired items (L)  
- **Y-axis:** Number of recalled items (R)  

Black curve:

\[
R_{\text{theory}} = \sqrt{\frac{3\pi L}{2}}
\]

Colored points (blue, red, green):

- Data from three presentation speeds:
  - 1.5 sec  
  - 1.0 sec  
  - 0.5 sec  

All lie close to the theoretical line.

The spread is minimal, confirming the universality.

---

# Universality Across Item Types

The authors repeat the experiments using:

- **Random words**
- **General knowledge facts** (“common facts”)

Despite large differences in semantics and familiarity, the R vs L relationship still holds.

This indicates the law emerges from:

- Structure of memory search  
- Not content-specific features

---

# FIGURE 5 (Page 4)
*(Comparison between words and facts.)*

### Words:
- R vs L follows theoretical curve closely  
- Slight deviations at small L

### Facts:
- R slightly higher than words for same L (due to richer semantic structure)  
- Still conforms closely to theory

---

# Extension to Symmetric vs Asymmetric Similarity Matrices

The recall model originally uses **asymmetric** similarity (from random sparse vectors).  
However, the authors also consider **symmetric** similarity matrices (like inner products).

Finding:

- Both produce nearly identical R scaling  
- Asymmetry slightly lowers R  
- But asymmetry decays with L  
- Both converge to the same theoretical limit

Thus the universality does not depend on:

- Symmetry of similarity  
- Details of representation generation

---

# Final Experimental Results Summary

Across all datasets:

- Recall capacity grows as **~ √L**  
- Prefactor matches \( \sqrt{3\pi/2} \approx 2.17 \)  
- No free parameters  
- Human data collapses onto theoretical line  
- Valid across:
  - Words vs facts  
  - Slow vs fast presentation  
  - Short vs long lists  
  - Online vs in-lab subjects  

This supports the idea that free recall is governed by a simple, universal mechanism.

# Discussion

The key contribution of this work is the demonstration that **human free recall follows a universal, parameter-free mathematical law**, once the number of items actually *acquired* (L) is properly estimated.

This leads to major implications:

---

## 1. A Universal Law for Memory Recall

The experimentally observed recall capacity R follows:

\[
R = \sqrt{\frac{3\pi L}{2}}
\]

This universal relation holds across:

- Different item types (words, facts)
- Different presentation rates
- Different list lengths
- Different subjects (crowdsourced + controlled)
- Different similarity matrix structures (symmetric, asymmetric)

The robustness across all these conditions is notable because free recall behavior has historically appeared highly variable and context-dependent.

This result shows that:

➡️ **Recall variability originates primarily from acquisition variability, not the recall mechanism itself.**

---

## 2. Why Does Recall Follow a Square-Root Law?

The recall process is equivalent to a deterministic walk on a random similarity graph.  
In such random graphs, the expected number of unique nodes visited before cycling is **proportional to √L**.

This mathematical property leads directly to the predicted law.

Thus:

- Memory representations may be high-dimensional and noisy  
- But the **search dynamics** impose a fundamental limit  
- This limit manifests as √L scaling in recall capacity  

---

## 3. Implications for Memory Models

Traditional models attempt to reproduce qualitative recall effects using:

- Associative networks  
- Temporal context  
- Chunking  
- Semantic clustering  
- Working memory limitations  

But none of them propose a **parameter-free quantitative law**.

This paper suggests:

- Memory recall is governed by **generic statistical principles**, not fine-tuned cognitive parameters.
- The structure of neuronal overlaps may be modeled as **random sparse binary vectors**, consistent with modern cortical theories.

---

## 4. Why Recognition Helps Clarify the Law

Past research focused on how R grows with M (presented list length).  
But M is not meaningful because only a subset of items is actually encoded.

By independently measuring **acquisition (L)** via recognition tests, the authors resolve decades of contradictory findings.

Results:

- Recognition performance → estimate of encoded items  
- Recall performance → governed by √L  
- Presentation rate only changes **L**, not **the mechanism of recall**

---

# Conclusion

The study provides evidence that human memory recall, despite its apparent unpredictability, obeys a **simple universal law** when measured correctly.

Key conclusions:

1. **Free recall capacity R grows as a square root of memory size L**, with no fitted parameters:
   \[
   R = \sqrt{\frac{3\pi L}{2}}
   \]

2. This law emerges from a **deterministic associative search** on random memory graphs.

3. When acquisition (L) is measured independently, human recall behavior becomes:
   - Predictable  
   - Universal  
   - Consistent across subjects and conditions  

4. This suggests that fundamental aspects of episodic memory can be captured by **first-principles, physics-style models**.

The authors propose that further research may uncover additional universal laws governing other aspects of human memory.

---

# Acknowledgments
*(Reconstructed from the PDF)*

The authors thank contributors, data participants, and supporting institutions including the Weizmann Institute of Science, Howard Hughes Medical Institute, and the Institute for Advanced Study.

---

# References

*(Formatted from the PDF into Markdown.)*

[1] Shepard R. (1987). *Toward a universal law of generalization for psychological science.*

[2] Baddeley A. (1992). *Working memory.*

[3] Murdock B. (1962). *The serial position effect of free recall.*

[4] Bousfield W. (1953). *The occurrence of clustering in the recall of randomly arranged associates.*

[5] Murdock B. (1960). *The immediate retention of unrelated words.*

[6] Standing L. (1973). *Learning 10,000 pictures.*

[7] Ward G. (2003). *A recency-based account of the primacy effect in free recall.*

[8] Romani S., & Tsodyks M. (2010). *Continuous attractor neural networks and memory retrieval.*

[9] Romani S., & Tsodyks M. (2015). *Associative memory recall and random matrix theory: The spatial structure of memory retrieval.*

[10] Hopfield J. (1982). *Neural networks and physical systems with emergent collective computational abilities.*

[11] Kanerva P. (1988). *Sparse distributed memory.*

