SimCSE: Simple Contrastive Learning of Sentence Embeddings
 Tianyu Gao
 Xingcheng Yao
 Danqi Chen
 Department of Computer Science, Princeton University
 Institute for Interdisciplinary Information Sciences, Tsinghua University
 {tianyug,danqic}@cs.princeton.edu
 yxc18@mails.tsinghua.edu.cn
 Abstract
 arXiv:2104.08821v4  [cs.CL]  18 May 2022
 This paper presents SimCSE, a simple con
trastive learning framework that greatly ad
vances state-of-the-art sentence embeddings.
 We first describe an unsupervised approach,
 which takes an input sentence and predicts
 itself in a contrastive objective, with only
 standard dropout used as noise. This simple
 method works surprisingly well, performing
 on par with previous supervised counterparts.
 Wefind that dropout acts as minimal data aug
mentation, and removing it leads to a repre
sentation collapse. Then, we propose a super
vised approach, which incorporates annotated
 pairs from natural language inference datasets
 into our contrastive learning framework by us
ing “entailment” pairs as positives and “con
tradiction” pairs as hard negatives. We evalu
ate SimCSE on standard semantic textual simi
larity (STS) tasks, and our unsupervised and
 supervised models using BERTbase achieve
 an average of 76.3% and 81.6% Spearman’s
 correlation respectively, a 4.2% and 2.2%
 improvement compared to the previous best
 results.
 We also show—both theoretically
 and empirically—that the contrastive learning
 objective regularizes pre-trained embeddings’
 anisotropic space to be more uniform, and it
 better aligns positive pairs when supervised
 signals are available.1
 1 Introduction
 Learning universal sentence embeddings is a fun
damental problem in natural language process
ing and has been studied extensively in the litera
ture (Kiros et al., 2015; Hill et al., 2016; Conneau
 et al., 2017; Logeswaran and Lee, 2018; Cer et al.,
 2018; Reimers and Gurevych, 2019, inter alia).
 In this work, we advance state-of-the-art sentence
 *The first two authors contributed equally (listed in alpha
betical order). This work was done when Xingcheng visited
 the Princeton NLP group remotely.
 1Our code and pre-trained models are publicly available at
 https://github.com/princeton-nlp/SimCSE.
 embedding methods and demonstrate that a con
trastive objective can be extremely effective when
 coupled with pre-trained language models such as
 BERT(Devlin et al., 2019) or RoBERTa (Liu et al.,
 2019). We present SimCSE, a simple contrastive
 sentence embedding framework, which can pro
duce superior sentence embeddings, from either
 unlabeled or labeled data.
 Our unsupervised SimCSE simply predicts the
 input sentence itself with only dropout (Srivastava
 et al., 2014) used as noise (Figure 1(a)). In other
 words, we pass the same sentence to the pre-trained
 encoder twice: by applying the standard dropout
 twice, we can obtain two different embeddings as
 “positive pairs”. Then we take other sentences in
 the same mini-batch as “negatives”, and the model
 predicts the positive one among the negatives. Al
though it may appear strikingly simple, this ap
proach outperforms training objectives such as pre
dicting next sentences (Logeswaran and Lee, 2018)
 and discrete data augmentation (e.g., word dele
tion and replacement) by a large margin, and even
 matches previous supervised methods. Through
 careful analysis, we find that dropout acts as mini
mal “data augmentation” of hidden representations
 while removing it leads to a representation collapse.
 Our supervised SimCSE builds upon the recent
 success of using natural language inference (NLI)
 datasets for sentence embeddings (Conneau et al.,
 2017; Reimers and Gurevych, 2019) and incorpo
rates annotated sentence pairs in contrastive learn
ing (Figure 1(b)). Unlike previous work that casts
 it as a 3-way classification task (entailment, neu
tral, and contradiction), we leverage the fact that
 entailment pairs can be naturally used as positive
 instances. We also find that adding correspond
ing contradiction pairs as hard negatives further
 improves performance. This simple use of NLI
 datasets achieves a substantial improvement com
pared to prior methods using the same datasets.
 We also compare to other labeled sentence-pair
(a) Unsupervised SimCSE
 (b) Supervised SimCSE
 Different hidden dropout masks
 in two forward passes
 Two dogs are running.
 A man surfing on the sea.
 A kid is on a skateboard.
 E
 Two dogs
 are running.
 A man surfing
 on the sea.
 E Encoder
 Positive instance
 Negative instance
 A kid is on a 
skateboard.
 E
 E
 There are animals outdoors.
 label=entailment
 The pets are sitting on a couch.
 The pets are sitting on a couch.
 label=contradiction
 There is a man.
 label=entailment
 The man wears a business suit.
 label=contradiction
 A kid is skateboarding.
 label=entailment
 A kit is inside the house.
 label=contradiction
 Figure 1: (a) Unsupervised SimCSE predicts the input sentence itself from in-batch negatives, with different hidden
 dropout masks applied. (b) Supervised SimCSE leverages the NLI datasets and takes the entailment (premise
hypothesis) pairs as positives, and contradiction pairs as well as other in-batch instances as negatives.
 datasets and find that NLI datasets are especially
 effective for learning sentence embeddings.
 To better understand the strong performance of
 SimCSE, we borrow the analysis tool from Wang
 and Isola (2020), which takes alignment between
 semantically-related positive pairs and uniformity
 of the whole representation space to measure the
 quality of learned embeddings. Through empiri
cal analysis, we find that our unsupervised Sim
CSE essentially improves uniformity while avoid
ing degenerated alignment via dropout noise, thus
 improving the expressiveness of the representa
tions. The same analysis shows that the NLI train
ing signal can further improve alignment between
 positive pairs and produce better sentence embed
dings. We also draw a connection to the recent find
ings that pre-trained word embeddings suffer from
 anisotropy (Ethayarajh, 2019; Li et al., 2020) and
 prove that—through a spectrum perspective—the
 2 Background: Contrastive Learning
 Contrastive learning aims to learn effective repre
sentation by pulling semantically close neighbors
 together and pushing apart non-neighbors (Hadsell
 et al., 2006). It assumes a set of paired examples
 D= (xi x+
 i )m
 i=1, where xi and x+
 i are semanti
cally related. We follow the contrastive framework
 in Chen et al. (2020) and take a cross-entropy ob
jective with in-batch negatives (Chen et al., 2017;
 Henderson et al., 2017): let hi and h+
 i denote the
 representations of xi and x+
 i , the training objective
 for (xi x+
 i ) with a mini-batch of N pairs is:
 i = log esim(hih+
 i )
 N
 j=1 esim(hih+
 j )
 where 
(1)
 is a temperature hyperparameter and
 sim(h1h2) is the cosine similarity h1 h2
 h1 h2
 . In
 contrastive learning objective “flattens” the singu
lar value distribution of the sentence embedding
 space, hence improving uniformity.
 Weconduct a comprehensive evaluation of Sim
CSE on seven standard semantic textual similarity
 (STS) tasks (Agirre et al., 2012, 2013, 2014, 2015,
 2016; Cer et al., 2017; Marelli et al., 2014) and
 seven transfer tasks (Conneau and Kiela, 2018).
 Onthe STS tasks, our unsupervised and supervised
 models achieve a 76.3% and 81.6% averaged Spear
man’s correlation respectively using BERTbase, a
 4.2% and 2.2% improvement compared to previous
 best results. We also achieve competitive perfor
mance on the transfer tasks. Finally, we identify
 an incoherent evaluation issue in the literature and
 consolidate the results of different settings for fu
ture work in evaluation of sentence embeddings.
 this work, we encode input sentences using a
 pre-trained language model such as BERT (De
vlin et al., 2019) or RoBERTa (Liu et al., 2019):
 h = f(x), and then fine-tune all the parameters
 using the contrastive learning objective (Eq. 1).
 Positive instances. One critical question in con
trastive learning is how to construct (xi x+
 i ) pairs.
 In visual representations, an effective solution is to
 take two randomtransformations of the same image
 (e.g., cropping, flipping, distortion and rotation) as
 xi and x+
 i (Dosovitskiy et al., 2014). A similar
 approach has been recently adopted in language
 representations (Wu et al., 2020; Meng et al., 2021)
 by applying augmentation techniques such as word
 deletion, reordering, and substitution. However,
 data augmentation in NLP is inherently difficult
 because of its discrete nature. As we will see in §3,
simplyusingstandarddropoutonintermediaterep
resentationsoutperformsthesediscreteoperators.
 InNLP,asimilarcontrastivelearningobjective
 hasbeenexploredindifferentcontexts(Henderson
 etal.,2017;Gillicketal.,2019;Karpukhinetal.,
 2020). Inthesecases,(xi x+
 i )arecollectedfrom
 superviseddatasetssuchasquestion-passagepairs.
 Becauseofthedistinctnatureofxiandx+
 i ,these
 approachesalwaysuseadual-encoderframework,
 i.e.,usingtwoindependentencodersf1
 andf2
 for
 xiandx+
 i .Forsentenceembeddings,Logeswaran
 andLee(2018)alsousecontrastivelearningwith
 adual-encoderapproach,byformingcurrentsen
tenceandnextsentenceas(xi x+
 i ).
 Alignmentanduniformity.Recently,Wangand
 Isola(2020)identifytwokeypropertiesrelatedto
 contrastivelearning—alignmentanduniformity—
 andproposetousethemtomeasurethequalityof
 representations. Givenadistributionofpositive
 pairsppos,alignmentcalculatesexpecteddistance
 betweenembeddingsof thepairedinstances(as
sumingrepresentationsarealreadynormalized):
 align E
 (xx+) ppos
 f(x) f(x+) 2 (2)
 Ontheotherhand,uniformitymeasureshowwell
 theembeddingsareuniformlydistributed:
 uniform log E
 xyiidpdata
 e 2 f(x) f(y) 2 (3)
 wherepdatadenotesthedatadistribution. These
 twometricsarewell alignedwiththeobjective
 ofcontrastivelearning:positiveinstancesshould
 staycloseandembeddingsforrandominstances
 shouldscatteronthehypersphere. Inthefollowing
 sections,wewillalsousethetwometricstojustify
 theinnerworkingsofourapproaches.
 3 UnsupervisedSimCSE
 The ideaofunsupervisedSimCSEisextremely
 simple:wetakeacollectionofsentences xi m
 i=1
 andusex+
 i =xi.Thekeyingredienttogetthisto
 workwithidenticalpositivepairsisthroughtheuse
 ofindependentlysampleddropoutmasksforxiand
 x+
 i . InstandardtrainingofTransformers(Vaswani
 etal.,2017), therearedropoutmasksplacedon
 fully-connectedlayersaswellasattentionprobabil
ities(defaultp=01).Wedenotehz
 i =f(xi z)
 wherezisarandommaskfordropout.Wesimply
 feedthesameinput totheencodertwiceandget
 Dataaugmentation STS-B
 None(unsup.SimCSE) 82.5
 Crop 10% 20% 30%
 77.8 71.4 63.6
 Worddeletion 10% 20% 30%
 75.9 72.2 68.2
 Deleteoneword 75.9
 w/odropout 74.2
 Synonymreplacement 77.4
 MLM15% 62.2
 Table1:ComparisonofdataaugmentationsonSTS-B
 development set (Spearman’scorrelation). Cropk%:
 keep100-k%of thelength;worddeletionk%: delete
 k%words; Synonymreplacement: usenlpaug(Ma,
 2019)torandomlyreplaceonewordwithitssynonym;
 MLMk%:useBERTbasetoreplacek%ofwords.
 Trainingobjective f (f1
 f2
 )
 Nextsentence 67.1 68.9
 Next3sentences 67.4 68.8
 Deleteoneword 75.9 73.1
 UnsupervisedSimCSE 82.5 80.7
 Table2: Comparisonofdifferentunsupervisedobjec
tives(STS-Bdevelopmentset,Spearman’scorrelation).
 Thetwocolumnsdenotewhetherweuseoneencoder
 or twoindependent encoders. Next3sentences: ran
domlysampleonefromthenext3sentences. Delete
 oneword:deleteonewordrandomly(seeTable1).
 twoembeddingswithdifferentdropoutmasksz z,
 andthetrainingobjectiveofSimCSEbecomes:
 i= log esim(hzi
 i hzi
 i )
 N
 j=1esim(hzi
 i hzj
 j )
 (4)
 foramini-batchofNsentences.Notethatzisjust
 thestandarddropoutmaskinTransformersandwe
 donotaddanyadditionaldropout.
 Dropoutnoiseasdataaugmentation.Weview
 itasaminimal formofdataaugmentation: the
 positivepairtakesexactlythesamesentence,and
 their embeddingsonlydiffer indropoutmasks.
 Wecompare thisapproachtoother trainingob
jectivesontheSTS-Bdevelopmentset(Ceretal.,
 2017)2.Table1comparesourapproachtocommon
 dataaugmentationtechniquessuchascrop,word
 deletionandreplacement,whichcanbeviewedas
 2We randomly sample 106 sentences fromEnglish
 Wikipediaandfine-tuneBERTbasewithlearningrate=3e-5,
 N=64. Inallourexperiments,noSTStrainingsetsareused.
0.400
 p
 0.0
 0.01
 0.05
 STS-B 71.1 72.6 81.1
 0.1
 82.5
 p
 0.15
 0.2
 0.5
 STS-B 81.4 80.5 71.0
 Fixed 0.1
 43.6
 Table 3: Effects of different dropout probabilities p
 on the STS-Bdevelopment set (Spearman’s correlation,
 BERTbase). Fixed 0.1: default 0.1 dropout rate but ap
ply the same dropout mask on both xi and x+
 i .
 h = f(g(x) z) and g is a (random) discrete op
erator on x. We note that even deleting one word
 would hurt performance and none of the discrete
 augmentations outperforms dropout noise.
 We also compare this self-prediction training
 objective to the next-sentence objective used in Lo
geswaran and Lee(2018), taking either one encoder
 or two independent encoders. As shown in Table 2,
 we find that SimCSE performs much better than
 the next-sentence objectives (82.5 vs 67.4 on STS
B) and using one encoder instead of two makes a
 significant difference in our approach.
 Why does it work? To further understand the
 role of dropout noise in unsupervised SimCSE, we
 try out different dropout rates in Table 3 and ob
serve that all the variants underperform the default
 dropout probability p = 01 from Transformers.
 Wefind two extreme cases particularly interesting:
 “no dropout” (p = 0) and “fixed 0.1” (using default
 dropout p = 01 but the same dropout masks for
 the pair). In both cases, the resulting embeddings
 for the pair are exactly the same, and it leads to
 a dramatic performance degradation. We take the
 checkpoints of these models every 10 steps during
 training and visualize the alignment and uniformity
 metrics3 in Figure 2, along with a simple data aug
mentation model “delete one word”. As clearly
 shown, starting from pre-trained checkpoints, all
 models greatly improve uniformity. However, the
 alignment of the two special variants also degrades
 drastically, while our unsupervised SimCSE keeps
 a steady alignment, thanks to the use of dropout
 noise. It also demonstrates that starting from a pre
trained checkpoint is crucial, for it provides good
 initial alignment. At last, “delete one word” im
proves the alignment yet achieves a smaller gain
 on the uniformity metric, and eventually underper
forms unsupervised SimCSE.
 3We take STS-B pairs with a score higher than 4 as ppos
 and all STS-B sentences as pdata.
 Fixed 0.1 
Fixed 0.1
 0.375
 0.350
 0.325
 align
 Alignment
 0.300
 0.275
 1o dUoSout
 Delete one woUd
 No dropout
 Delete one word
 Unsup. SimCSE 8nsuS. 6imC6E
 Training direction
 0.250
 0.225
 0.200
 −2.6
 −2.4
 −2.2
 −2.0
 8nifoUmity
 uniform
 −1.8
 −1.6
 Figure 2: align-uniform plot for unsupervised SimCSE,
 “no dropout”, “fixed 0.1”, and “delete one word”. We
 visualize checkpoints every 10 training steps and the
 arrows indicate the training direction. For both align
 and uniform, lower numbers are better.
 4 Supervised SimCSE
 We have demonstrated that adding dropout noise
 is able to keep a good alignment for positive pairs
 (xx+) ppos. In this section, we study whether
 we can leverage supervised datasets to provide
 better training signals for improving alignment of
 our approach. Prior work (Conneau et al., 2017;
 Reimers and Gurevych, 2019) has demonstrated
 that supervised natural language inference (NLI)
 datasets (Bowman et al., 2015; Williams et al.,
 2018) are effective for learning sentence embed
dings, by predicting whether the relationship be
tween two sentences is entailment, neutral or con
tradiction. In our contrastive learning framework,
 we instead directly take (xi x+
 i ) pairs from super
vised datasets and use them to optimize Eq. 1.
 Choices of labeled data. We first explore which
 supervised datasets are especially suitable for con
structing positive pairs (xi x+
 i ). We experiment
 with a number of datasets with sentence-pair ex
amples, including 1) QQP4: Quora question pairs;
 2) Flickr30k (Young et al., 2014): each image is
 annotated with 5 human-written captions and we
 consider any two captions of the same image as a
 positive pair; 3) ParaNMT (Wieting and Gimpel,
 2018): a large-scale back-translation paraphrase
 dataset5; and finally 4) NLI datasets: SNLI (Bow
man et al., 2015) and MNLI (Williams et al., 2018).
 Wetrain the contrastive learning model (Eq. 1)
 with different datasets and compare the results in
 4https://www.quora.com/q/quoradata/
 5ParaNMT is automatically constructed by machine trans
lation systems. Strictly speaking, we should not call it “super
vised”. It underperforms our unsupervised SimCSE though.
Table 4. For a fair comparison, we also run exper
Dataset
 sample
 full
 iments with the same # of training pairs. Among
 all the options, using entailment pairs from the
 NLI (SNLI + MNLI) datasets performs the best.
 We think this is reasonable, as the NLI datasets
 consist of high-quality and crowd-sourced pairs.
 Also, human annotators are expected to write the
 hypotheses manually based on the premises and
 two sentences tend to have less lexical overlap.
 For instance, we find that the lexical overlap (F1
 measured between two bags of words) for the en
tailment pairs (SNLI + MNLI) is 39%, while they
 are 60% and 55% for QQP and ParaNMT.
 Contradiction as hard negatives. Finally, we fur
ther take the advantage of the NLI datasets by us
ing its contradiction pairs as hard negatives6. In
 NLI datasets, given one premise, annotators are re
quired to manually write one sentence that is abso
lutely true (entailment), one that might be true (neu
tral), and one that is definitely false (contradiction).
 Therefore, for each premise and its entailment hy
pothesis, there is an accompanying contradiction
 hypothesis7 (see Figure 1 for an example).
 Formally, we extend (xi x+
 i ) to (xi x+
 i xi ),
 where xi is the premise, x+
 i and xi are entailment
 and contradiction hypotheses. The training objec
tive i is then defined by (N is mini-batch size):
 log
 esim(hih+
 i )
 N
 j=1 esim(hih+
 j ) + esim(hihj )
 (5)
 As shown in Table 4, adding hard negatives can
 further improve performance (84.9 
86.2) and
 this is our final supervised SimCSE. We also tried
 to add the ANLI dataset (Nie et al., 2020) or com
bine it with our unsupervised SimCSE approach,
 but didn’t find a meaningful improvement. We also
 considered a dual encoder framework in supervised
 SimCSE and it hurt performance (86.2 
5 Connection to Anisotropy
 84.2).
 Recent work identifies an anisotropy problem in
 language representations (Ethayarajh, 2019; Li
 et al., 2020), i.e., the learned embeddings occupy a
 narrow cone in the vector space, which severely
 limits their expressiveness. Gao et al. (2019)
 6We also experimented with adding neutral hypotheses as
 hard negatives. See Section 6.3 for more discussion.
 7In fact, one premise can have multiple contradiction hy
potheses. In our implementation, we only sample one as the
 hard negative and we did not find a difference by using more.
 Unsup. SimCSE (1m)-
 82.5
 QQP(134k)
 Flickr30k (318k)
 ParaNMT (5m)
 SNLI+MNLI
 entailment (314k)
 neutral (314k)8
 contradiction (314k)
 all (942k)
 81.8
 81.5
 79.7
 84.1
 82.6
 77.5
 81.7
 81.8
 81.4
 78.7
 84.9
 82.9
 77.6
 81.9
 SNLI+MNLI
 entailment + hard neg.
 + ANLI(52k)--
 86.2
 85.0
 Table 4: Comparisons of different supervised datasets
 as positive pairs. Results are Spearman’s correlations
 on the STS-B development set using BERTbase (we
 use the same hyperparameters as the final SimCSE
 model). Numbers in brackets denote the # of pairs.
 Sample: subsampling 134k positive pairs for a fair com
parison among datasets; full: using the full dataset. In
 the last block, we use entailment pairs as positives and
 contradiction pairs as hard negatives (our final model).
 demonstrate that language models trained with tied
 input/output embeddings lead to anisotropic word
 embeddings, and this is further observed by Etha
yarajh (2019) in pre-trained contextual representa
tions. Wang et al. (2020) show that singular values
 of the word embedding matrix in a language model
 decay drastically: except for a few dominating sin
gular values, all others are close to zero.
 A simple way to alleviate the problem is post
processing, either to eliminate the dominant prin
cipal components (Arora et al., 2017; Mu and
 Viswanath, 2018), or to map embeddings to an
 isotropic distribution (Li et al., 2020; Su et al.,
 2021). Another common solution is to add reg
ularization during training (Gao et al., 2019; Wang
 et al., 2020). In this work, we show that—both
 theoretically and empirically—the contrastive ob
jective can also alleviate the anisotropy problem.
 Theanisotropy problem is naturally connected to
 uniformity (Wang and Isola, 2020), both highlight
ing that embeddings should be evenly distributed
 in the space. Intuitively, optimizing the contrastive
 learning objective can improve uniformity (or ease
 the anisotropy problem), as the objective pushes
 negative instances apart. Here, we take a singular
 spectrum perspective—which is a common practice
 8Though our final model only takes entailment pairs as
 positive instances, here we also try taking neutral and contra
diction pairs from the NLI datasets as positive pairs.
in analyzing word embeddings (Mu and Viswanath,
 also optimizes for aligning positive pairs by the
 2018; Gao et al., 2019; Wang et al., 2020), and
 show that the contrastive objective can “flatten” the
 singular value distribution of sentence embeddings
 and make the representations more isotropic.
 Following Wang and Isola (2020), the asymp
totics of the contrastive learning objective (Eq. 1)
 can be expressed by the following equation when
 the number of negative instances approaches infin
ity (assuming f(x) is normalized):
 1
 E
 (xx+) ppos
 f(x) f(x+)
 + E x pdata
 log E
 x pdata
 ef(x) f(x )
 (6)
 where the first term keeps positive instances similar
 and the second pushes negative pairs apart. When
 pdata is uniform over finite samples xi m
 i=1, with
 hi = f(xi), we can derive the following formula
 from the second term with Jensen’s inequality:
 E
 x pdata
 log E
 x pdata
 =1
 m 
m
 i=1 
log 1
 m 
m
 j=1
 1
 m2
 m
 i=1
 m
 j=1
 hi hj
 ef(x) f(x )
 ehi hj
 (7)
 Let W be the sentence embedding matrix corre
sponding to xi m
 i=1, i.e., the i-th row of W is
 hi. Optimizing the second term in Eq. 6 essen
tially minimizes an upper bound of the summation
 of all elements in WW, i.e., Sum(WW) =
 m
 i=1
 m
 j=1 hi hj.
 Since we normalize hi, all elements on the di
agonal of WW are 1 and then tr(WW) (the
 sum of all eigenvalues) is a constant. According
 to Merikoski (1984), if all elements in WW are
 positive, which is the case in most times accord
ing to Figure G.1, then Sum(WW) is an upper
 bound for the largest eigenvalue of WW. When
 minimizing the second term in Eq. 6, we reduce
 the top eigenvalue of WW and inherently “flat
ten” the singular spectrum of the embedding space.
 Therefore, contrastive learning is expected to alle
viate the representation degeneration problem and
 improve uniformity of sentence embeddings.
 Compared to post-processing methods in Li et al.
 (2020); Su et al. (2021), which only aim to encour
age isotropic representations, contrastive learning
 f
 irst term in Eq. 6, which is the key to the success
 of SimCSE. A quantitative analysis is given in §7.
 6 Experiment
 6.1 Evaluation Setup
 Weconduct our experiments on 7 semantic textual
 similarity (STS) tasks. Note that all our STS exper
iments are fully unsupervised and no STS training
 sets are used. Even for supervised SimCSE, we
 simply mean that we take extra labeled datasets
 for training, following previous work (Conneau
 et al., 2017). We also evaluate 7 transfer learning
 tasks and provide detailed results in Appendix E.
 We share a similar sentiment with Reimers and
 Gurevych (2019) that the main goal of sentence
 embeddings is to cluster semantically similar sen
tences and hence take STS as the main result.
 Semantic textual similarity tasks. We evalu
ate on 7 STS tasks: STS 2012–2016 (Agirre
 et al., 2012, 2013, 2014, 2015, 2016), STS
 Benchmark (Cer et al., 2017) and SICK
Relatedness (Marelli et al., 2014). When compar
ing to previous work, we identify invalid compari
son patterns in published papers in the evaluation
 settings, including (a) whether to use an additional
 regressor, (b) Spearman’s vs Pearson’s correlation,
 and (c) how the results are aggregated (Table B.1).
 Wediscuss the detailed differences in Appendix B
 and choose to follow the setting of Reimers and
 Gurevych (2019) in our evaluation (no additional
 regressor, Spearman’s correlation, and “all” aggre
gation). We also report our replicated study of
 previous work as well as our results evaluated in
 a different setting in Table B.2 and Table B.3. We
 call for unifying the setting in evaluating sentence
 embeddings for future research.
 Training details. We start from pre-trained check
points of BERT (Devlin et al., 2019) (uncased)
 or RoBERTa (Liu et al., 2019) (cased) and take
 the [CLS] representation as the sentence embed
ding9 (see §6.3 for comparison between different
 pooling methods). We train unsupervised SimCSE
 on 106 randomly sampled sentences from English
 Wikipedia, and train supervised SimCSE on the
 combination of MNLI and SNLI datasets (314k).
 More training details can be found in Appendix A.
 9There is an MLP layer over [CLS] in BERT’s original
 implementation and we keep it with random initialization.
Model STS12 STS13 STS14 STS15 STS16 STS-B SICK-R Avg.
 Unsupervisedmodels
 GloVeembeddings(avg.) 55.14 70.66 59.73 68.25 63.66 58.02 53.76 61.32
 BERTbase(first-lastavg.) 39.70 59.38 49.67 66.03 66.19 53.87 62.06 56.70
 BERTbase-flow 58.40 67.10 60.85 75.16 71.22 68.66 64.47 66.55
 BERTbase-whitening 57.83 66.90 60.90 75.08 71.31 68.24 63.73 66.28
 IS-BERTbase 56.77 69.24 61.21 75.23 70.16 69.21 64.25 66.58
 CT-BERTbase 61.63 76.80 68.47 77.50 76.48 74.31 69.19 72.05
 SimCSE-BERTbase 68.40 82.41 74.38 80.91 78.56 76.85 72.23 76.25
 RoBERTabase(first-lastavg.) 40.88 58.74 49.07 65.63 61.48 58.55 61.63 56.57
 RoBERTabase-whitening 46.99 63.24 57.23 71.36 68.99 61.36 62.91 61.73
 DeCLUTR-RoBERTabase 52.41 75.19 65.52 77.12 78.63 72.41 68.62 69.99
 SimCSE-RoBERTabase 70.16 81.77 73.24 81.36 80.65 80.22 68.56 76.57
 SimCSE-RoBERTalarge 72.86 83.99 75.62 84.77 81.80 81.98 71.26 78.90
 Supervisedmodels
 InferSent-GloVe 52.86 66.75 62.15 72.77 66.87 68.03 65.65 65.01
 UniversalSentenceEncoder 64.49 67.80 64.61 76.83 73.18 74.92 76.69 71.22
 SBERTbase 70.97 76.53 73.19 79.09 74.30 77.03 72.91 74.89
 SBERTbase-flow 69.78 77.27 74.35 82.01 77.46 79.12 76.21 76.60
 SBERTbase-whitening 69.65 77.57 74.66 82.27 78.39 79.52 76.91 77.00
 CT-SBERTbase 74.84 83.20 78.07 83.84 77.93 81.46 76.42 79.39
 SimCSE-BERTbase 75.30 84.67 80.19 85.40 80.82 84.25 80.39 81.57
 SRoBERTabase 71.54 72.49 70.80 78.74 73.69 77.77 74.46 74.21
 SRoBERTabase-whitening 70.46 77.07 74.46 81.64 76.43 79.49 76.65 76.60
 SimCSE-RoBERTabase 76.53 85.21 80.95 86.03 82.57 85.83 80.50 82.52
 SimCSE-RoBERTalarge 77.46 87.27 82.36 86.66 83.93 86.70 81.95 83.76
 Table5:SentenceembeddingperformanceonSTStasks(Spearman’scorrelation,“all”setting).Wehighlightthe
 highestnumbersamongmodelswiththesamepre-trainedencoder. :resultsfromReimersandGurevych(2019);
 :resultsfromZhangetal.(2020);allotherresultsarereproducedorreevaluatedbyourselves.ForBERT-flow(Li
 etal.,2020)andwhitening(Suetal.,2021),weonlyreportthe“NLI”setting(seeTableC.1).
 6.2 MainResults
 WecompareunsupervisedandsupervisedSim
CSEtopreviousstate-of-the-artsentenceembed
dingmethodsonSTStasks. Unsupervisedbase
lines include averageGloVe embeddings (Pen
ningtonetal.,2014),averageBERTorRoBERTa
 embeddings10,andpost-processingmethodssuch
 as BERT-flow (Li et al., 2020) and BERT
whitening(Suetal.,2021).Wealsocomparetosev
eralrecentmethodsusingacontrastiveobjective,
 including1)IS-BERT(Zhangetal.,2020),which
 maximizestheagreementbetweenglobalandlo
cal features;2)DeCLUTR(Giorgietal.,2021),
 whichtakesdifferentspansfromthesamedocu
mentaspositivepairs;3)CT(Carlssonetal.,2021),
 whichalignsembeddingsof thesamesentence
 fromtwodifferentencoders.11Othersupervised
 10FollowingSuetal.(2021),wetaketheaverageofthefirst
 andthelastlayers,whichisbetterthanonlytakingthelast.
 11WedonotcomparetoCLEAR(Wuetal.,2020),because
 theyuse theirownversionofpre-trainedmodels, andthe
 numbersappear tobemuchlower. AlsonotethatCTisa
 concurrentworktoours.
 methodsincludeInferSent(Conneauetal.,2017),
 UniversalSentenceEncoder(Ceretal.,2018),and
 SBERT/SRoBERTa(ReimersandGurevych,2019)
 withpost-processingmethods(BERT-flow,whiten
ing, andCT).Weprovidemoredetailsof these
 baselinesinAppendixC.
 Table5showstheevaluationresultson7STS
 tasks. SimCSEcansubstantiallyimproveresults
 onall thedatasetswithorwithoutextraNLIsu
pervision,greatlyoutperformingthepreviousstate
of-the-artmodels.Specifically,ourunsupervised
 SimCSE-BERTbase improves thepreviousbest
 averagedSpearman’scorrelationfrom72.05%to
 76.25%,evencomparabletosupervisedbaselines.
 WhenusingNLIdatasets,SimCSE-BERTbasefur
therpushesthestate-of-the-artresultsto81.57%.
 The gains aremore pronouncedonRoBERTa
 encoders, andour supervisedSimCSEachieves
 83.76%withRoBERTalarge.
 InAppendixE,we showthat SimCSEalso
 achievesonparorbettertransfertaskperformance
 comparedtoexistingwork,andanauxiliaryMLM
 objectivecanfurtherboostperformance.
incorporate weighting of different negatives:
 Pooler
 Unsup. Sup.
 [CLS]
 w/ MLP
 w/ MLP(train)
 w/o MLP
 First-last avg.
 81.7
 82.5
 80.9
 81.2
 86.2
 85.8
 86.2
 86.1
 Table 6: Ablation studies of different pooling methods
 in unsupervised and supervised SimCSE. [CLS] w/
 MLP(train): using MLP on [CLS] during training but
 removing it during testing. The results are based on the
 development set of STS-B using BERTbase.
 Hard neg N/A Contradiction-
 0.5
 1.0
 2.0
 Contra.+
 Neutral
 1.0
 STS-B
 84.9 86.1 86.2 86.2
 85.3
 Table 7: STS-B development results with different hard
 negative policies. “N/A”: no hard negative.
 6.3 Ablation Studies
 Weinvestigate the impact of different pooling meth
ods and hard negatives. All reported results in this
 section are based on the STS-B development set.
 Weprovide more ablation studies (normalization,
 temperature, and MLM objectives) in Appendix D.
 Pooling methods. Reimers and Gurevych (2019);
 Li et al. (2020) show that taking the average em
beddings of pre-trained models (especially from
 both the first and last layers) leads to better perfor
mance than [CLS]. Table 6 shows the comparison
 between different pooling methods in both unsuper
vised and supervised SimCSE. For [CLS] repre
sentation, the original BERT implementation takes
 an extra MLP layer on top of it. Here, we consider
 three different settings for [CLS]: 1) keeping the
 MLPlayer; 2) no MLP layer; 3) keeping MLP dur
ing training but removing it at testing time. We find
 that for unsupervised SimCSE, taking [CLS] rep
resentation with MLP only during training works
 the best; for supervised SimCSE, different pooling
 methods do not matter much. By default, we take
 [CLS]with MLP(train) for unsupervised SimCSE
 and [CLS]with MLP for supervised SimCSE.
 Hard negatives. Intuitively, it may be beneficial
 to differentiate hard negatives (contradiction exam
ples) from other in-batch negatives. Therefore, we
 esim(hih+
 i )
 log
 N
 j=1 esim(hih+
 j ) + 1j
 iesim(hihj )
 where 1j
 i 
(8)
 01 isan indicator that equals 1 if
 and only if i = j. We train SimCSE with different
 values of and evaluate the trained models on
 the development set of STS-B. We also consider
 taking neutral hypotheses as hard negatives. As
 shown in Table 7, = 1 performs the best, and
 neutral hypotheses do not bring further gains.
 7 Analysis
 In this section, we conduct further analyses to un
derstand the inner workings of SimCSE.
 Uniformity and alignment. Figure 3 shows uni
formity and alignment of different sentence embed
ding models along with their averaged STS results.
 In general, models which have both better align
ment and uniformity achieve better performance,
 confirming the findings in Wang and Isola (2020).
 We also observe that (1) though pre-trained em
beddings have good alignment, their uniformity is
 poor (i.e., the embeddings are highly anisotropic);
 (2) post-processing methods like BERT-flow and
 BERT-whitening greatly improve uniformity but
 also suffer a degeneration in alignment; (3) unsu
pervised SimCSE effectively improves uniformity
 of pre-trained embeddings whereas keeping a good
 alignment; (4) incorporating supervised data in
 SimCSE further amends alignment. In Appendix F,
 we further show that SimCSE can effectively flat
ten singular value distribution of pre-trained em
beddings. In Appendix G, we demonstrate that
 SimCSE provides more distinguishable cosine sim
ilarities between different sentence pairs.
 Qualitative comparison. We conduct a small
scale retrieval experiment using SBERTbase and
 SimCSE-BERTbase. We use 150k captions from
 Flickr30k dataset and take any random sentence as
 query to retrieve similar sentences (based on cosine
 similarity). As several examples shown in Table 8,
 the retrieved sentences by SimCSE have a higher
 quality compared to those retrieved by SBERT.
 8 Related Work
 Early work in sentence embeddings builds upon the
 distributional hypothesis by predicting surrounding
 extend our training objective defined in Eq. 5 to
 sentences of a given one (Kiros et al., 2015; Hill
SBERTbase
 Supervised SimCSE-BERTbase
 Query: A man riding a small boat in a harbor.
 #1 Agroupofmentraveling over the ocean in a small boat. A man on a moored blue and white boat.
 #2 Twomensitonthe bow of a colorful boat.
 Amanis riding in a boat on the water.
 #3 Amanwearingalife jacket is in a small boat on a lake. A man in a blue boat on the water.
 Query: A dog runs on the green grass near a wooden fence.
 #1 Adogrunsonthe green grass near a grove of trees.
 The dog by the fence is running on the grass.
 #2 Abrownandwhite dog runs through the green grass.
 #3 Thedogsrun in the green field.
 Dog running through grass in fenced area.
 Adog runs on the green grass near a grove of trees.
 Table 8: Retrieved top-3 examples by SBERT and supervised SimCSE from Flickr30k (150k sentences).
 0.7
 0.6
 Alignment
 align
 0.5
 0.4
 0.3
 0.2
 0.1
 0.0
 −4.0
 BERT-whitening (66.3)
 BERT-flow (66.6)
 SBERT-whitening (77.0)
 SBERT-flow (76.6)
 Unsup. SimCSE (76.3)
 Avg. BERT (56.7)
 SimCSE (81.6)
 SBERT (74.9)
 Next3Sent (63.1)
 −3.5
 −3.0
 −2.5
 −2.0
 8nifoUmity
 uniform
 −1.5
 −1.0
 100
 90
 80
 70
 60
 50
 40
 Figure 3: align-uniform plot of models based on
 BERTbase. Color of points and numbers in brackets
 represent average STS performance (Spearman’s corre
lation). Next3Sent: “next 3 sentences” from Table 2.
 et al., 2016; Logeswaran and Lee, 2018). Pagliar
dini et al. (2018) show that simply augmenting
 the idea of word2vec (Mikolov et al., 2013) with
 n-gram embeddings leads to strong results. Sev
eral recent (and concurrent) approaches adopt con
trastive objectives (Zhang et al., 2020; Giorgi et al.,
 2021; Wu et al., 2020; Meng et al., 2021; Carlsson
 et al., 2021; Kim et al., 2021; Yan et al., 2021) by
 taking different views—from data augmentation or
 different copies of models—of the same sentence
 or document. Compared to these work, SimCSE
 uses the simplest idea by taking different outputs
 of the same sentence from standard dropout, and
 performs the best on STS tasks.
 Supervised sentence embeddings are promised
 to have stronger performance compared to unsu
pervised counterparts. Conneau et al. (2017) pro
pose to fine-tune a Siamese model on NLI datasets,
 which is further extended to other encoders or
 pre-trained models (Cer et al., 2018; Reimers and
 Gurevych, 2019). Furthermore, Wieting and Gim
pel (2018); Wieting et al. (2020) demonstrate that
 bilingual and back-translation corpora provide use
ful supervision for learning semantic similarity. An
other line of work focuses on regularizing embed
dings (Li et al., 2020; Su et al., 2021; Huang et al.,
 2021) to alleviate the representation degeneration
 problem (as discussed in §5), and yields substantial
 improvement over pre-trained language models.
 9 Conclusion
 In this work, we propose SimCSE, a simple con
trastive learning framework, which greatly im
proves state-of-the-art sentence embeddings on se
mantic textual similarity tasks. We present an un
supervised approach which predicts input sentence
 itself with dropout noise and a supervised approach
 utilizing NLI datasets. We further justify the inner
 workings of our approach by analyzing alignment
 and uniformity of SimCSE along with other base
line models. We believe that our contrastive objec
tive, especially the unsupervised one, may have a
 broader application in NLP. It provides a new per
spective on data augmentation with text input, and
 can be extended to other continuous representations
 and integrated in language model pre-training.
 Acknowledgements
 We thank Tao Lei, Jason Lee, Zhengyan Zhang,
 Jinhyuk Lee, Alexander Wettig, Zexuan Zhong,
 and the members of the Princeton NLP group for
 helpful discussion and valuable feedback. This
 research is supported by a Graduate Fellowship at
 Princeton University and a gift award from Apple.
References
 Eneko Agirre, Carmen Banea, Claire Cardie, Daniel
 Cer, Mona Diab, Aitor Gonzalez-Agirre, Weiwei
 Guo, Iñigo Lopez-Gazpio, Montse Maritxalar, Rada
 Mihalcea, German Rigau, Larraitz Uria, and Janyce
 Wiebe. 2015. SemEval-2015 task 2: Semantic tex
tual similarity, English, Spanish and pilot on inter
pretability. In Proceedings of the 9th International
 Workshop on Semantic Evaluation (SemEval 2015),
 pages 252–263.
 Eneko Agirre, Carmen Banea, Claire Cardie, Daniel
 Cer, Mona Diab, Aitor Gonzalez-Agirre, Weiwei
 Guo, Rada Mihalcea, German Rigau, and Janyce
 Wiebe. 2014. SemEval-2014 task 10: Multilingual
 semantic textual similarity. In Proceedings of the
 8th International Workshop on Semantic Evaluation
 (SemEval 2014), pages 81–91.
 Eneko Agirre, Carmen Banea, Daniel Cer, Mona Diab,
 Aitor Gonzalez-Agirre, Rada Mihalcea, German
 Rigau, and Janyce Wiebe. 2016. SemEval-2016
 task 1: Semantic textual similarity, monolingual
 and cross-lingual evaluation. In Proceedings of the
 10th International Workshop on Semantic Evalua
tion (SemEval-2016), pages 497–511. Association
 for Computational Linguistics.
 Eneko Agirre, Daniel Cer, Mona Diab, and Aitor
 Gonzalez-Agirre. 2012. SemEval-2012 task 6: A
 pilot on semantic textual similarity. In *SEM 2012:
 The First Joint Conference on Lexical and Compu
tational Semantics– Volume 1: Proceedings of the
 main conference and the shared task, and Volume
 2: Proceedings of the Sixth International Workshop
 on Semantic Evaluation (SemEval 2012), pages 385
393.
 Eneko Agirre, Daniel Cer, Mona Diab, Aitor Gonzalez
Agirre, and Weiwei Guo. 2013. *SEM 2013 shared
 task: Semantic textual similarity. In Second Joint
 Conference on Lexical and Computational Seman
tics (*SEM), Volume 1: Proceedings of the Main
 Conference and the Shared Task: Semantic Textual
 Similarity, pages 32–43.
 Sanjeev Arora, Yingyu Liang, and Tengyu Ma. 2017.
 Asimple but tough-to-beat baseline for sentence em
beddings. In International Conference on Learning
 Representations (ICLR).
 Samuel R. Bowman, Gabor Angeli, Christopher Potts,
 and Christopher D. Manning. 2015. A large anno
tated corpus for learning natural language inference.
 In Empirical Methods in Natural Language Process
ing (EMNLP), pages 632–642.
 Fredrik Carlsson, Amaru Cuba Gyllensten, Evan
gelia Gogoulou, Erik Ylipää Hellqvist, and Magnus
 Sahlgren. 2021. Semantic re-tuning with contrastive
 tension. In International Conference on Learning
 Representations (ICLR).
 Daniel Cer, Mona Diab, Eneko Agirre, Iñigo Lopez
Gazpio, and Lucia Specia. 2017. SemEval-2017
 task 1: Semantic textual similarity multilingual and
 crosslingual focused evaluation. In Proceedings of
 the 11th International Workshop on Semantic Evalu
ation (SemEval-2017), pages 1–14.
 Daniel Cer, Yinfei Yang, Sheng-yi Kong, Nan Hua,
 Nicole Limtiaco, Rhomni St. John, Noah Constant,
 Mario Guajardo-Cespedes, Steve Yuan, Chris Tar,
 Brian Strope, and Ray Kurzweil. 2018. Universal
 sentence encoder for English. In Empirical Methods
 in Natural Language Processing (EMNLP): System
 Demonstrations, pages 169–174.
 Ting Chen, Simon Kornblith, Mohammad Norouzi,
 and Geoffrey Hinton. 2020. A simple framework
 for contrastive learning of visual representations.
 In International Conference on Machine Learning
 (ICML), pages 1597–1607.
 Ting Chen, Yizhou Sun, Yue Shi, and Liangjie Hong.
 2017. On sampling strategies for neural network
based collaborative filtering. In ACM SIGKDD
 International Conference on Knowledge Discovery
 and Data Mining, pages 767–776.
 Alexis Conneau and DouweKiela. 2018. SentEval: An
 evaluation toolkit for universal sentence representa
tions. In International Conference on Language Re
sources and Evaluation (LREC).
 Alexis Conneau, Douwe Kiela, Holger Schwenk, Loïc
 Barrault, and Antoine Bordes. 2017. Supervised
 learning of universal sentence representations from
 natural language inference data.
 In Empirical
 Methods in Natural Language Processing (EMNLP),
 pages 670–680.
 Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
 Kristina Toutanova. 2019. BERT: Pre-training of
 deep bidirectional transformers for language under
standing. In North American Chapter of the As
sociation for Computational Linguistics: Human
 Language Technologies (NAACL-HLT), pages 4171
4186.
 William B. Dolan and Chris Brockett. 2005. Automati
cally constructing a corpus of sentential paraphrases.
 In Proceedings of the Third International Workshop
 on Paraphrasing (IWP2005).
 Alexey Dosovitskiy, Jost Tobias Springenberg, Mar
tin Riedmiller, and Thomas Brox. 2014. Discrim
inative unsupervised feature learning with convolu
tional neural networks. In Advances in Neural Infor
mation Processing Systems (NIPS), volume 27.
 Kawin Ethayarajh. 2019. How contextual are contex
tualized word representations? comparing the geom
etry of BERT, ELMo, and GPT-2 embeddings. In
 Empirical Methods in Natural Language Processing
 and International Joint Conference on Natural Lan
guage Processing (EMNLP-IJCNLP), pages 55–65.
 Jun Gao, Di He, Xu Tan, Tao Qin, Liwei Wang,
 and Tieyan Liu. 2019. Representation degenera
tion problem in training natural language generation
models. In International Conference on Learning
 Representations (ICLR).
 Dan Gillick, Sayali Kulkarni, Larry Lansing, Alessan
dro Presta, Jason Baldridge, Eugene Ie, and Diego
 Garcia-Olano. 2019. Learning dense representa
tions for entity retrieval. In Computational Natural
 Language Learning (CoNLL), pages 528–537.
 John Giorgi, Osvald Nitski, Bo Wang, and Gary Bader.
 2021. DeCLUTR: Deep contrastive learning for
 unsupervised textual representations. In Associ
ation for Computational Linguistics and Interna
tional Joint Conference on Natural Language Pro
cessing (ACL-IJCNLP), pages 879–895.
 Raia Hadsell, Sumit Chopra, and Yann LeCun. 2006.
 Dimensionality reduction by learning an invariant
 mapping. In IEEE/CVF Conference on Computer
 Vision and Pattern Recognition (CVPR), volume 2,
 pages 1735–1742. IEEE.
 MatthewHenderson, RamiAl-Rfou, BrianStrope, Yun
Hsuan Sung, László Lukács, Ruiqi Guo, Sanjiv Ku
mar, Balint Miklos, and Ray Kurzweil. 2017. Effi
cient natural language response suggestion for smart
 reply. arXiv preprint arXiv:1705.00652.
 Felix Hill, Kyunghyun Cho, and Anna Korhonen. 2016.
 Learning distributed representations of sentences
 from unlabelled data. In North American Chapter of
 the Association for Computational Linguistics: Hu
man Language Technologies (NAACL-HLT), pages
 1367–1377.
 Minqing Hu and Bing Liu. 2004. Mining and summa
rizing customer reviews. In ACM SIGKDD interna
tional conference on Knowledge discovery and data
 mining.
 Junjie Huang, Duyu Tang, Wanjun Zhong, Shuai Lu,
 Linjun Shou, Ming Gong, Daxin Jiang, and Nan
 Duan. 2021. Whiteningbert: An easy unsuper
vised sentence embedding approach. arXiv preprint
 arXiv:2104.01767.
 Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick
 Lewis, Ledell Wu, Sergey Edunov, Danqi Chen,
 and Wen-tau Yih. 2020. Dense passage retrieval
 for open-domain question answering. In Empirical
 Methods in Natural Language Processing (EMNLP),
 pages 6769–6781.
 Taeuk Kim, Kang Min Yoo, and Sang-goo Lee. 2021.
 Self-guided contrastive learning for BERT sentence
 representations. In Association for Computational
 Linguistics and International Joint Conference on
 Natural LanguageProcessing (ACL-IJCNLP),pages
 2528–2540.
 Ryan Kiros, Yukun Zhu, Ruslan Salakhutdinov,
 Richard S Zemel, Antonio Torralba, Raquel Urtasun,
 and Sanja Fidler. 2015. Skip-thought vectors. In
 Advances in Neural Information Processing Systems
 (NIPS), pages 3294–3302.
 Bohan Li, Hao Zhou, Junxian He, Mingxuan Wang,
 Yiming Yang, and Lei Li. 2020. On the sentence
 embeddings from pre-trained language models. In
 Empirical Methods in Natural Language Processing
 (EMNLP), pages 9119–9130.
 Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man
dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
 Luke Zettlemoyer, and Veselin Stoyanov. 2019.
 Roberta: A robustly optimized bert pretraining ap
proach. arXiv preprint arXiv:1907.11692.
 Lajanugen Logeswaran and Honglak Lee. 2018. An ef
f
 icient framework for learning sentence representa
tions. In International Conference on Learning Rep
resentations (ICLR).
 Edward Ma. 2019.
 Nlp augmentation.
 https://github.com/makcedward/nlpaug.
 Marco Marelli, Stefano Menini, Marco Baroni, Luisa
 Bentivogli, Raffaella Bernardi, and Roberto Zampar
elli. 2014. A SICK cure for the evaluation of compo
sitional distributional semantic models. In Interna
tional Conference on Language Resources and Eval
uation (LREC), pages 216–223.
 Yu Meng, Chenyan Xiong, Payal Bajaj, Saurabh Ti
wary, Paul Bennett, Jiawei Han, and Xia Song.
 2021. COCO-LM: Correcting and contrasting text
 sequences for language model pretraining. arXiv
 preprint arXiv:2102.08473.
 Jorma Kaarlo Merikoski. 1984. On the trace and the
 sum of elements of a matrix. Linear Algebra and its
 Applications, 60:177–185.
 Tomas Mikolov, Ilya Sutskever, Kai Chen, G. Corrado,
 and J. Dean. 2013. Distributed representations of
 words and phrases and their compositionality. In
 Advances in Neural Information Processing Systems
 (NIPS).
 Jiaqi Mu and Pramod Viswanath. 2018. All-but-the
top: Simple and effective postprocessing for word
 representations.
 In International Conference on
 Learning Representations (ICLR).
 Yixin Nie, Adina Williams, Emily Dinan, Mohit
 Bansal, Jason Weston, and Douwe Kiela. 2020. Ad
versarial NLI: A new benchmark for natural lan
guage understanding. In Association for Computa
tional Linguistics (ACL), pages 4885–4901.
 Matteo Pagliardini, Prakhar Gupta, and Martin Jaggi.
 2018. Unsupervised learning of sentence embed
dings using compositional n-gram features. In North
 American Chapter of the Association for Computa
tional Linguistics: Human Language Technologies
 (NAACL-HLT), pages 528–540.
 Bo Pang and Lillian Lee. 2004. A sentimental educa
tion: Sentiment analysis using subjectivity summa
rization based on minimum cuts. In Association for
 Computational Linguistics (ACL), pages 271–278.
Bo Pang and Lillian Lee. 2005. Seeing stars: Exploit
ing class relationships for sentiment categorization
 with respect to rating scales. In Association for Com
putational Linguistics (ACL), pages 115–124.
 Jeffrey Pennington, Richard Socher, and Christopher
 Manning. 2014. GloVe: Global vectors for word
 representation. In Proceedings of the 2014 Confer
ence on Empirical Methods in Natural Language
 Processing (EMNLP), pages 1532–1543.
 Nils Reimers, Philip Beyer, and Iryna Gurevych. 2016.
 Task-oriented intrinsic evaluation of semantic tex
tual similarity. In International Conference on Com
putational Linguistics (COLING), pages 87–96.
 Nils Reimers and Iryna Gurevych. 2019. Sentence
BERT: Sentence embeddings using Siamese BERT
networks. In Empirical Methods in Natural Lan
guage Processing and International Joint Confer
ence on Natural Language Processing (EMNLP
IJCNLP), pages 3982–3992.
 Richard Socher, Alex Perelygin, Jean Wu, Jason
 Chuang, Christopher D. Manning, Andrew Ng, and
 Christopher Potts. 2013. Recursive deep models
 for semantic compositionality over a sentiment tree
bank. In Empirical Methods in Natural Language
 Processing (EMNLP), pages 1631–1642.
 Nitish Srivastava, Geoffrey Hinton, Alex Krizhevsky,
 Ilya Sutskever, and Ruslan Salakhutdinov. 2014.
 Dropout: a simple way to prevent neural networks
 from overfitting. The Journal of Machine Learning
 Research (JMLR), 15(1):1929–1958.
 Jianlin Su, Jiarun Cao, Weijie Liu, and Yangyiwen Ou.
 2021. Whitening sentence representations for bet
ter semantics and faster retrieval. arXiv preprint
 arXiv:2103.15316.
 Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob
 Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz
 Kaiser, and Illia Polosukhin. 2017. Attention is all
 you need. In Advances in Neural Information Pro
cessing Systems (NIPS), pages 6000–6010.
 Ellen M Voorhees and Dawn M Tice. 2000. Building
 a question answering test collection. In the 23rd
 annual international ACM SIGIR conference on Re
search and development in information retrieval,
 pages 200–207.
 Lingxiao Wang, Jing Huang, Kevin Huang, Ziniu Hu,
 Guangtao Wang, and Quanquan Gu. 2020. Improv
ing neural language generation with spectrum con
trol. In International Conference on Learning Rep
resentations (ICLR).
 Tongzhou Wang and Phillip Isola. 2020. Understand
ing contrastive representation learning through align
ment and uniformity on the hypersphere. In Inter
national Conference on Machine Learning (ICML),
 pages 9929–9939.
 Janyce Wiebe, Theresa Wilson, and Claire Cardie.
 2005. Annotating expressions of opinions and emo
tions in language. Language resources and evalua
tion, 39(2-3):165–210.
 John Wieting and Kevin Gimpel. 2018. ParaNMT
50M: Pushing the limits of paraphrastic sentence
 embeddings with millions of machine translations.
 In Association for Computational Linguistics (ACL),
 pages 451–462.
 John Wieting, Graham Neubig, and Taylor Berg
Kirkpatrick. 2020. A bilingual generative trans
former for semantic sentence embedding. In Em
pirical Methods in Natural Language Processing
 (EMNLP), pages 1581–1594.
 Adina Williams, Nikita Nangia, and Samuel Bowman.
 2018. A broad-coverage challenge corpus for sen
tence understanding through inference. In North
 American Chapter of the Association for Computa
tional Linguistics: Human Language Technologies
 (NAACL-HLT), pages 1112–1122.
 Thomas Wolf, Lysandre Debut, Victor Sanh, Julien
 Chaumond, Clement Delangue, Anthony Moi, Pier
ric Cistac, Tim Rault, Remi Louf, Morgan Funtow
icz, Joe Davison, Sam Shleifer, Patrick von Platen,
 Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu,
 Teven Le Scao, Sylvain Gugger, Mariama Drame,
 Quentin Lhoest, and Alexander Rush. 2020. Trans
formers: State-of-the-art natural language process
ing. In Empirical Methods in Natural LanguagePro
cessing (EMNLP): System Demonstrations, pages
 38–45.
 Zhuofeng Wu, Sinong Wang, Jiatao Gu, Madian
 Khabsa, Fei Sun, and Hao Ma. 2020. Clear: Con
trastive learning for sentence representation. arXiv
 preprint arXiv:2012.15466.
 YuanmengYan,RumeiLi,SiruiWang,FuzhengZhang,
 Wei Wu, and Weiran Xu. 2021. ConSERT: A
 contrastive framework for self-supervised sentence
 representation transfer. In Association for Com
putational Linguistics and International Joint Con
ference on Natural Language Processing (ACL
IJCNLP), pages 5065–5075.
 Peter Young, Alice Lai, Micah Hodosh, and Julia Hock
enmaier. 2014. From image descriptions to visual
 denotations: New similarity metrics for semantic in
ference over event descriptions. Transactions of the
 Association for Computational Linguistics, 2:67–78.
 Yan Zhang, Ruidan He, Zuozhu Liu, Kwan Hui Lim,
 and Lidong Bing. 2020. An unsupervised sentence
 embedding method by mutual information maxi
mization. In Empirical Methods in Natural Lan
guage Processing (EMNLP), pages 1601–1610.
A Training Details
 Paper
 Reg.
 Metric
 Aggr.
 We implement SimCSE with transformers
 package (Wolf et al., 2020). For supervised Sim
CSE, wetrain our models for 3 epochs, evaluate the
 model every 250 training steps on the development
 set of STS-B and keep the best checkpoint for the
 f
 inal evaluation on test sets. We do the same for
 the unsupervised SimCSE, except that we train the
 model for one epoch. We carry out grid-search of
 batch size 
64128256512 andlearning rate
 1e-5, 3e-5, 5e-5 on STS-B development set
 and adopt the hyperparameter settings in Table A.1.
 Wefind that SimCSE is not sensitive to batch sizes
 as long as tuning the learning rates accordingly,
 which contradicts the finding that contrastive learn
ing requires large batch sizes (Chen et al., 2020).
 It is probably due to that all SimCSE models start
 from pre-trained checkpoints, which already pro
vide us a good set of initial parameters.
 Unsupervised
 BERT
 base large base large
 Supervised
 RoBERTa base large
 Batch size
 64
 64
 512 512 512 512
 Learning rate 3e-5 1e-5 1e-5 3e-5 5e-5 1e-5
 Table A.1: Batch sizes and learning rates for SimCSE.
 For both unsupervised and supervised SimCSE,
 we take the [CLS] representation with an MLP
 layer on top of it as the sentence representation.
 Specially, for unsupervised SimCSE, we discard
 the MLP layer and only use the [CLS] output
 during test, since we find that it leads to better
 performance (ablation study in §6.3).
 Finally, we introduce one more optional variant
 which adds a masked language modeling (MLM)
 objective (Devlin et al., 2019) as an auxiliary loss
 to Eq. 1: + 
mlm ( is a hyperparameter).
 This helps SimCSE avoid catastrophic forgetting
 of token-level knowledge. As we will show in Ta
ble D.2, we find that adding this term can help
 improve performance on transfer tasks (not on
 sentence-level STS tasks).
 B Different Settings for STS Evaluation
 Weelaborate the differences in STS evaluation set
tings in previous work in terms of (a) whether to
 use additional regressors; (b) reported metrics; (c)
 different ways to aggregate results.
 Additional regressors. The default SentEval
 implementation applies a linear regressor on top of
 Hill et al. (2016)
 Conneau et al. (2017)
 Conneau and Kiela (2018)
 Reimers and Gurevych (2019)
 Zhang et al. (2020)
 Li et al. (2020)
 Su et al. (2021)
 Wieting et al. (2020)
 Giorgi et al. (2021)
 Ours
 Both
 Pearson
 Pearson
 Spearman
 Spearman
 all
 mean
 mean
 all
 all
 Spearman wmean
 Spearman wmean
 Pearson
 mean
 Spearman mean
 Spearman
 all
 Table B.1: STS evaluation protocols used in different
 papers. “Reg.”: whether an additional regressor is used;
 “aggr.”: methods to aggregate different subset results.
 frozen sentence embeddings for STS-B and SICK
R, and train the regressor on the training sets of
 the two tasks, while most sentence representation
 papers take the raw embeddings and evaluate in an
 unsupervised way. In our experiments, we do not
 apply any additional regressors and directly take
 cosine similarities for all STS tasks.
 Metrics. Both Pearson’s and Spearman’s cor
relation coefficients are used in the literature.
 Reimers et al. (2016) argue that Spearman corre
lation, which measures the rankings instead of the
 actual scores, better suits the need of evaluating
 sentence embeddings. For all of our experiments,
 we report Spearman’s rank correlation.
 Aggregation methods. Given that each year’s
 STS challenge contains several subsets, there are
 different choices to gather results from them: one
 way is to concatenate all the topics and report the
 overall Spearman’s correlation (denoted as “all”),
 and the other is to calculate results for differ
ent subsets separately and average them (denoted
 as “mean” if it is simple average or “wmean” if
 weighted by the subset sizes). However, most pa
pers do not claim the method they take, making it
 challenging for a fair comparison. We take some
 of the most recent work: SBERT (Reimers and
 Gurevych, 2019), BERT-flow (Li et al., 2020) and
 BERT-whitening (Su et al., 2021)12 as an example:
 In Table B.2, we compare our reproduced results
 to reported results of SBERT and BERT-whitening,
 and findthat Reimers and Gurevych (2019) take the
 “all” setting but Li et al. (2020); Su et al. (2021) take
 the “wmean” setting, even though Li et al. (2020)
 claim that they take the same setting as Reimers
 12Li et al. (2020) and Su et al. (2021) have consistent results,
 so we assume that they take the same evaluation and just take
 BERT-whitening in experiments here.
Model STS12 STS13 STS14 STS15 STS16 STS-B SICK-R Avg.
 SBERT(all) 70.97 76.53 73.19 79.09 74.30 76.98 72.91 74.85
 SBERT(wmean) 66.35 73.76 73.88 77.33 73.62 76.98 72.91 73.55
 SBERT 70.97 76.53 73.19 79.09 74.30 77.03 72.91 74.89
 BERT-whitening(NLI,all) 57.83 66.90 60.89 75.08 71.30 68.23 63.73 66.28
 BERT-whitening(NLI,wmean) 61.43 65.90 65.96 74.80 73.10 68.23 63.73 67.59
 BERT-whitening(NLI) 61.69 65.70 66.02 75.11 73.11 68.19 63.60 67.63
 BERT-whitening(target,all) 42.88 77.77 66.27 63.60 67.58 71.34 60.40 64.26
 BERT-whitening(target,wmean) 63.38 73.01 69.13 74.48 72.56 71.34 60.40 69.19
 BERT-whitening(target) 63.62 73.02 69.23 74.52 72.15 71.34 60.60 69.21
 TableB.2:Comparisonsofourreproducedresultsusingdifferentevaluationprotocolsandtheoriginalnumbers.
 :resultsfromReimersandGurevych(2019); :resultsfromSuetal.(2021);Otherresultsarereproducedbyus.
 FromthetableweseethatSBERTtakesthe“all”evaluationandBERT-whiteningtakesthe“wmean”evaluation.
 Model STS12 STS13 STS14 STS15 STS16 STS-B SICK-R Avg.
 BERTbase(first-lastavg.) 57.86 61.97 62.49 70.96 69.76 59.04 63.75 63.69
 +flow(NLI) 59.54 64.69 64.66 72.92 71.84 58.56 65.44 65.38
 +flow(target) 63.48 72.14 68.42 73.77 75.37 70.72 63.11 69.57
 +whitening(NLI) 61.69 65.70 66.02 75.11 73.11 68.19 63.60 67.63
 +whitening(target) 63.62 73.02 69.23 74.52 72.15 71.34 60.60 69.21
 Unsup.SimCSE-BERTbase 70.14 79.56 75.91 81.46 79.07 76.85 72.23 76.46
 SBERTbase(first-lastavg.) 68.70 74.37 74.73 79.65 75.21 77.63 74.84 75.02
 +flow(NLI) 67.75 76.73 75.53 80.63 77.58 79.10 78.03 76.48
 +flow(target) 68.95 78.48 77.62 81.95 78.94 81.03 74.97 77.42
 +whitening(NLI) 69.11 75.79 75.76 82.31 79.61 78.66 76.33 76.80
 +whitening(target) 69.01 78.10 77.04 80.83 77.93 80.50 72.54 76.56
 Sup.SimCSE-BERTbase 70.90 81.49 80.19 83.79 81.89 84.25 80.39 80.41
 TableB.3:STSresultswith“wmean”setting(Spearman). : fromLietal.(2020);Suetal.(2021).
 andGurevych(2019).Sincethe“all”settingfuses
 datafromdifferent topics together, itmakes the
 evaluationclosertoreal-worldscenarios,andun
lessspecified,wetakethe“all”setting.
 Welistevaluationsettingsforanumberofpre
viousworkinTableB.1.Someofthesettingsare
 reportedbythepaperandsomeofthemareinferred
 bycomparingtheresultsandcheckingtheircode.
 Aswecansee, theevaluationprotocolsarevery
 incoherentacrossdifferentpapers.Wecallforuni
fyingthesettinginevaluatingsentenceembeddings
 forfutureresearch.Wewillalsoreleaseourevalua
tioncodeforbetterreproducibility.Sinceprevious
 workusesdifferentevaluationprotocolsfromours,
 wefurtherevaluateourmodelsinthesesettingsto
 makeadirectcomparisontothepublishednum
bers. WeevaluateSimCSEwith“wmean”and
 Spearman’scorrelationtodirectlycomparetoLi
 etal.(2020)andSuetal.(2021)inTableB.3.
 C BaselineModels
 Weelaborateonhowweobtaindifferentbaselines
 forcomparisoninourexperiments:
 •ForaverageGloVeembedding(Pennington
 etal.,2014),InferSent(Conneauetal.,2017)
 andUniversalSentenceEncoder(Ceretal.,
 2018), wedirectly report the results from
 ReimersandGurevych(2019),sinceoureval
uationsettingisthesameastheirs.
 • ForBERT(Devlinetal.,2019)andRoBERTa
 (Liu et al., 2019), we download the pre
trainedmodelweightsfromHuggingFace’s
 Transformers13,andevaluatethemodels
 withourownscripts.
 •ForSBERTandSRoBERTa (Reimers and
 Gurevych,2019),wereusetheresultsfrom
 theoriginalpaper. For resultsnot reported
 byReimersandGurevych(2019),suchasthe
 performanceofSRoBERTaontransfertasks,
 wedownloadthemodelweightsfromSen
tenceTransformers14andevaluatethem.
 13https://github.com/huggingface/
 transformers
 14https://www.sbert.net/
Model STS12 STS13 STS14 STS15 STS16 STS-B SICK-R Avg.
 BERT-flow(NLI) 58.40 67.10 60.85 75.16 71.22 68.66 64.47 66.55
 BERT-flow(target) 53.15 78.38 66.02 62.09 70.84 71.70 61.97 66.31
 BERT-whitening(NLI) 57.83 66.90 60.90 75.08 71.31 68.24 63.73 66.28
 BERT-whitening(target) 42.88 77.77 66.28 63.60 67.58 71.34 60.40 64.26
 SBERT-flow(NLI) 69.78 77.27 74.35 82.01 77.46 79.12 76.21 76.60
 SBERT-flow(target) 66.18 82.69 76.22 73.72 75.71 79.99 73.82 75.48
 SBERT-whitening(NLI) 69.65 77.57 74.66 82.27 78.39 79.52 76.91 77.00
 SBERT-whitening(target) 52.91 81.91 75.44 72.24 72.93 80.50 72.54 72.64
 TableC.1:ComparisonofusingNLIortargetdataforpostprocessingmethods(“all”,Spearman’scorrelation).
 N/A 0.001 0.01 0.05 0.1 1
 STS-B 85.9 84.9 85.4 86.2 82.0 64.0
 TableD.1: STS-Bdevelopment results (Spearman’s
 correlation)withdifferent temperatures. “N/A”:Dot
 productinsteadofcosinesimilarity.
 • ForDeCLUTR(Giorgietal.,2021)andcon
trastive tension(Carlssonet al., 2021),we
 reevaluatetheircheckpointsinoursetting.
 •ForBERT-flow(Lietal.,2020), sincetheir
 originalnumberstakeadifferentsetting,we
 retraintheirmodelsusingtheircode15,and
 evaluatethemodelsusingourownscript.
 • ForBERT-whitening(Suetal.,2021),weim
plementedourownversionofwhiteningscript
 followingthesamepoolingmethodinSuetal.
 (2021),i.e.first-lastaveragepooling.Ourim
plementationcanreproducetheresultsfrom
 theoriginalpaper(seeTableB.2).
 ForbothBERT-flowandBERT-whitening,they
 havetwovariantsofpostprocessing:onetakesthe
 NLIdata(“NLI”)andonedirectlylearnstheem
beddingdistributiononthetargetsets(“target”).
 Wefindthat inourevaluationsetting,“target”is
 generallyworsethan“NLI”(TableC.1),soweonly
 reporttheNLIvariantinthemainresults.
 D AblationStudies
 Normalizationandtemperature.WetrainSim
CSEusingbothdotproductandcosinesimilarity
 withdifferenttemperaturesandevaluatethemon
 theSTS-Bdevelopmentset.AsshowninTableD.1,
 withacarefullytunedtemperature =005,co
sinesimilarityisbetterthandotproduct.
 15https://github.com/bohanli/BERT-flow
 Model STS-B Avg. transfer
 w/oMLM 86.2 85.8
 w/MLM
 =001 85.7 86.1
 =01 85.7 86.2
 =1 85.1 85.8
 TableD.2: Ablation studies of theMLMobjective
 basedonthedevelopmentsetsusingBERTbase.
 MLMauxiliarytask. Finally,westudytheim
pactoftheMLMauxiliaryobjectivewithdifferent
 .AsshowninTableD.2, thetoken-levelMLM
 objectiveimprovestheaveragedperformanceon
 transfertasksmodestly,yet itbringsaconsistent
 dropinsemantictextualsimilaritytasks.
 E TransferTasks
 Weevaluateourmodelsonthefollowingtrans
fer tasks: MR(PangandLee, 2005), CR(Hu
 andLiu, 2004), SUBJ (Pang andLee, 2004),
 MPQA(Wiebeetal.,2005),SST-2(Socheretal.,
 2013), TREC (Voorhees andTice, 2000) and
 MRPC(DolanandBrockett,2005).Alogisticre
gressionclassifieristrainedontopof(frozen)sen
tenceembeddingsproducedbydifferentmethods.
 WefollowdefaultconfigurationsfromSentEval16.
 TableE.1showstheevaluationresultsontrans
fer tasks. Wefindthat supervisedSimCSEper
formsonparorbetterthanpreviousapproaches,
 althoughthetrendofunsupervisedmodelsremains
 unclear.WefindthataddingthisMLMtermcon
sistentlyimprovesperformanceontransfertasks,
 confirmingourintuitionthatsentence-levelobjec
tivemaynotdirectlybenefittransfertasks.Wealso
 experimentwithpost-processingmethods(BERT
16https://github.com/facebookresearch/
 SentEval
Model
 MR CR SUBJ MPQA SST TREC MRPC Avg.
 Unsupervised models
 GloVe embeddings (avg.)
 Skip-thought
 77.25 78.30 91.17 87.85 80.18 83.00 72.87 81.52
 76.50 80.10 93.60 87.10 82.00 92.20 73.00 83.50
 Avg. BERT embeddings
 BERT-[CLS]embedding
 IS-BERTbase
 SimCSE-BERTbase
 w/ MLM
 78.66 86.25 94.37 88.66 84.40 92.80 69.54 84.94
 78.68 84.85 94.21 88.23 84.13 91.40 71.13 84.66
 81.09 87.18 94.96 88.75 85.96 88.64 74.24 85.83
 81.18 86.46 94.45 88.88 85.50 89.80 74.43 85.81
 82.92 87.23 95.71 88.73 86.81 87.01 78.07 86.64
 SimCSE-RoBERTabase
 w/ MLM
 SimCSE-RoBERTalarge
 w/ MLM
 81.04 87.74 93.28 86.94 86.60 84.60 73.68 84.84
 83.37 87.76 95.05 87.16 89.02 90.80 75.13 86.90
 82.74 87.87 93.66 88.22 88.58 92.00 69.68 86.11
 84.66 88.56 95.43 87.50 89.46 95.00 72.41 87.57
 Supervised models
 InferSent-GloVe
 Universal Sentence Encoder
 81.57 86.54 92.50 90.38 84.18 88.20 75.77 85.59
 80.09 85.19 93.98 86.70 86.38 93.20 70.14 85.10
 SBERTbase
 SimCSE-BERTbase
 w/ MLM
 83.64 89.43 94.39 89.86 88.96 89.60 76.00 87.41
 82.69 89.25 94.81 89.59 87.31 88.40 73.51 86.51
 82.68 88.88 94.52 89.82 88.41 87.60 76.12 86.86
 SRoBERTabase
 SimCSE-RoBERTabase
 w/ MLM
 SimCSE-RoBERTalarge
 w/ MLM
 84.91 90.83 92.56 88.75 90.50 88.60 78.14 87.76
 84.92 92.00 94.11 89.82 91.27 88.80 75.65 88.08
 85.08 91.76 94.02 89.72 92.31 91.20 76.52 88.66
 88.12 92.37 95.11 90.49 92.75 91.80 76.64 89.61
 88.45 92.53 95.19 90.58 93.30 93.80 77.74 90.23
 Table E.1: Transfer task results of different sentence embedding models (measured as accuracy). : results from
 Reimers and Gurevych (2019); : results from Zhang et al. (2020). We highlight the highest numbers among
 models with the same pre-trained encoder. MLM: adding MLM as an auxiliary task with = 01.
 f
 low/whitening) and find that they both hurt per
formance compared to their base models, showing
 that good uniformity of representations does not
 lead to better embeddings for transfer learning. As
 we argued earlier, we think that transfer tasks are
 not a major goal for sentence embeddings, and thus
 we take the STS results for main comparison.
 F Distribution of Singular Values
 1.0
 1.0
 0.8
 0.6
 0.4
 Normalized Singular Values
 0.2
 0.0
 0
 200
 Index
 Unsupervised models
 0.8
 BERT
 BERT-flow
 BERT-whitening
 SimCSE-BERT
 400
 600
 0.6
 0.4
 0.2
 Normalized Singular Values
 800
 0.0
 SBERT
 SBERT-flow
 SBERT-whitening
 SimCSE-BERT
 0
 200
 400
 Index
 600
 Supervised models
 Figure F.1 shows the singular value distribution of
 SimCSE together with other baselines. For both
 800
 Figure F.1: Singular value distributions of sentence em
bedding matrix from sentences in STS-B. We normal
ize the singular values so that the largest one is 1.
 unsupervised and supervised cases, singular value
 drops the fastest for vanilla BERT or SBERT em
beddings, while SimCSE helps flatten the spectrum
 distribution. Postprocessing-based methods such
 as BERT-flow or BERT-whitening flatten the curve
 even more since they directly aim for the goal of
 mapping embeddings to an isotropic distribution.
 G Cosine-similarity Distribution
 To directly show the strengths of our approaches
 on STStasks, we illustrate the cosine similarity dis
human ratings in Figure G.1. Compared to all the
 baseline models, both unsupervised and supervised
 SimCSE better distinguish sentence pairs with dif
ferent levels of similarities, thus leading to a better
 performance on STS tasks. In addition, we observe
 that SimCSE generally shows a more scattered dis
tribution than BERT or SBERT, but also preserves
 a lower variance on semantically similar sentence
 pairs compared to whitened distribution. This ob
servation further validates that SimCSE can achieve
 a better alignment-uniformity balance.
 tributions of STS-B pairs with different groups of
0-1
 1-2
 2-3
 3-4
 1.00 0.75 0.50 0.25 0.00 0.25 0.50 0.75 1.00
 4-5
 Avg.BERTbase
 0-1
 1-2
 2-3
 3-4
 1.00 0.75 0.50 0.25 0.00 0.25 0.50 0.75 1.00
 4-5
 BERTbase-whitening
 0-1
 1-2
 2-3
 3-4
 1.00 0.75 0.50 0.25 0.00 0.25 0.50 0.75 1.00
 4-5
 UnsupervisedSimCSE-BERTbase
 0-1
 1-2
 2-3
 3-4
 1.00 0.75 0.50 0.25 0.00 0.25 0.50 0.75 1.00
 4-5
 SBERTbase
 0-1
 1-2
 2-3
 3-4
 1.00 0.75 0.50 0.25 0.00 0.25 0.50 0.75 1.00
 4-5
 SBERTbase-whitening
 0-1
 1-2
 2-3
 3-4
 1.00 0.75 0.50 0.25 0.00 0.25 0.50 0.75 1.00
 4-5
 SupervisedSimCSE-BERTbase
 FigureG.1:DensityplotsofcosinesimilaritiesbetweensentencepairsinSTS-B.Pairsaredividedinto5groups
 basedongroundtruthratings(highermeansmoresimilar)alongthey-axis,andx-axisisthecosinesimilarity