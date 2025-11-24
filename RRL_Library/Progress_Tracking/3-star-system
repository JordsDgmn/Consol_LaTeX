# To Three or Not to Three: Improving Human Computation Game Onboarding with a Three-Star System  
**Jacqueline Gaston** – Carnegie Mellon University – jgaston@andrew.cmu.edu  
**Seth Cooper** – Northeastern University – scooper@ccs.neu.edu  

---

# ABSTRACT
While many popular casual games use three-star systems, which give players up to three stars based on their performance in a level, this technique has seen limited application in human computation games (HCGs). This gives rise to the question of what impact, if any, a three-star system will have on the behavior of players in HCGs.

In this work, we examined the impact of a three-star system implemented in the protein folding HCG Foldit. We compared the basic game’s introductory levels with two versions using a three-star system, where players were rewarded with more stars for completing levels in fewer moves. In one version, players could continue playing levels for as many moves as they liked, and in the other, players were forced to reset the level if they used more moves than required to achieve at least one star on the level.

We observed that the three-star system encouraged players to use fewer moves, take more time per move, and replay completed levels more often. We did not observe an impact on retention. This indicates that three-star systems may be useful for re-enforcing concepts introduced by HCG levels, or as a flexible means to encourage desired behaviors.

**Author Keywords:** games; human computation; design; analytics  
**ACM Classification Keywords:** H.5.0 Information interfaces and presentation: General

---

# INTRODUCTION
Human computation games (HCGs) hold promise for solving a variety of challenging problems relevant to many fields of science. These range from designing RNA folds [13] to improving cropland coverage maps [24] to building 3D models of neurons [9] to software verification [16].

However, engaging and retaining participants in citizen science projects such as HCGs is difficult, with many participants leaving projects soon after starting [21, 15]. A critical part of any game is the onboarding process, often accomplished through a series of introductory levels that teach players the fundamental concepts of the game.

These levels, being the first thing that a user interacts with when playing, profoundly impact experience and lay the foundation for later levels. Improving the onboarding process is therefore critical to retaining players.

Three-star systems are used in many popular casual games (e.g., **Angry Birds**, **Candy Crush**, **Cut the Rope**, **DragonBox Algebra**). These systems reward players with up to three stars upon completing a level, with better performance yielding more stars.

Despite their popularity in entertainment games, little research exists examining three-star systems in HCGs. We hypothesized that adding such a system could encourage more thoughtful play during onboarding.

We carried out an experiment in the protein folding game **Foldit** to evaluate this.

---

# RELATED WORK
Different players respond to different reward types.

- **Bartle (1996)** categorized players into: Achievers, Killers, Socializers, Explorers. Three-star systems appeal most to *Achievers*.  
- **Yee (2006)** refined these motivations using survey data.  
- **Tondello et al. (2016)** identify Achievers as users motivated by completing tasks and overcoming challenges.

### Reward Systems in Games
Hallford & Hallford [8] categorized RPG rewards; Phillips et al. [18] expanded this for multiple genres.

In this study, the three-star system functions as a “**Reward of Glory**”—purely cosmetic, not affecting gameplay mechanics.

### Rewards in Human Computation Games
- von Ahn & Dabbish (ESP Game) → output-agreement rewards  
- TagATune (Law & von Ahn) → input-agreement  
- Siu et al. → competition rewards improved engagement  
- Allowing players to choose rewards increased task completion (Siu & Riedl)

Goh et al. [7] found that points and badges increased enjoyment.

### Online experimentation
Recent work uses online A/B tests to examine design decisions in educational or HCG contexts. This work adds a study of three-star systems.

---

# SYSTEM OVERVIEW
We implemented a three-star system in **Foldit** [6].

Foldit is a protein-folding HCG where players manipulate a 3D protein to reach lower-energy configurations.

### Introductory Levels
Foldit contains 31 introductory onboarding levels covering:
- basic concepts  
- tools  
- guided tutorial text  

Levels can be solved in **one to four moves** if done thoughtfully.

Making extra moves often makes solving harder, as ideal solutions are usually close to starting positions.

Thus, we rewarded **fewer moves**.

---

## Three-Star System Implementation
A screenshot is shown in **Figure 1** (gameplay UI with stars and moves gauge).

Rewards:

- Completing in ideal moves or fewer → **3 stars**  
- Completing in +1 to +2 moves → **2 stars**  
- Completing in ≥ +3 moves → **1 star**

### Forced Reset Variant
In the **3-STAR-R** condition:
- If players exceeded **ideal + 4 moves**, they were forced to **restart the level**.

This added a failure mode (similar to many casual games).

### UI Changes
(Shown in Figure 2)

- A **test tube gauge** depleted as moves were spent  
- Stars overlaid on the gauge, fading as the player lost the ability to earn them  
- Level-complete summary panel showing earned stars  
- Level-select screen showing best stars earned per level  

Players had no explicit tutorial about stars; they discovered the system themselves.

### Determining Ideal Move Count
Four Foldit developers played through all levels and chose the minimum number of moves required when using the intended tools.

When ambiguous, a slightly higher ideal number was chosen.  

10 out of 32 levels used a non-minimum ideal threshold.

---

# EXPERIMENT
We tested three conditions over one week (September 2016):

- **NO-STAR:** baseline game  
- **3-STAR:** three-star system, no forced reset  
- **3-STAR-R:** three-star system + forced reset  

Chat was disabled to prevent cross-condition confusion.

### Sample Size  
N = 626  
- 212 NO-STAR  
- 215 3-STAR  
- 199 3-STAR-R  

### Variables Collected
- **Extra Moves**  
- **Time per Move**  
- **Recompleted** (whether a player replayed any level)  
- **Levels** (unique levels completed)  
- **Total Time**  
- **Returned** (whether they returned after closing the game)

### Statistical Tests
- Kruskal-Wallis → Wilcoxon post-hoc (Bonferroni corrected)  
- Chi-square tests for categorical variables  
- Effect sizes: **r** and **φ**

### Table 1: Results Summary
(Exact table preserved:)

Variable | Omnibus | NO-STAR / 3-STAR | NO-STAR / 3-STAR-R | 3-STAR / 3-STAR-R  
---|---|---|---|---  
Extra Moves | H(2)=141.66, p<.001 | 2.69/1.6 | 2.69/0.67 | 1.6/0.67  
Time per Move (s) | H(2)=48.65, p<.001 | 14/16 | 14/20 | 16/20  
Recompleted (%) | χ²=22.00, p<.001 | 15.57/35.35 | 15.57/28.14 | 35.35/28.14  
Levels | H(2)=1.04, n.s. | 9/8 | 9/8 | 8/8  
Total Time (m) | H(2)=2.65, n.s. | 17.04/18.48 | 17.04/14.2 | 18.48/14.2  
Returned (%) | χ²=2.30, n.s. | 33.96/27.44 | 33.96/29.15 | 27.44/29.15  

Post-hoc comparisons shown in blue italics in the PDF; values preserved here as exact text.

---

# Results by Hypothesis

### **H1 supported:**  
Three-star systems caused players to:  
- complete levels with **fewer extra moves**  
- take **more time per move**

Forced reset further amplified this.

### **H2 supported:**  
Players in both 3-STAR conditions:  
- replayed levels **about twice as often**

3-STAR and 3-STAR-R did not differ significantly from each other in recompletion rate.

### **H3 not supported:**  
No difference between groups in:  
- retention  
- number of unique levels completed  
- total time spent  
- likelihood of returning

---

# CONCLUSION AND FUTURE WORK
- Three-star systems encouraged players to use fewer moves, think more carefully, and replay levels.  
- Adding a forced reset intensified careful play.  
- However, retention did **not** improve.

Therefore, three-star systems are effective for **encouraging desired behaviors**, but not necessarily for **long-term retention**.

Future directions:
- Test in less challenging games  
- Examine effect in educational settings  
- Study influence on correctness and other designer-desired behaviors  

---

# ACKNOWLEDGMENTS
Thanks to Robert Kleffner, Qi Wang, the Center for Game Science, and all Foldit players.  
Funding: NIH 1UH2CA203780, RosettaCommons, Amazon, NSF Grants 1541278 and 1629879.

---

# REFERENCES
(Full reference list preserved exactly.)

1. von Ahn & Dabbish, 2004  
2. Andersen et al., 2011  
3. Andersen et al., 2012  
4. Bartle, 1996  
5. Cooper et al., 2010a  
6. Cooper et al., 2010b  
7. Goh et al., 2015  
8. Hallford & Hallford, 2001  
9. Kim et al., 2014  
10. King (Candy Crush), 2012  
11. Law & von Ahn, 2009  
12. Leaver-Fay et al., 2011  
13. Lee et al., 2014  
14. Lomas et al., 2013  
15. Mao et al., 2013  
16. Moffitt et al., 2015  
17. Newell & Rosenbloom, 1981  
18. Phillips et al., 2013  
19. Rohl et al., 2004  
20. Rovio (Angry Birds), 2009  
21. Sauermann & Franzoni, 2015  
22. Siu & Riedl, 2016  
23. Siu et al., 2014  
24. Sturn et al., 2015  
25. Tondello et al., 2016  
26. DragonBox Algebra, 2012  
27. Yee, 2006  
28. Cut the Rope, 2010  

