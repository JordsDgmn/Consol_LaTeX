CatSight AI: Enhancing Document Search Accuracy and User Interaction through OCR, Vector 
Similarity Search, and LLM-Based Chat Interfaces 
A Thesis Project 
Submitted to 
The Faculty of the Department of Computer Science 
Mindanao State University - Iligan Institute of Technology 
In Fulfillment of the Requirements in CSC198 - Research Method 
Arellano, Carlo P. 
Carnaje, Michael James M. 
Lavesores, Fulgent Kvasir E. 
Proponents 
Professor Dante D. Dinawanao 
Adviser 
` 
Abstract 
The CatSight AI system is designed to address limitations of MSU-IIT’s keyword-based document 
search by leveraging a unified pipeline of OCR, vector embeddings, and an LLM-driven conversational 
interface. The architecture follows a retrieval-augmented generation (RAG) framework: documents 
(scanned or digital) are processed via OCR (ensuring text extraction from scanned or image-based 
documents), segmented into chunks, embedded into vector representations stored in a vector database, 
and then retrieved to support LLM response generation. This integration enables users to issue intuitive 
natural-language queries and receive contextually relevant answers through a chat-based interface. 
In evaluations against the legacy system, CatSight AI achieved higher retrieval accuracy, semantic 
relevance, and efficiency. The hybrid approach substantially improves semantic understanding, 
capturing paraphrases and synonyms (for example, equating “academic calendar” with “term 
schedule”) that the keyword system misses, and retrieves more relevant results than keyword-only 
search. User testing confirmed a marked usability gain: CatSight’s System Usability Scale score 
averaged 77.17%, versus only 50.33% for the existing system. Overall, these results indicate that 
CatSight AI outperforms traditional methods in search accuracy and user experience, offering a more 
accurate, intelligent, and efficient document retrieval solution. 
Keywords:  Document Retrieval System, Optical Character Recognition (OCR), Vector-Based 
Similarity Search, Large Language Model (LLM), Semantic Search 
` 
Table of Contents 
Abstract.....................................................................................................................................................1 
Table of Contents......................................................................................................................................2 
Chapter 1 Research Description.............................................................................................................4 
1.1 Background of the Study..............................................................................................................6 
1.2 Statement of the Problem..............................................................................................................7 
1.3 Research Objective.......................................................................................................................8 
1.3.1 General Objective...............................................................................................................8 
1.3.2 Specific Objective...............................................................................................................8 
1.4. Scope and Limitations of the Research........................................................................................9 
1.5 Significance of the Study..............................................................................................................9 
Chapter 2 Review of Related Literature..............................................................................................10 
2.1 Document and Information Retrieval Systems...........................................................................10 
2.1.1 COIL: Revisit Exact Lexical Match in Information Retrieval with Contextualized 
Inverted List...............................................................................................................................11 
2.2 Embeddings in Document Retrieval...........................................................................................12 
2.2.1 Embedding-based Retrieval in Facebook Search.............................................................13 
2.2.2 RepBERT: Contextualized Text Embeddings for First-Stage Retrieval...........................14 
2.2.3 CLEAR.............................................................................................................................15 
2.2.4 Automatic Document Screening of Medical Literature Using Word and Text 
Embeddings in an Active Learning Setting...............................................................................16 
2.3 Information Extraction and Retrieval from PDF Documents.....................................................17 
2.3.1 BEIR.................................................................................................................................18 
2.3.2 Declarative Experimentation in Information Retrieval using PyTerrier...........................18 
2.4 Large Language Models (LLMs) in Information Retrieval........................................................19 
2.4.1 Large Language Models for Information Retrieval: A Survey........................................21 
2.4.2 Fine-Tuning LLaMA for Multi-Stage Text Retrieval.......................................................22 
2.5 AI-Powered Prompt-Based Information Extraction...................................................................22 
2.5.1 Prompt-Time Symbolic Knowledge Capture with Large Language Models...................24 
2.5.2 ChatUIE: Exploring Chat-based Unified Information Extraction using Large Language 
Models.......................................................................................................................................25 
2.6 Integration of Embeddings and LLMs for Hybrid Retrieval Systems and Retrieval Augmented 
Generation Systems (RAGS)............................................................................................................26 
2.6.1 Leveraging Semantic and Lexical Matching to Improve the Recall of Document 
Retrieval Systems: A Hybrid Approach....................................................................................27 
2.6.2 A Hybrid Retrieval Approach for Advancing Retrieval-Augmented Generation Systems..
 28 
2.6.3 HybridRAG: Integrating Knowledge Graphs and Vector Retrieval Augmented 
Generation for Efficient Information Extraction.......................................................................29 
2.6.4 Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection..........30 
2.6.5 Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models 
through Question Complexity...................................................................................................31 
2.7 LangChain...................................................................................................................................32 
2.7.1 Automating Customer Service with LangChain: A Custom Open-Source GPT Chatbot33 
2.7.2 Generating Breast Ultrasound Reports Using LangChain for Standardized Medical 
Documentation...........................................................................................................................34 
2.7.3 Chatbot Technology in Higher Education: Leveraging LangChain and GPT for 
Internationalization and Digital Transformation.......................................................................35 
2.7.4 A Conversational Agent for Promoting Cultural Awareness in Seoul Using LangChain37 
` 
2.8 Challenges and Limitations........................................................................................................38 
2.9 Future Trends in AI-Powered Document Retrieval....................................................................38 
2.10 Summary of Related Literatures...............................................................................................38 
Chapter 3 Research Methodology........................................................................................................41 
3.1 Process of Document Collection and Preparation......................................................................42 
3.2 Literature Review and System Architecture Design...................................................................42 
3.3 Implementation of the Core Components...................................................................................43 
3.4 Performance Evaluation of the DRS Prototype..........................................................................44 
3.5 Analysis of Evaluation Results and Final Documentation.........................................................45 
Chapter 4  Research Schedule..............................................................................................................46 
Appendix A Bibliography......................................................................................................................47 
Appendix B Personal Vitae...................................................................................................................53 
 
` 
Chapter 1 Research Description 
In today’s era of digital transformation, organizations generate and store an unprecedented volume of 
documents daily. This exponential growth in document storage has created a pressing demand for 
efficient document retrieval systems (DRS) to access, manage, and leverage information effectively. A 
document retrieval system is a specialized application of information retrieval (IR) designed to locate 
relevant documents within vast repositories based on user queries. By enabling quick and accurate 
access to information, DRS plays a pivotal role in knowledge management, informed decision-making, 
and productivity enhancement across diverse domains, including education, business, healthcare, and 
research (Blair, n.d.; Macdonald & Tait, 2020). 
At its core, document retrieval addresses the challenge of identifying stored documents that contain 
pertinent information. The primary objective is to distinguish between relevant and non-relevant 
documents for a user’s specific query. Modern DRS employs various techniques to achieve this, 
ranging from traditional keyword-based methods to advanced machine learning approaches. 
Keyword-based retrieval is a foundational technique that matches user queries to specific keywords 
within documents. While it is straightforward and easy to implement, its reliance on exact matches can 
limit its ability to capture the broader context of queries (Blair, n.d.). Boolean retrieval, an early and 
widely used approach, utilizes logical operators like AND, OR, and NOT to narrow down search 
results based on exact keyword matches. Though simple, it often lacks the flexibility to handle nuanced 
user queries (Macdonald & Tait, 2020). The Vector Space Model (VSM) improves on this by 
representing documents and queries as vectors in a multi-dimensional space, with relevance determined 
by the cosine similarity between these vectors, enabling more precise ranking of results compared to 
Boolean methods (Blair, n.d.). Latent Semantic Analysis (LSA) takes this further by uncovering hidden 
relationships between terms in a document collection through term-document matrix analysis, thereby 
enhancing retrieval accuracy by capturing the semantic meaning of words rather than relying solely on 
exact matches (Macdonald & Tait, 2020). Machine learning-based retrieval techniques, such as support 
vector machines (SVMs), random forests, and deep learning models, dynamically adapt to user 
behavior and context, significantly enhancing retrieval accuracy (Blair, 1984). Neural information 
retrieval systems, leveraging advanced deep learning architectures like recurrent neural networks 
` 
(RNNs) and transformers, model complex language patterns and contextual nuances in documents, 
offering even greater precision and relevance in search results (Macdonald & Tait, 2020). 
A notable advancement in modern DRS is the integration of Retrieval-Augmented Generation (RAG) 
frameworks. RAG combines document retrieval with generative AI models to provide highly 
contextual and human-like responses. This approach retrieves relevant documents from the repository 
and feeds them into generative models, like GPT, which synthesize coherent and informative answers 
to user queries. The RAG framework not only enhances the retrieval process but also bridges the gap 
between static document retrieval and dynamic information synthesis, making it a revolutionary tool in 
data-driven environments (Macdonald & Tait, 2020). 
This research aims to explore the evolving landscape of document retrieval systems, 
emphasizing their significance in transforming data into actionable knowledge. By analyzing advanced 
retrieval techniques and highlighting the role of RAG, this study underscores the pivotal role of DRS in 
fostering innovation and informed decision-making in the digital age. 
1.1 Background of the Study 
Effective management and access to extensive information repositories are crucial for institutions that 
maintain vast collections of documents. Document Retrieval Systems (DRS) are essential tools that 
enable users to efficiently locate specific documents. This study focuses on the Mindanao State 
University – Iligan Institute of Technology (MSU-IIT), which has its own repositories for Special 
Orders, Memorandums, and other important records. MSU-IIT maintains two primary repositories:
 ● Board of Regents (BOR) Resolutions Archive: This repository contains BOR resolutions of 
the MSU System. (Mindanao State University - Iligan Institute of Technology, n.d.-a) 
● IIT Docs: This repository houses Special Orders, Memorandum Orders, and other issuances 
of MSU-IIT. (Mindanao State University - Iligan Institute of Technology, n.d.-b) 
Both repositories utilize keyword-based document search mechanisms. IIT Docs, for instance, is built 
on top of Google Drive and leverages its search capabilities.  
` 
While functional, the current keyword-based approach presents several challenges that limit its 
effectiveness. Keyword searches often fail to account for the context or semantics of user queries, 
leading to inaccurate or irrelevant search results. Users frequently encounter difficulties in locating 
exact documents based on their information needs, particularly when dealing with large or complex 
datasets. This issue is particularly pronounced at MSU-IIT, where reliance on traditional 
keyword-based models highlights significant gaps in accuracy and efficiency. 
In the advent of large language models, the MSU-IIT repository can benefit from enhanced search 
capabilities that understand the context and semantics of user queries, potentially improving the 
precision and efficiency of document retrieval. 
The current system's gap lies in its inability to comprehend the semantic nuances of user queries, 
limiting its effectiveness in handling large or complex datasets. As a result, the system is held back in 
providing a streamlined and user-friendly retrieval process. This inefficiency hinders the institution's 
ability to fully leverage its vast repository of documents, affecting productivity and decision-making 
processes. 
The study was conducted to address these limitations and explore potential solutions to enhance 
document retrieval at MSU-IIT. By investigating advanced approaches such as content-based retrieval 
systems, which will utilize technologies like Optical Character Recognition (OCR), vector embeddings, 
and Large Language Model (LLM)-powered conversational interfaces, the research will aim to 
improve search accuracy, user experience, and overall system efficiency. This initiative will seek to 
bridge the gap between traditional methods and modern technological capabilities, ensuring that 
MSU-IIT can effectively meet the demands of its users and maintain operational excellence. 
1.2 Statement of the Problem 
Traditional title and keyword-based document retrieval systems often struggle to provide accurate, 
efficient, and user-friendly search experiences on a global scale. These systems, which rely heavily on 
` 
exact keyword matches, frequently fail to understand the context, semantics, or synonyms of user 
queries, leading to irrelevant or incomplete search results. This global challenge is also evident at 
MSU-IIT, where implementing advanced retrieval techniques could significantly enhance the efficiency 
of locating pertinent information. By addressing these limitations with modern solutions tailored to the 
institution's unique needs, MSU-IIT has the opportunity to become a model for improving document 
retrieval systems worldwide. 
1.3 Research Objective 
The following are the general and specific objects: 
1.3.1 General Objective 
To develop and evaluate a content-based document retrieval system that integrates Optical Character 
Recognition (OCR), vector embeddings, and Large Language Model (LLM)-powered conversational 
interaction. 
1.3.2 Specific Objective 
1. To collect sample documents from the two repositories of MSU-IIT, namely IIT 
Docs, which contains special orders, memorandum orders and other issuances within 
the MSU-IIT, and Board of Regents(BOR), which contains BOR resolutions for the 
whole MSU system. 
2. To design the architecture of a content-based document retrieval system that 
incorporates OCR for text extraction, vector embeddings for semantic search, and 
LLMs for conversational interaction. 
3. To implement the core components of the proposed system, including OCR 
processing, vector-based similarity search, and an LLM-powered user interface. 
` 
4. To conduct performance evaluations of the proposed system in comparison to 
traditional methods, focusing on search accuracy, user experience, and retrieval 
efficiency. 
5. To analyze and document the results of the evaluation to validate the system's 
effectiveness and provide recommendations for future improvements. 
1.4. Scope and Limitations of the Research 
This study focuses on enhancing the Document Retrieval System (DRS) at Mindanao State University - 
Iligan Institute of Technology (MSU-IIT). The research will involve a sample of 50 PDF documents 
and will be conducted from January 2025 to April 2025, with participants including MSU-IIT students, 
faculty, and staff. A notable limitation of the current system is its inability to analyze images and tables 
within documents, restricting its effectiveness in processing non-textual data. This constraint may 
impact the retrieval accuracy for documents where critical information is presented in these formats. 
By acknowledging this limitation, the study aims to provide a clear understanding of the system's 
current capabilities and identify areas for improvement to effectively meet the institution's document 
retrieval needs. 
1.5 Significance of the Study 
This study holds significant value not only for MSU-IIT students, staff, and faculty but also for other 
institutions and entities that require efficient document storage and retrieval systems. It aims to enhance 
the overall efficiency and effectiveness of managing and accessing documents within an organization. 
` 
Chapter 2 Review of Related Literature 
This chapter explores the foundational principles and advancements in document retrieval systems. It 
examines the traditional title and keyword-based search methods alongside the more sophisticated 
content-based approaches. A comparative analysis is provided, highlighting the strengths, limitations, 
and applications of these systems in addressing the evolving demands of users. By delving into the role 
of OCR, vector embeddings, and LLMs, this review sets the stage for evaluating how content-based 
systems redefine document retrieval processes in terms of accuracy, efficiency, and user satisfaction. 
2.1 
Document and Information Retrieval Systems 
In the modern era of digital transformation, organizations generate and store vast volumes of 
documents daily. This exponential growth in document storage has created an urgent need for efficient 
document retrieval systems (DRS) to access, manage, and utilize information effectively. A document 
retrieval system is a specialized application of information retrieval (IR) focused on locating relevant 
documents from a repository based on user queries. It plays a crucial role in knowledge management, 
decision-making, and enhancing productivity across various domains, including education, business, 
healthcare, and research. 
Document retrieval is the problem of finding stored documents that contain useful 
information. According to Blaire et. al., (n.d.), There exist a set of documents on a range of topics, 
written by different authors, at different times, and at varying levels of depth, detail, clarity, and 
precision, and a set of individuals who, at different times and for different reasons, search for recorded 
information that may be contained in some of the documents in this set. In each instance in which an 
individual seeks information, he or she will find some documents of Ihe set useful and other documents 
not useful; the documents found useful are, we say. relevant; the others, not relevant. In order for a 
person to find all and only the relevant items in a collection of stored documents; one answer is 
automatic full-text retrieval, which on its surface is disarmingly simple: Store the full text of all 
documents in the collection on a computer so that every character of every word in every sentence of 
every document can be located by the machine. Then, when a person wants information from that 
stored collection, the computer is instructed to search for all documents containing certain specified 
words and word combinations, which the user has specified (MacDonald & Tonelleto, 2020). 
` 
2.1.1 COIL: Revisit Exact Lexical Match in Information Retrieval with Contextualized Inverted 
List 
In the realm of information retrieval, traditional systems like BM25 have long relied on exact lexical 
matches, efficiently utilizing inverted list indexes to retrieve documents. However, these systems often 
struggle with vocabulary mismatches and fail to capture the semantic nuances of language. Conversely, 
recent neural information retrieval (IR) models emphasize soft semantic matching across all 
query-document terms, enhancing semantic understanding but at the cost of computational efficiency. 
Addressing this dichotomy, Gao, Dai, and Callan (2021) introduced the Contextualized Inverted List 
(COIL) architecture, which aims to integrate the efficiency of exact lexical matching with the semantic 
depth provided by deep language models. 
COIL innovatively stores contextualized token representations within inverted lists, enabling 
the system to perform exact matches based on the contextual meaning of terms rather than solely on 
their surface forms. This approach allows COIL to leverage the rich semantic information captured by 
deep language models while maintaining the retrieval speed characteristic of traditional inverted index 
structures. By focusing on overlapping query-document tokens' contextualized representations, COIL 
effectively bridges the gap between lexical and semantic matching. Empirical evaluations demonstrate 
that COIL outperforms both classical lexical retrievers and state-of-the-art deep language model 
retrievers, achieving superior retrieval effectiveness with comparable or reduced latency. This 
performance underscores COIL's capability to deliver precise and contextually relevant results without 
compromising on efficiency. 
The introduction of COIL represents a significant advancement in document and information 
retrieval systems. By harmonizing the strengths of exact lexical matching and semantic understanding, 
COIL addresses longstanding challenges such as vocabulary mismatch and semantic ambiguity. Its 
design offers a practical solution for developing retrieval systems that are both effective and efficient, 
making it a valuable reference for researchers and practitioners aiming to enhance retrieval 
performance in various applications. 
` 
2.2 
Embeddings in Document Retrieval 
In the realm of information retrieval, traditional methods have predominantly relied on keyword 
matching, which often falls short in capturing the nuanced meanings inherent in human language. This 
limitation has spurred the development of embedding techniques that represent words, sentences, and 
documents as vectors in high-dimensional space, effectively encoding semantic relationships. By 
transcending the constraints of exact keyword matches, embeddings facilitate a more profound 
understanding of context and intent, thereby significantly enhancing the precision and recall of 
document retrieval systems. 
Embeddings represent words, phrases, or documents as vectors in a continuous vector space, 
enabling systems to measure semantic similarity between textual elements. This representation 
facilitates the retrieval of documents that are contextually relevant, even when there is no exact 
keyword match. For instance, embedding-based retrieval systems can recognize that the terms "car" 
and "automobile" are semantically related, retrieving pertinent documents regardless of the specific 
term used in the query (Mikolov et al., 2013; Devlin et al., 2019). 
Mikolov et al. (2013) introduced word embeddings through the word2vec model, which 
revolutionized natural language understanding by encoding semantic relationships in vector space. 
Later advancements, such as BERT (Devlin et al., 2019), extended this concept by producing 
contextualized embeddings that capture meanings based on surrounding text. These advancements have 
made embedding-based approaches foundational in modern information retrieval, including models 
like RepBERT (Zhan et al., 2020), which demonstrated the effectiveness of embeddings in document 
ranking tasks. 
The integration of embeddings into retrieval systems has led to significant improvements in 
performance. For instance, Huang et al. (2020) implemented embedding-based retrieval in Facebook 
Search, resulting in enhanced search relevance and user satisfaction. Similarly, Zhan et al. (2020) 
introduced RepBERT, a model that represents documents and queries with fixed-length contextualized 
embeddings, achieving state-of-the-art results in initial retrieval tasks. 
The adoption of embedding techniques marks a pivotal advancement in document retrieval, 
enabling systems to move beyond simple keyword matching to a more nuanced understanding of 
` 
language. This evolution has significantly improved the precision and recall of retrieval systems, 
aligning them more closely with human language understanding and enhancing the overall user 
experience. 
2.2.1 Embedding-based Retrieval in Facebook Search 
Facebook Search is a feature that enables users to locate content within the Facebook platform, 
including profiles, pages, groups, posts, and other entities. Unlike traditional web search engines, 
Facebook Search must consider the unique context of each user, such as their social connections and 
personal interactions, to deliver relevant results. This personalized approach leverages the user's social 
graph to enhance the search experience (Huang et al., 2020). 
According to Huang et al., (2020), “historically, Facebook Search relied on Boolean matching 
models, which focus on exact keyword matches. However, this method often failed to capture the 
nuanced meanings and contextual relevance of queries, leading to less satisfactory user experiences”. 
To address these limitations, Facebook implemented Embedding-Based Retrieval (EBR) techniques. 
EBR represents queries and documents as vectors in a continuous vector space, allowing the system to 
measure semantic similarities between them. This approach enables the retrieval of contextually 
relevant information, even when there is no exact keyword match. 
The adoption of EBR in Facebook Search has significantly improved the relevance of search 
results and user satisfaction. By understanding the semantic relationships between queries and 
documents, the system can provide more accurate and personalized results. For instance, if a user 
searches for "apple," the system can discern whether the user is interested in the fruit or the technology 
company based on contextual cues, thereby delivering appropriate results. This advancement aligns 
with the findings of Huang et al. (2020), who reported significant metric gains in online A/B 
experiments after implementing EBR in Facebook Search. 
In summary, the integration of embedding-based retrieval techniques into Facebook Search 
has transformed the platform's ability to deliver semantically relevant and personalized search results, 
thereby enhancing overall user satisfaction. 
` 
2.2.2 RepBERT: Contextualized Text Embeddings for First-Stage Retrieval 
In the realm of information retrieval, traditional first-stage retrieval methods have predominantly relied 
on exact term matching techniques, such as bag-of-words models. While these methods are 
computationally efficient, they often fail to capture the semantic nuances of language, leading to 
suboptimal retrieval performance. To address these limitations, Zhan et al. (2020) introduced 
RepBERT, a model that leverages fixed-length contextualized embeddings to represent both queries 
and documents. By computing the inner products of these embeddings as relevance scores, RepBERT 
effectively captures semantic relationships, thereby enhancing retrieval accuracy. 
According to Zhan, J., et. al (2020), ‘traditional exact term matching methods, such as BM25, 
depend on the presence of identical terms in both queries and documents. This reliance can result in 
missed relevant documents that use synonymous or semantically related terms’. RepBERT addresses 
this issue by encoding the contextual meaning of text into dense vectors, allowing for the recognition of 
semantic similarities even in the absence of exact term matches. For example, RepBERT can identify 
that "car" and "automobile" refer to the same concept, thus retrieving pertinent documents regardless of 
the specific term used in the query. 
In the study by Zhan, J., Mao, J., Liu, Y., Zhang, M., & Ma, S. (2020), RepBERT represents 
documents and queries with fixed-length contextualized embeddings, using their inner products as 
relevance scores. This method achieves state-of-the-art results in initial retrieval tasks, balancing 
effectiveness and efficiency. 
2.2.3 CLEAR 
In information retrieval, traditional lexical models like BM25 rely on exact term matching, which can 
overlook semantic nuances and lead to issues such as vocabulary mismatch. To address these 
limitations, Gao et al. (2020) introduced the Complement Lexical Retrieval Model with Semantic 
Residual Embeddings (CLEAR). CLEAR enhances retrieval performance by integrating semantic 
matching signals from neural embeddings with traditional lexical retrieval methods.  
The information regarding the Complement Lexical Retrieval Model with Semantic Residual 
Embeddings (CLEAR) is sourced from the study by Gao et al. (2020). In their research, they introduce 
` 
CLEAR, a retrieval model that enhances traditional lexical retrieval methods like BM25 by 
incorporating semantic matching signals derived from neural embeddings. This integration is achieved 
through a novel residual-based embedding learning method, which trains the neural embeddings to 
capture language structures and semantics that lexical retrieval models may overlook. Empirical 
evaluations conducted in the study demonstrate that CLEAR outperforms state-of-the-art retrieval 
models, significantly improving both the accuracy and efficiency of reranking pipelines. 
By combining the strengths of lexical and semantic retrieval methods, CLEAR offers a more 
robust solution to the challenges of information retrieval, effectively bridging the gap between exact 
term matching and semantic understanding. 
2.2.4 Automatic Document Screening of Medical Literature Using Word and Text Embeddings in 
an Active Learning Setting 
In Evidence-Based Medicine (EBM), document screening is essential for providing scientific evidence 
to support medical decisions. However, the exponential growth of medical literature has made this task 
increasingly time-consuming and labor-intensive for physicians. To address this challenge, Carvallo et 
al. (2020) investigated the use of word and text embeddings within an active learning framework to 
semi-automate the document screening process. 
Implementing semi-automated screening methods can significantly alleviate the burden on 
healthcare professionals, allowing them to focus more on patient care and critical decision-making. By 
efficiently identifying relevant studies, these methods enhance the quality and timeliness of medical 
evidence synthesis, ultimately leading to improved patient outcomes. Moreover, the integration of 
advanced natural language processing techniques, such as word and text embeddings, enables the 
system to capture complex semantic relationships within the literature, further improving the accuracy 
of the screening process. 
The approach proposed by Carvallo et al. (2020) has practical applications in various medical 
fields, including the development of clinical guidelines, systematic reviews, and meta-analyses. By 
reducing the manual effort required for literature screening, it facilitates the timely incorporation of the 
latest research findings into clinical practice, thereby supporting the continuous advancement of 
healthcare quality. 
` 
2.3  
Information Extraction and Retrieval from PDF Documents 
The Portable Document Format (PDF) is a widely adopted standard for disseminating digital 
documents across various domains, including academia, business, and government. Its design ensures 
consistent presentation across different platforms and devices, encapsulating text, images, and complex 
layouts. However, this fixed-layout nature poses challenges for information extraction and retrieval, as 
the format prioritizes visual fidelity over structural representation. 
The significance of information extraction and retrieval from PDF documents lies in its ability 
to unlock valuable data embedded within these widely used files. By facilitating access to information 
that might otherwise remain obscured, effective PDF data extraction enhances data accessibility 
(Livathinos et al., 2021). Transforming unstructured PDF content into structured data further improves 
search capabilities, allowing users to efficiently locate specific information. This process also supports 
better knowledge management within organizations, enabling them to manage and utilize extracted 
information for informed decision-making and streamlined workflows (Clark et al., n.d). 
The evolution of information extraction and retrieval from PDF documents reflects significant 
technological advancements. Initially, information was manually extracted from PDFs, a 
labor-intensive and error-prone process (Clark et al., n.d.). This was followed by the introduction of 
rule-based systems, which used predefined rules and templates to identify and extract data. While these 
systems provided some automation, they struggled with diverse document layouts and lacked 
scalability. The emergence of machine learning marked a transformative phase, with models capable of 
learning from annotated data, thereby improving extraction accuracy and adaptability to various 
document structures (Palm et al., 2017). More recently, deep learning techniques have revolutionized 
the field by leveraging neural networks to capture complex patterns and relationships within 
documents. These advancements have significantly enhanced the performance of information 
extraction systems, enabling more effective processing of PDF content (Gupta et al., 2018). 
` 
2.3.1 BEIR 
The Benchmarking Information Retrieval (BEIR) dataset is a comprehensive benchmark designed to 
evaluate the zero-shot performance of information retrieval models across a diverse array of tasks and 
domains. Introduced by Thakur et al. (2021), BEIR encompasses 18 publicly available datasets, each 
representing unique retrieval challenges, including fact-checking, question answering, and biomedical 
information retrieval. This diversity enables researchers to systematically assess how well retrieval 
models generalize to new, unseen scenarios without domain-specific training. 
A key feature of BEIR is its facilitation of zero-shot evaluation, where models are tested on 
datasets they were not specifically trained on. This approach provides critical insights into a model's 
out-of-distribution generalization capabilities, reflecting its robustness and applicability in real-world 
situations where annotated data may be scarce. By offering a standardized framework, BEIR allows for 
consistent and fair comparisons among various retrieval systems, including lexical, sparse, dense, 
late-interaction, and re-ranking architectures. 
The significance of BEIR lies in its role as a unifying benchmark that addresses the limitations 
of previous evaluations, which often focused on narrow or homogeneous settings. By encompassing a 
wide range of tasks and domains, BEIR challenges models to perform well across different types of 
retrieval scenarios, thereby promoting the development of more robust and versatile information 
retrieval systems. The benchmark's comprehensive nature encourages the advancement of models 
capable of effective zero-shot retrieval, ultimately contributing to more adaptable and efficient 
information retrieval technologies. 
2.3.2 Declarative Experimentation in Information Retrieval using PyTerrier 
In the field of information retrieval (IR), constructing and evaluating complex retrieval pipelines can be 
a challenging endeavor, often requiring intricate coding and deep system knowledge. To address these 
challenges, Macdonald and Tonellotto (2020) introduced PyTerrier, a Python-based framework that 
facilitates declarative experimentation in IR. PyTerrier enables researchers and practitioners to express 
retrieval pipelines in a manner that closely aligns with their conceptual design, thereby simplifying the 
experimentation process. 
` 
Prior to the development of PyTerrier, the IR community lacked a formalism that allowed for 
the expressive representation of complex retrieval pipelines in high-level programming languages. 
Existing tools often required extensive coding and were not conducive to rapid experimentation or 
reproducibility. Macdonald and Tonellotto identified this gap and proposed PyTerrier as a solution to 
enable declarative experimentation, thereby addressing the need for a more efficient and collaborative 
approach to IR research.  
The significance of PyTerrier lies in its ability to streamline the development and evaluation of 
retrieval systems. By allowing users to construct retrieval pipelines declaratively, PyTerrier reduces the 
complexity associated with traditional procedural programming approaches. This declarative paradigm 
enhances reproducibility in IR research, as experiments can be easily shared and replicated. Moreover, 
PyTerrier's integration with existing IR platforms, such as Anserini and Terrier, enables seamless 
execution and evaluation of retrieval pipelines, fostering collaboration and innovation within the 
research community. 
2.4 
Large Language Models (LLMs) in Information Retrieval 
Large Language Models (LLMs) have significantly advanced the field of Information Retrieval (IR), 
enhancing the ability to extract and retrieve information from complex document formats such as 
PDFs. PDFs are widely used across various domains, including academia, business, and government, 
due to their consistent presentation across platforms and devices. However, their fixed-layout nature 
poses challenges for information extraction and retrieval, as they prioritize visual fidelity over 
structural representation (Meuschke et al., 2023; Parsio, 2023). 
Effectively extracting and retrieving information from PDFs is crucial for several reasons. 
Unlocking the data embedded within PDFs facilitates access to valuable information that might 
otherwise remain obscured (Meuschke et al., 2023). Transforming unstructured PDF content into 
structured data improves search capabilities, enabling users to locate specific information efficiently 
(Feng et al., 2024). Additionally, organizations can better manage and utilize extracted information for 
informed decision-making and streamlined workflows (Parsio, 2023). 
The process of extracting information from PDFs has evolved significantly. Initially, manual 
extraction was labor-intensive and prone to errors (Clark et al., 2009). Rule-based systems followed, 
` 
utilizing predefined rules and templates to automate the process, but they struggled with diverse 
document layouts (Palm et al., 2017). The advent of machine learning introduced models capable of 
learning from annotated data, improving accuracy and adaptability (Gupta et al., 2018). More recently, 
deep learning techniques, particularly neural networks, have revolutionized the field by capturing 
complex patterns and relationships within documents (Livathinos et al., 2021). 
LLMs, such as GPT models, have further revolutionized IR by enabling a more sophisticated 
understanding of natural language. Their ability to comprehend context, disambiguate queries, and 
generate coherent responses has significantly improved search relevance and user satisfaction. For 
example, LLMs can interpret nuanced queries and retrieve information that closely aligns with user 
intent, even in the absence of exact keyword matches (Zhu et al., 2023). They also facilitate 
conversational search, personalized retrieval, and cross-lingual information retrieval, broadening access 
to information and enhancing user experiences (Feng et al., 2024). 
As LLMs continue to evolve, their role in IR is expected to expand, leading to more intuitive 
and effective systems for handling the complexities of various document formats, including PDFs. 
Their integration into IR technologies holds the promise of significantly advancing data accessibility, 
searchability, and knowledge management across numerous applications. 
2.4.1 Large Language Models for Information Retrieval: A Survey 
Large Language Models (LLMs) have significantly enhanced Information Retrieval (IR) systems by 
improving components such as query rewriting, retrieval, reranking, and reading. Zhu et al. (2023) 
provide a comprehensive survey on this integration, highlighting the transformative impact of LLMs on 
IR. 
The incorporation of LLMs into IR systems offers several key advantages. LLMs can interpret 
complex and nuanced user queries, capturing semantic meanings beyond simple keyword matching, 
leading to more accurate retrieval of relevant documents as they understand the intent behind queries. 
By generating contextual embeddings, LLMs facilitate the retrieval of documents that align more 
closely with user intent, even when exact keyword matches are absent, enhancing the relevance of 
search results. Additionally, LLMs can assess and reorder retrieved documents based on a deeper 
understanding of content relevance, improving the precision of top-ranked results. They can also 
` 
generate coherent and informative responses by synthesizing information from multiple documents, 
providing users with concise and comprehensive answers. 
The integration of LLMs into IR systems has led to various practical applications. LLMs 
enable the development of search systems that support natural language interactions, allowing users to 
engage in dialogue-based queries and receive contextually relevant responses. By understanding user 
preferences and context, LLMs can tailor search results to individual users, enhancing the 
personalization of information retrieval. Their multilingual capabilities facilitate the retrieval of 
information across different languages, broadening access to diverse information sources. Moreover, 
LLMs can be fine-tuned for specific domains, improving the retrieval of specialized information in 
areas such as healthcare, finance, and law. 
Despite their advantages, integrating LLMs into IR systems presents challenges. LLMs 
require large amounts of data for training, and in specialized domains, such data may be limited, 
affecting model performance. The complex nature of LLMs can make it difficult to interpret how they 
arrive at specific results, posing challenges for transparency and trust. Deploying LLMs demands 
significant computational power, which may not be feasible for all organizations. Addressing these 
challenges is crucial for the effective integration of LLMs into IR systems, ensuring they enhance user 
experience and information accessibility. 
2.4.2 Fine-Tuning LLaMA for Multi-Stage Text Retrieval 
Text retrieval is crucial in various natural language comprehension tasks, including web search, 
open-domain question answering, and fact verification. Retrieval also plays an important role in 
enhancing the effectiveness of large language models (LLMs) in a retrieval-augmented generation 
(RAG) pipeline. This approach not only mitigates hallucinations but also enables LLMs to access 
external knowledge (Ma, X., Wang, L., Yang, N., Wei, F., & Lin, J., 2024). 
According to Ma, X., Wang, L., Yang, N., Wei, F., & Lin, J. (2024), “Recent LLMs with 
billions of parameters such as GPT-4 and LLaMA have exhibited extraordinary capabilities in many 
NLP tasks, surpassing previous smaller models. For retrieval, recent methods such as RankGPT, LRL, 
and PRP have explored prompting LLMs to perform zero-shot listwise or pairwise ranking as text 
generation tasks. 
` 
This study by Ma et al. (2024) investigates the fine-tuning of the LLaMA model for 
multi-stage text retrieval. The multi-stage approach allows for initial coarse retrieval followed by 
increasingly refined reranking steps, leveraging the advanced capabilities of LLaMA. By integrating 
fine-tuned LLaMA into this process, the study aims to enhance retrieval effectiveness, particularly in 
scenarios requiring deep contextual understanding and ranking precision. 
2.5 
AI-Powered Prompt-Based Information Extraction 
AI-powered prompt-based information extraction has revolutionized the retrieval of specific data points 
from extensive text corpora. By leveraging Large Language Models (LLMs) through carefully 
designed prompts, this approach enables efficient extraction of structured information from 
unstructured text (Xu et al., 2023). This methodology is particularly beneficial in scenarios where 
traditional information extraction methods may falter due to the complexity or variability of the text 
(Çöplü et al., 2024). 
The significance of prompt-based information extraction lies in its flexibility and adaptability. 
Unlike rule-based systems that require extensive manual effort to create and maintain, prompt-based 
techniques can be quickly tailored to new tasks or domains by modifying the prompts provided to the 
AI model (Xu et al., 2024). This adaptability reduces the time and resources needed to develop 
information extraction systems for diverse applications (Do et al., 2024). 
In practical applications, prompt-based information extraction has been employed in various 
fields. For instance, in the legal domain, it assists in extracting pertinent case details from legal 
documents, thereby streamlining the research process (Xu et al., 2023). In healthcare, it facilitates the 
extraction of patient information from medical records, enhancing data accessibility for clinical 
decision-making (Wei et al., 2023). Moreover, in business intelligence, it aids in mining insights from 
financial reports and market analyses, supporting strategic planning (Xu et al., 2023). 
However, the effectiveness of this approach is highly dependent on the design of the prompts. 
Crafting effective prompts requires a deep understanding of both the AI model's capabilities and the 
specific information extraction task. Well-designed prompts can guide the model to produce accurate 
and relevant outputs, while poorly constructed prompts may lead to incomplete or incorrect 
information extraction (Çöplü et al., 2024; Do et al., 2024). 
` 
In summary, AI-powered prompt-based information extraction offers a flexible and efficient 
solution for retrieving specific data from large text collections. Its adaptability makes it suitable for a 
wide range of applications, provided that careful attention is given to prompt design to ensure the 
accuracy and relevance of the extracted information (Wei et al., 2023). 
2.5.1 Prompt-Time Symbolic Knowledge Capture with Large Language Models 
In their 2024 study, Çöplü et al. address a critical challenge in the deployment of Large Language 
Models (LLMs) for personalized applications: the models' inherent inability to capture and utilize 
user-specific knowledge provided during interactions. This limitation hampers the development of AI 
systems, such as personal assistants, that require the integration of individual user information to 
function effectively. To tackle this issue, the authors propose a method for prompt-driven symbolic 
knowledge capture, focusing on the extraction of subject-predicate-object triples from user prompts to 
construct knowledge graphs. 
The researchers explored three approaches to Prompt-to-Triple (P2T) generation to capture 
symbolic knowledge from prompts effectively. The first approach, Zero-Shot Prompting, leverages the 
Large Language Model's (LLM) pre-existing knowledge to generate triples without requiring additional 
training. The second, Few-Shot Prompting, involves providing the model with a limited number of 
examples to guide the generation process, helping the model better understand the task. Finally, 
Fine-Tuning adjusts the model's parameters through training on a specialized dataset, significantly 
improving its ability to extract accurate triples. To evaluate these methods, the authors created a 
synthetic dataset specifically designed to assess the performance of each approach in capturing 
symbolic knowledge from user prompts. 
The study's experiments reveal that fine-tuning the LLM yields the most accurate and reliable 
results in P2T generation, outperforming both zero-shot and few-shot prompting techniques. This 
indicates that while LLMs possess some capacity for symbolic knowledge extraction through 
in-context learning, their performance significantly improves when fine-tuned on relevant data. 
This research contributes to the field by demonstrating effective strategies for enabling LLMs 
to capture and utilize user-specific knowledge during interactions. The findings suggest that fine-tuning 
LLMs can substantially enhance their ability to integrate personal information, thereby improving the 
` 
functionality of AI systems that depend on personalized data. This advancement is particularly relevant 
for developing AI applications that require a deep understanding of individual user contexts to provide 
tailored and accurate responses. 
2.5.2 ChatUIE: Exploring Chat-based Unified Information Extraction using Large Language 
Models 
As Large Language Models (LLMs) continue to revolutionize natural language processing (NLP), their 
ability to perform diverse tasks, including conversational AI and information extraction, has 
significantly advanced. However, their capacity to extract structured information from complex, 
domain-specific text remains a challenge, particularly in scenarios involving ambiguous or 
schema-independent data. To address this gap, Xu et al. (2024) introduced ChatUIE, a unified 
information extraction framework that builds upon conversational LLM architectures. 
In their 2024 study, Xu et al. introduce ChatUIE, a unified information extraction framework 
built upon ChatGLM, designed to address the limitations of Large Language Models (LLMs) in 
domain-specific information extraction tasks. While LLMs have demonstrated impressive performance 
in general conversational contexts, they often struggle with extracting structured information from 
natural language, especially when it deviates from known schemas or instructions. 
ChatUIE employs reinforcement learning to enhance and align various tasks, particularly 
those involving confusing and limited samples. Additionally, it integrates generation constraints to 
prevent the inclusion of elements not present in the input, thereby improving the accuracy of the 
extracted information. Experimental results indicate that ChatUIE significantly improves the 
performance of information extraction tasks, with only a slight decrease in general conversational 
abilities. 
This study contributes to the field by providing a framework that effectively combines the 
conversational strengths of LLMs with enhanced capabilities for domain-specific information 
extraction. By addressing the challenges associated with extracting structured information from diverse 
natural language inputs, ChatUIE offers a promising solution for applications requiring precise 
information extraction across various domains. 
` 
2.6 
Integration of Embeddings and LLMs for Hybrid Retrieval Systems and Retrieval 
Augmented Generation Systems (RAGS) 
The integration of embeddings and Large Language Models (LLMs) has led to the development of 
hybrid retrieval systems that combine the strengths of semantic understanding and contextual 
generation, enhancing the retrieval of relevant information from extensive document collections (Kuzi 
et al., 2020). 
Embeddings are vector representations of text that capture semantic meanings, enabling the 
comparison of textual elements based on their contextual similarities (Sarmah et al., 2024). Dense 
embeddings, derived from neural networks, facilitate semantic searches by identifying related concepts 
even when exact keyword matches are absent. Conversely, sparse embeddings focus on exact term 
matches, emphasizing the presence or absence of specific words (Yoon et al., 2023). 
LLMs, such as GPT-4, are trained on vast datasets to understand and generate human-like text. 
Their ability to comprehend context and generate coherent responses makes them valuable in 
information retrieval tasks, especially when dealing with complex queries that require nuanced 
understanding (Doan et al., 2024). 
Hybrid retrieval systems combine dense and sparse retrieval methods to leverage the 
advantages of both. By integrating embeddings with LLMs, these systems can perform semantic 
searches while also considering the contextual relevance of documents. This combination enhances the 
retrieval process by capturing both the exactness of term matching and the depth of semantic 
understanding (Bruch et al., 2022). 
The integration of embeddings and LLMs in hybrid retrieval systems has significantly 
improved the efficiency and accuracy of document retrieval. These systems can handle diverse and 
complex queries, providing more relevant results and improving user satisfaction. In the modern world, 
where information is abundant and varied, such systems are crucial for effective data access and 
utilization (Kuzi et al., 2020). 
` 
2.6.1 Leveraging Semantic and Lexical Matching to Improve the Recall of Document Retrieval 
Systems: A Hybrid Approach 
Kuzi et al. (2020) propose a hybrid retrieval approach that combines semantic matching via deep neural 
networks with traditional lexical methods. This integration aims to enhance recall by capturing both 
exact term matches and broader semantic relationships. 
In their 2020 study, Kuzi et al. address the limitations of traditional lexical-based retrieval 
models, such as BM25, which depend on exact keyword matching and may overlook relevant 
documents that use synonymous or semantically related terms. To overcome these limitations, they 
propose a hybrid retrieval approach that combines semantic matching, utilizing deep neural networks, 
with traditional lexical methods. This integration aims to enhance recall by capturing both exact term 
matches and broader semantic relationships (Kuzi et al., 2020). 
The researchers conducted parallel retrieval processes using both semantic and lexical models.  
The semantic component employed a deep neural network trained to understand complex word 
relationships, enabling it to identify relevant documents even when there was no direct keyword 
overlap with the query (Kuzi et al., 2020). The lexical component relied on traditional keyword 
matching techniques. The results from both models were then merged to form an initial set of 
documents for re-ranking. 
An empirical evaluation using a publicly available TREC collection demonstrated that the 
semantic retrieval model could retrieve relevant documents not identified by the lexical model. This 
indicates that the two approaches are complementary, with the hybrid model achieving higher recall 
than either method alone. The study also found that relevant documents retrieved by the semantic 
model often exhibited different characteristics compared to those retrieved by the lexical model, 
underscoring the value of combining both methods. 
This study provides valuable insights into the benefits of integrating semantic and lexical 
matching techniques in document retrieval systems. By demonstrating that a hybrid approach can 
improve recall and retrieve a more diverse set of relevant documents, it offers a compelling case for the 
adoption of such models in information retrieval research and practice. The findings suggest that 
leveraging the strengths of both semantic understanding and exact term matching can lead to more 
` 
effective retrieval systems, particularly in scenarios where relevant information may be expressed using 
varied terminology. 
2.6.2 A Hybrid Retrieval Approach for Advancing Retrieval-Augmented Generation Systems 
In their 2024 study, Doan et al. address the limitations of Retrieval-Augmented Generation (RAG) 
systems, particularly the challenge of "hallucination"—where models generate responses not grounded 
in factual data—due to knowledge boundaries and outdated information. They propose a hybrid 
retrieval method that integrates embeddings from both textual data and knowledge graphs to enhance 
the retriever component of RAG systems. 
The authors' approach involves combining text embeddings with knowledge graph 
embeddings to capture both the semantic content of passages and the relationships between them. This 
integration aims to improve the retriever's ability to select relevant information, thereby providing the 
Large Language Model (LLM) with accurate and contextually appropriate data for response generation. 
Notably, their method does not require complex joint learning processes, making it more 
straightforward to implement. 
Evaluations on custom test sets demonstrate that this hybrid retrieval approach significantly 
enhances the accuracy and ranking capabilities of the retriever component (Doan et al., 2024). As a 
result, the LLM-based reader generates more precise and reliable responses, effectively reducing 
instances of hallucination. This highlights the potential of the hybrid approach to address critical 
challenges in RAG systems (Doan et al., 2024). 
This study contributes to the field by offering a practical solution to improve the factual 
accuracy of RAG systems without necessitating extensive fine-tuning or complex training procedures. 
By leveraging both textual and structured data through knowledge graphs, the proposed method 
provides a more holistic understanding of the information landscape, which is crucial for applications 
requiring up-to-date and domain-specific knowledge. 
` 
2.6.3 HybridRAG: Integrating Knowledge Graphs and Vector Retrieval Augmented Generation 
for Efficient Information Extraction 
In their 2024 study, Sarmah et al. introduce HybridRAG, a novel framework that integrates Knowledge 
Graphs (KGs) with vector-based Retrieval-Augmented Generation (RAG) techniques to enhance 
information extraction from unstructured financial documents, such as earnings call transcripts. This 
approach addresses challenges like domain-specific terminology and complex document formats, 
which often hinder the effectiveness of Large Language Models (LLMs) in financial applications. 
HybridRAG combines two complementary retrieval strategies to enhance information 
extraction. The first, VectorRAG, utilizes vector databases to retrieve semantically relevant textual 
information, which aids Large Language Models (LLMs) in generating contextually appropriate 
responses. The second, GraphRAG, employs Knowledge Graphs to capture structured relationships 
between entities, providing a deeper and more nuanced understanding of the data's context. By 
integrating these two approaches, HybridRAG retrieves context from both vector databases and 
knowledge graphs, enabling LLMs to generate accurate, contextually relevant, and well-informed 
answers. 
Experiments conducted on financial earnings call transcripts, which naturally contain 
question-answer pairs, demonstrate that HybridRAG outperforms traditional VectorRAG and 
GraphRAG techniques individually. Evaluations at both the retrieval and generation stages show 
improvements in retrieval accuracy and the quality of generated answers. 
This study highlights the potential of combining unstructured and structured data retrieval 
methods to enhance the performance of LLMs in complex domains like finance. By leveraging the 
strengths of both vector-based retrieval and knowledge graphs, HybridRAG offers a more 
comprehensive approach to information extraction, which can be applied beyond the financial sector to 
other fields requiring precise and context-aware data retrieval. 
2.6.4 Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection 
Large Language Models (LLMs) have demonstrated remarkable capabilities across various natural 
language processing tasks. However, their reliance solely on internal parametric knowledge often leads 
` 
to factual inaccuracies in generated responses. To address this limitation, Asai et al. (2023) introduced 
Self-Reflective Retrieval-Augmented Generation (Self-RAG), a framework that enhances LLMs' 
factual accuracy and overall response quality by integrating on-demand retrieval and self-reflection 
mechanisms. 
Self-RAG operates by training an LLM to perform three key functions: retrieve relevant 
information, generate responses, and critique its outputs. This process is facilitated through the use of 
special "reflection tokens" that signal when to initiate retrieval and when to assess the quality of 
generated content. Upon receiving an input prompt, the model determines the necessity of external 
information. If additional data is required, it retrieves pertinent passages and incorporates them into the 
response generation process. Subsequently, the model evaluates its output, identifying and rectifying 
any factual inconsistencies or errors. 
Empirical evaluations across diverse tasks—including open-domain question answering, 
reasoning, and fact verification—demonstrate that Self-RAG significantly outperforms existing LLMs 
and retrieval-augmented models. Notably, Self-RAG exhibits superior performance compared to 
models like ChatGPT and retrieval-augmented Llama2-chat, particularly in enhancing factual accuracy 
and citation precision in long-form text generation. 
The introduction of Self-RAG marks a substantial advancement in the field of 
retrieval-augmented generation. By enabling LLMs to dynamically retrieve information and critically 
assess their outputs, Self-RAG effectively mitigates issues related to factual inaccuracies. This 
approach not only bolsters the reliability of LLM-generated content but also preserves the models' 
versatility across various applications. The framework's emphasis on self-reflection and adaptive 
retrieval sets a new precedent for developing more accurate and trustworthy AI language models. 
2.6.5 Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through 
Question Complexity 
Large Language Models (LLMs) have significantly advanced natural language processing tasks, 
particularly in question-answering (QA) systems. However, their reliance on internal parametric 
knowledge can lead to inaccuracies, especially when handling queries of varying complexities. To 
` 
address this challenge, Jeong et al. (2024) introduced Adaptive-RAG, a novel framework that 
dynamically adjusts retrieval-augmented generation strategies based on the complexity of user queries.  
The methodology of Adaptive-RAG centers on a classifier—a smaller language 
model—trained to predict the complexity level of incoming queries. This classifier utilizes 
automatically collected labels derived from actual model predictions and inherent dataset biases to 
evaluate query complexity. Based on the assessed complexity, the system dynamically selects the most 
suitable retrieval strategy. For straightforward queries that can be answered using the LLM's internal 
knowledge, the system opts for no retrieval, bypassing the need for external data. For moderately 
complex queries requiring minimal external information, it employs single-step retrieval. For intricate, 
multi-hop queries necessitating iterative reasoning and extensive data, the system adopts multi-step 
retrieval. This adaptive approach ensures that each query is processed with optimal efficiency and 
accuracy, minimizing computational overhead for simple queries while delivering thorough and precise 
responses for complex ones. 
Evaluations on open-domain QA datasets with varying query complexities demonstrated that 
Adaptive-RAG enhances both efficiency and accuracy compared to existing baselines, including other 
adaptive retrieval methods. The framework effectively balances the trade-off between computational 
resources and response quality, adapting seamlessly to the demands of each query. 
Adaptive-RAG represents a significant advancement in retrieval-augmented generation by 
introducing a dynamic, complexity-aware approach to query processing. By tailoring retrieval 
strategies to query complexity, it optimizes resource utilization and improves response accuracy. This 
framework offers a scalable solution adaptable to various QA systems, enhancing their ability to handle 
a diverse range of user queries effectively. 
2.7 
LangChain 
LangChain is an open-source framework designed to facilitate the development of applications 
powered by Large Language Models (LLMs), offering a suite of tools and integrations that enhance the 
capabilities of LLMs in various contexts (Wang et al., 2022). One of its primary features is the support 
for Retrieval-Augmented Generation (RAG), a technique that combines LLMs with external data 
retrieval to produce more accurate and contextually relevant outputs (LangChain Team, 2022). This 
` 
approach is particularly beneficial in scenarios where up-to-date or domain-specific information is 
crucial (LangChain Team, 2022). 
In the realm of document and information retrieval systems, LangChain provides robust 
mechanisms for integrating LLMs with retrieval components (Wang et al., 2022). It offers abstractions 
for document loaders, embeddings, and vector stores, enabling the construction of semantic search 
engines that can retrieve and process information from extensive text corpora (LangChain Team, 2022). 
This integration allows for the development of sophisticated question-answering systems and chatbots 
capable of accessing and utilizing external knowledge sources effectively (LangChain Team, 2022). 
Moreover, LangChain's architecture supports the creation of complex retrieval pipelines, 
including multi-step retrieval processes and conversational interactions (Wang et al., 2022). By 
leveraging its comprehensive set of tools and integrations, developers can build applications that not 
only generate responses but also ground them in factual and up-to-date information, thereby enhancing 
the reliability and relevance of the outputs (LangChain Team, 2022). 
In summary, LangChain serves as a versatile framework that bridges the gap between LLMs 
and information retrieval systems, empowering developers to create applications that effectively 
combine the generative capabilities of LLMs with the precision of retrieval mechanisms (Wang et al., 
2022). This synergy is essential for advancing the performance and applicability of document and 
information retrieval systems in various domains (LangChain Team, 2022). 
2.7.1 Automating Customer Service with LangChain: A Custom Open-Source GPT Chatbot 
In the era of digital transformation, organizations increasingly rely on advanced technologies to 
enhance customer service efficiency and user satisfaction. Traditional methods, such as static 
Frequently Asked Questions (FAQs), often fail to meet the dynamic and diverse needs of users. To 
address these limitations, Pandya and Holia (2023) proposed Sahaay, a custom open-source chatbot 
framework powered by LangChain and Large Language Models (LLMs). Sahaay aims to revolutionize 
customer service by providing real-time, personalized, and context-aware support. 
` 
The development of Sahaay involves several key components. First, data collection is 
achieved through web scraping techniques to gather comprehensive and up-to-date information from 
organizational websites, ensuring the chatbot has a robust knowledge base. Second, embeddings and 
language models play a pivotal role, with textual data represented using embeddings and knowledge 
retrieval facilitated by Google's Flan T5 models (XXL, Base, and Small). These models enable Sahaay 
to generate accurate and contextually relevant responses. Finally, integration with customer service 
platforms ensures seamless embedding of the chatbot into existing support infrastructures, allowing for 
real-time query resolution and enhanced user interaction. This multi-faceted approach equips Sahaay to 
handle diverse queries effectively while aligning with organizational needs. 
According to Pandya, S., & Holia, R. (2023), the implementation of Sahaay within an 
educational institution demonstrated its capability to handle diverse queries from prospective and 
current students, as well as researchers. The chatbot effectively provided information on topics such as 
notice board updates and potential research guides, showcasing its versatility and responsiveness. 
This study contributes to the field of document and information retrieval systems by 
illustrating how integrating LLMs with open-source tools like LangChain can revolutionize customer 
service. By moving beyond static FAQs to dynamic, personalized interactions, organizations can 
enhance customer satisfaction and engagement. The research underscores the potential for scalable 
solutions across various industries, paving the way for more responsive and efficient customer service 
ecosystems. 
2.7.2 Generating Breast Ultrasound Reports Using LangChain for Standardized Medical 
Documentation 
Medical imaging plays a critical role in the early detection and diagnosis of various conditions, 
including breast cancer. Breast ultrasound (BUS), as a non-invasive imaging technique, is widely used 
for its ability to identify abnormalities in breast tissue. However, generating detailed and standardized 
medical reports from BUS images is a labor-intensive process that places significant demands on 
radiologists. To address these challenges, Huh, Park, and Ye (2023) propose an innovative system 
leveraging LangChain and Large Language Models (LLMs) to automate the generation of BUS reports. 
` 
Their approach focuses on enhancing efficiency, consistency, and quality in medical documentation by 
integrating multiple image analysis tools within the LangChain framework. 
The proposed system employs a combination of designated tools and LLM-powered text 
generation within LangChain to extract relevant features from BUS images. These features are then 
contextualized within a clinical framework to produce comprehensive and standardized medical reports 
(Huh et al., 2023). According to Huh et al. (2023), by automating the traditionally manual process of 
feature extraction and interpretation, this approach reduces the workload on radiologists while ensuring 
uniformity in the generated reports. 
Extensive experiments conducted by the authors demonstrate that the integrated tools deliver 
significant improvements in both qualitative and quantitative metrics. Clinical evaluations confirm the 
clinical utility of the generated reports, highlighting their alignment with diagnostic needs and their 
potential for practical application in real-world healthcare settings (Huh et al., 2023). 
This study is a significant contribution to the field of medical imaging and documentation. By 
leveraging LangChain and LLMs, the authors present a scalable solution that integrates multiple image 
analysis tools for automated report generation. This advancement not only enhances the efficiency of 
diagnostic workflows but also ensures standardized documentation, which is critical for improving 
patient care outcomes (Huh et al., 2023). Furthermore, the approach outlined in this study demonstrates 
the adaptability of LangChain for other medical imaging modalities, providing a foundation for further 
innovations in healthcare technology. 
2.7.3 Chatbot Technology in Higher Education: Leveraging LangChain and GPT for 
Internationalization and Digital Transformation 
The internationalization of higher education institutions (HEIs) necessitates innovative approaches to 
support a diverse student body effectively. Traditional student support services often face challenges in 
scalability and personalization, particularly for international students who may encounter language 
barriers and cultural differences. In response to these challenges, Hsain and El Housni (2024) explore 
the integration of advanced chatbot technology powered by GPT-3.5 and GPT-4 Turbo to enhance 
student engagement and information access. Their research focuses on leveraging Large Language 
` 
Models (LLMs) to facilitate digital transformation in higher education, aiming to provide real-time, 
personalized support that aligns with the needs of a global student population. 
The study employs a comprehensive technological stack, including Python 3, GPT API, 
LangChain, and Chroma Vector Store, to develop a chatbot capable of delivering context-aware and 
accurate responses. A critical component of the development process is the creation of a high-quality, 
timely, and relevant transcript dataset, which serves as the foundation for training and testing the 
chatbot's performance. This dataset encompasses a wide range of topics pertinent to international 
students, ensuring that the chatbot can address diverse queries effectively. 
Evaluation of the chatbot's performance indicates a high level of efficacy in providing 
comprehensive and relevant responses. User feedback suggests a preference for the chatbot over 
traditional support methods, citing its ability to engage in real-time interactions and maintain 
conversational memory, which enhances the overall user experience. Additionally, the chatbot 
demonstrates a low error rate, further validating its reliability as a tool for student support. 
This study contributes to the field of educational technology by demonstrating the potential of 
LLM-powered chatbots to transform student support services in HEIs. By facilitating real-time, 
personalized interactions, such chatbots can significantly improve accessibility and satisfaction among 
international students. The research underscores the importance of digital transformation in higher 
education and provides a framework for integrating advanced AI technologies to meet the evolving 
needs of a diverse student body. 
2.7.4 A Conversational Agent for Promoting Cultural Awareness in Seoul Using LangChain 
Promoting cultural awareness among visitors is essential for preserving and appreciating a city's 
heritage. In Seoul, a city rich in historical sites, effectively disseminating information about these 
landmarks can enhance tourists' experiences and foster a deeper understanding of Korean culture. To 
address this need, Suh, Kwak, Kim, and Cho (2024) developed a conversational agent designed to 
provide accessible and accurate information about Seoul's historical sites. This agent leverages 
LangChain, a framework for building applications powered by large language models (LLMs), to 
deliver contextually relevant responses to user inquiries. 
` 
The development of the conversational agent involved several key components that ensured its 
functionality and user engagement. First, data collection was conducted using information provided by 
the Seoul Metropolitan Government, guaranteeing the dataset was authoritative, up-to-date, and rich 
with details about various historical sites, their significance, and their locations. Next, framework 
implementation utilized LangChain to integrate multiple language models and tools, enabling the agent 
to process and generate natural language responses effectively. This framework facilitated the seamless 
combination of different models, enhancing the agent's conversational capabilities. Finally, user 
interface development was achieved using Streamlit, an open-source app framework that provided an 
interactive and user-friendly platform. This design allowed users to engage effortlessly with the agent, 
receiving accurate and contextually relevant information in a conversational manner. 
Despite the limited volume of data, the conversational agent consistently delivered reliable 
and accurate responses aligned with the available information. The system effectively increased 
awareness among visitors unfamiliar with Seoul's cultural heritage, providing precise locations and 
historical context for various sites. The use of LangChain enabled the agent to handle diverse queries, 
demonstrating its versatility in managing complex conversational scenarios. 
This study highlights the potential of integrating LLM frameworks like LangChain with 
conversational agents to promote cultural heritage. By providing accessible information through natural 
language interactions, such systems can enhance tourists' experiences and contribute to cultural 
preservation. The research also underscores the importance of utilizing authoritative data sources and 
user-friendly interfaces to ensure the effectiveness of conversational agents in real-world applications. 
2.8 
Challenges and Limitations 
Despite advancements, challenges persist in document retrieval systems, including handling ambiguous 
queries, ensuring scalability, and maintaining the interpretability of complex models. Balancing 
precision and recall remains a critical concern, especially when integrating neural embeddings and 
LLMs 
` 
2.9 Future Trends in AI-Powered Document Retrieval 
Future trends point towards deeper integration of LLMs and embeddings, development of more robust 
hybrid models, and enhanced capabilities in zero-shot and few-shot learning scenarios. Emphasis on 
ethical considerations and transparency in AI-powered retrieval systems is also expected to grow. 
 
2.10 Summary of Related Literature 
Study 
Documen
 t and 
Informati
 on 
Retrieval 
Systems 
Embeddi
 ngs in 
Documen
 t 
Retrieval 
Informati
 on 
Extractio
 n and 
Retrieval 
from PDF 
Documen
 ts 
Large 
Language 
Models 
(LLMs) 
in 
Informati
 on 
Retrieval 
AI-Power
 ed 
Prompt-B
 ased 
Informati
 on 
Extractio
 n 
Integratio
 n of 
Embeddi
 ngs and 
LLMs for 
Hybrid 
Retrieval 
Systems 
and 
RAGS 
LangChai
 n 
Gao, L., Dai, Z., 
& Callan, J. 
(2021) 
✔ ✔      
Devlin, J., 
Chang, M. W., 
Lee, K., & 
Toutanova, K. 
(2019) 
✔ ✔  ✔    
Huang, P.-S., et 
al. (2020) 
✔ ✔    ✔  
Zhan, J., Mao, ✔ ✔      
` 
J., Liu, Y., 
Zhang, M., & 
Ma, S. (2020) 
Carvallo, A., 
Parra, D., Lobel, 
H., & Soto, A. 
(2020) 
 ✔ ✔     
Thakur, N., 
Reimers, N., 
Rücklé, A., 
Srivastava, A., 
& Gurevych, I. 
(2021) 
✔ ✔      
Macdonald, C., 
& Tonellotto, N. 
(2020) 
✔       
Feng, J., Tao, C., 
et al. (2024) 
✔   ✔ ✔ ✔  
Çöplü, T., et al. 
(2024) 
  ✔ ✔ ✔   
Xu, J., et al. 
(2024) 
✔ ✔ ✔ ✔ ✔  ✔ 
Doan, N. N., et 
al. (2024) 
✔ ✔  ✔ ✔ ✔ ✔ 
Kuzi, S., et al. 
(2020) 
✔ ✔  ✔  ✔  
Sarmah, B., et 
al. (2024) 
✔ ✔  ✔  ✔  
` 
Table 1. Summary Features of Related Literature 
 
 
 
 
 
 
 
 
Asai, A., et al. 
(2023) 
✔   ✔  ✔  
Jeong, S., et al. 
(2024) 
✔ ✔  ✔  ✔  
Wang, J., et al. 
(2022) 
✔ ✔  ✔ ✔ ✔ ✔ 
Pandya, S., & 
Holia, R. (2023) 
   ✔ ✔  ✔ 
Huh, S., Kim, J., 
& Park, S. H. 
(2023) 
  ✔ ✔ ✔  ✔ 
Hsain, F., & El 
Housni, Z. 
(2024) 
   ✔ ✔  ✔ 
Suh, J., Lee, Y., 
& Park, M. 
(2024) 
   ✔ ✔  ✔ 
Proposed 
System 
✔ ✔ ✔ ✔ ✔ ✔ ✔ 
` 
Chapter 3 Research Methodology 
This chapter outlines the systematic methodology employed to develop CatSight AI, a document 
retrieval system (DRS) designed to enhance search accuracy and user interaction at Mindanao State 
University - Iligan Institute of Technology (MSU-IIT). The approach is inspired by a structured 
framework for building large language models (LLM)-powered applications, as outlined in a Medium 
post by Pallavi Sinha (Building LLM-Powered Applications). The methodology has been adapted to 
exclude deployment-related steps (Observability Setup and Deployment and Hosting) as shown in 
Figure 3.1, aligning with the research objectives and timeline from January 2025 to April 2025. The 
process encompasses seven phases: Use Case Discovery, System Architecture Design, Prototype 
Building, Implementation of Core Components, Performance Evaluation, and Analysis and 
Documentation. 
The development of AI-powered applications, particularly those leveraging LLMs, requires a 
structured methodology to navigate their inherent complexities. Research suggests that a systematic 
approach, including a clear objective definition, high-quality data preparation, appropriate model 
selection, and rigorous evaluation, is essential for success (Sarker, 2022). This methodology ensures 
that CatSight AI addresses the specific needs of MSU-IIT’s document retrieval system while 
incorporating best practices in AI development, such as iterative testing and refinement. 
Figure 3.1: Steps Breakdown for Building LLM-Powered Applications (Sinha, 2024) 
` 
3.1 
Use Case Discovery 
The use case for CatSight AI addresses the inefficiencies of MSU-IIT’s traditional keyword-based 
document retrieval systems, which struggle with contextual understanding and semantic relevance. 
Traditional keyword-based search systems face significant limitations in understanding user intent and 
query context, often returning irrelevant results when exact keywords are not matched (Semantic 
Search vs Keyword Search). For instance, a search for “policy updates” might miss documents phrased 
differently but semantically relevant. CatSight AI overcomes these challenges by integrating optical 
character recognition (OCR), vector similarity search, and LLM-based chat interfaces to enable 
semantic search and conversational interaction, aligning with the study’s objective to enhance search 
accuracy and user experience. 
3.1.1 
Process of Document Collection and Preparation 
The study begins with the collection and preparation of institutional documents sourced from two 
repositories: (1) MSU-IIT documents and (2) MSU System Board of Regents (BOR) Resolutions. Both 
scanned and text-based PDF files are gathered, curated, and pre-processed to serve as representative 
data for evaluating the proposed Document Retrieval System (DRS). This ensures the inclusion of a 
diverse range of document types, formats, and complexities, including scanned documents requiring 
Optical Character Recognition (OCR) processing. 
To ensure that the DRS is evaluated across a realistic and meaningful spectrum of institutional 
documentation, specific criteria were observed in selecting the files: 
● Relevance: Documents were chosen based on their alignment with common administrative 
functions and frequently referenced topics within institutional settings. 
● Diversity of Content: Categories were selected to represent a range of document purposes, 
such as policies, designations, and event-related issuances. 
● Format Variety: Both scanned and digitally native PDF files were included to evaluate the 
system’s ability to handle different input formats and OCR-related challenges. 
` 
● Structural Complexity: Documents with varied layouts—such as those containing tables, 
headings, and multiple sections—were prioritized to test the system’s retrieval accuracy under 
complex formatting conditions. 
3.1.2 
Problem Definition & Stakeholders 
The development of CatSight AI was motivated by critical limitations observed in the existing 
Document Retrieval System (DRS) at Mindanao State University - Iligan Institute of Technology 
(MSU-IIT). The institution relies on two primary repositories: the Board of Regents (BOR) Resolutions 
Archive, which governs MSU System policies, and IIT Docs, a repository of Special Orders, 
Memorandum Orders, and administrative issuances built on Google Drive’s keyword-based search. 
While functional, these systems exhibit significant shortcomings: 
1. Semantic Blindness: 
The keyword-only mechanism fails to interpret contextual nuances or semantic relationships, 
leading to irrelevant or incomplete results. For example: 
○ Queries for "Special Orders" miss documents labeled with abbreviations like "SO." 
○ Synonym-rich content (e.g., "academic calendar" vs. "term schedule") remains 
undiscovered. 
○ Paraphrased queries (e.g., "student allowances" vs. "financial aid") yield inconsistent 
results. 
2. Format Exclusion: 
Scanned or image-based PDFs are entirely excluded from search results due to the lack of 
Optical Character Recognition (OCR) capabilities. Documents with complex layouts—such as 
tables, multi-column text, or handwritten annotations—are similarly unsearchable. 
3. Rigid Interaction: 
Users cannot refine queries iteratively due to the absence of a conversational interface, forcing 
them to rely on repetitive keyword adjustments. 
Primary Stakeholders: 
● Students: Require timely access to academic policies (e.g., scholarship resolutions, enrollment 
guidelines) and event announcements. 
` 
● Staff: Responsible for locating memorandums (e.g., procurement procedures, compliance 
records) to streamline operational workflows. 
3.2 
System Architecture Design 
Informed by the different literatures, a comprehensive literature review is conducted to identify the best 
practices and state-of-the-art techniques in content-based retrieval systems, OCR, vector embeddings, 
and large model integration. This review guides the design of a system architecture that addresses 
identified shortcomings. 
The system architecture of CatSight AI integrates OCR, vector embeddings, vector storage, and an 
LLM to create a robust DRS. Informed by a comprehensive literature review, the design addresses 
shortcomings identified in traditional systems and incorporates state-of-the-art techniques in 
content-based retrieval, OCR, embeddings, and LLM integration. The architecture follows a standard 
RAG framework, where documents are processed, embedded, stored, and retrieved to support 
LLM-generated responses (Knowledge Retrieval Architecture). 
3.2.1 
LLM System Strategy 
The LLM System Strategy for CatSight AI prioritized a single LLM approach to streamline 
development and reduce computational overhead, opting against multi-agent systems that are better 
suited for complex, specialized tasks (Chen et al., 2023). This decision was informed by a rigorous 
evaluation of multiple candidate models from Ollama to ensure optimal performance for document 
retrieval and conversational interaction at MSU-IIT. 
Several models were tested for both the primary LLM and the embedding model: 
For the LLM: 
● llama3.1:8b: Demonstrated strong language understanding but required significant 
computational resources, making it less feasible for real-time applications. 
● llama3.2:1b: A lightweight model with low resource demands but insufficient for handling 
complex conversational tasks requiring deep contextual understanding. 
` 
● qwen3:1.7b: Offered good language capabilities but struggled with processing long-context 
documents, a critical requirement for MSU-IIT’s use case. 
● qwen2.5:7b-instruct-q4_K_M: Excelled in instruction-following tasks but was less efficient 
for real-time interaction due to higher latency. 
● llama3.1:8b-text-fp16: Optimized for text processing, it performed well but was less versatile 
than Llama 3.1 for conversational applications but requires more resources. 
● llama3.18b-q4: Selected as the primary LLM for its balanced performance, efficiency, and 
ability to handle complex queries and generate context-aware responses, fine-tuned for 
MSU-IIT’s institutional context (Meta AI, 2025). 
For the embedding model: 
● bge-m3:latest: Initially evaluated for its multi-lingual support but found lacking in accurately 
capturing specific entities such as names, numbers, and native terms prevalent in MSU-IIT’s 
documents. 
● mxbai-embed-large: Chosen for its superior semantic accuracy, particularly in handling 
nuanced entities, making it ideal for semantic search across MSU-IIT’s diverse document set 
(mixedbread.ai, 2024). 
Benchmarking was conducted using sample documents from MSU-IIT, focusing on tasks such as text 
generation, question answering, and semantic similarity search. Metrics included response accuracy, 
latency, and resource utilization. Llama 3.1 8B Q4 outperformed other LLMs in generating accurate 
and contextually relevant responses with moderate computational requirements, making it suitable for 
real-time applications. Similarly, mxbai-embed-large demonstrated higher precision in embedding tasks 
compared to bge-m3, particularly for documents containing names, numbers, and native terms, 
ensuring robust retrieval performance (Brown et al., 2020; mixedbread.ai, 2024). 
The decision to use a single LLM was driven by simplicity and cost-effectiveness. Multi-agent systems, 
while capable of handling specialized tasks, introduce complexity and overhead that were unnecessary 
for MSU-IIT’s document retrieval needs (Chen et al., 2023). Llama 3.1-8 B-Q4’s capabilities, 
combined with mxbai-embed-large’s embedding accuracy, provided a streamlined and efficient 
solution, aligning with the system’s objectives of enhancing search accuracy and user interaction. 
` 
This model selection process, grounded in literature and practical experimentation, ensured that 
CatSight AI’s architecture was optimized for performance, scalability, and relevance to MSU-IIT’s 
specific requirements. 
3.2.2 
Architecture Components 
A comprehensive literature review identified best practices in content-based retrieval, OCR, vector 
embeddings, and LLM integration, guiding the design of CatSight AI’s architecture to address 
limitations of MSU-IIT’s keyword-based systems. The architecture integrates: 
● OCR (Marker): Converting scanned PDFs into searchable text, specifically converting it to 
markdown. 
● Dynamic Chunking: Dividing markdown text into contextually coherent segments. 
● Embedding Generation (mxbai-embed-large): Transforming text segments into vector 
representations. 
● Vector Storage (pgvector on PostgreSQL): Efficient storage and similarity-based retrieval of 
embeddings. 
● Interactive Retrieval (Llama 3.1 8B Q4): Features a LangGraph-based chatbot enabling 
users to engage in chat-based queries and receive contextually relevant responses. 
A frontend developed in React ensures a user-friendly interface, while a Django-based backend and 
API layer handle data flow. Figure 3.1 illustrates the data pipeline from document ingestion to 
interactive retrieval, clarifying how each component fits into the overall architecture. 
` 
Figure 3.1 System Workflow for Document Processing, Search, and Chat Interaction 
3.3 
Development and Iterative Validation 
In the development of CatSight AI, the team proceeded directly to full implementation, integrating core 
components such as document ingestion, OCR, text chunking, embeddings, vector storage, and the 
interactive chat interface. This approach, while bypassing a separate prototyping phase, incorporated 
iterative testing and refinement throughout the development process, effectively serving as a 
continuous validation mechanism. This aligns with agile development practices, where validation is 
embedded within the development cycle to ensure the system meets functional and performance 
requirements (Agile Manifesto). 
` 
During the initial development phases, each component was tested individually and in integration with 
sample documents from MSU-IIT’s repositories. For example, the OCR pipeline, utilizing Marker, 
MarkItDown, and Docling, was validated by processing a subset of scanned and text-based PDFs, 
ensuring high-fidelity text extraction and structure preservation. Similarly, the embedding and retrieval 
mechanisms, powered by mxbai-embed-large and pgvector, were tested with sample queries to verify 
semantic accuracy and retrieval efficiency. 
This iterative validation process allowed for early detection and resolution of issues, such as OCR 
errors or suboptimal chunking, ensuring that the system evolved into a robust solution. By embedding 
testing within development, the team effectively validated the concept without a distinct prototyping 
phase, aligning with the Medium post’s emphasis on iterative development and testing (LLM-Powered 
Applications). 
The development process also included continuous refinement based on preliminary results. For 
instance, initial tests with the chat interface revealed the need for enhanced reranking, leading to the 
integration of LLMListwiseRerank for improved relevance scoring. This iterative approach ensured 
that the final system met the research objectives of enhancing search accuracy and user interaction at 
MSU-IIT. 
Development Phase 
OCR Pipeline 
Validation Activity 
Processed sample PDFs to test 
text extraction accuracy 
Output 
High-fidelity Markdown output 
with preserved structure 
Embedding & Retrieval 
Chat Interface 
Tested with sample queries to 
verify semantic matching 
Initial user queries to assess 
response quality 
Table 2. Iterative Validation 
Accurate retrieval of relevant 
document chunks 
Integration 
LLMListwiseRerank 
enhanced relevance 
of 
for 
` 
3.4 
Implementation of the Core Components 
This phase integrates the core components of CatSight AI into a unified system, aligning with the steps 
for LLM setup and development (Building LLM-Powered Applications). The implementation 
leverages state-of-the-art open-source technologies to process diverse documents, generate 
embeddings, and enable interactive querying, ensuring scalability and accuracy for MSU-IIT’s 
document retrieval needs. 
3.4.1 
LLM Setup 
The Llama 3.1-8B-Q4 model was selected for its state-of-the-art performance in natural language tasks 
and open-source availability, reducing costs compared to proprietary models. Setup involved 
configuring the model for retrieval-augmented generation, with prompt engineering to optimize 
responses based on retrieved document chunks. Fine-tuning was performed on a subset of MSU-IIT 
documents to enhance domain-specific performance, following best practices for LLM customization 
(Lewis et al., 2020). This step ensures that the LLM is tailored to the institutional context, improving 
response relevance and accuracy. 
3.4.2 
Document Ingestion & OCR 
CatSight AI employs a hybrid approach for document ingestion and optical character recognition 
(OCR), utilizing Marker to convert PDFs into structured Markdown format and Surya for complex 
documents. This ensures high-fidelity text extraction while preserving semantic structures like 
headings, lists, and tables, which are critical for downstream processing. 
● Marker: Marker uses a pipeline of machine learning models, including LayoutLMv3 for 
layout detection and Nougat for mathematical equation recognition, to produce accurate 
Markdown output (Marker GitHub). LayoutLMv3, a multimodal transformer model, excels in 
understanding document layouts by pre-training with unified text and image masking, 
achieving state-of-the-art performance in tasks like form understanding and document visual 
question answering (Huang et al., 2022). Nougat, designed for scientific documents, converts 
mathematical expressions into LaTeX markup, enhancing accessibility for technical content 
` 
(Blecher et al., 2023). Marker’s ability to handle complex layouts and equations makes it ideal 
for MSU-IIT’s diverse document set, including scanned academic papers. 
● Surya: Surya is an open-source toolkit that performs high-accuracy OCR and sophisticated 
document layout analysis, such as table and header detection (Paruchuri, 2024a). For each 
input PDF or image, Surya produces a structured JSON representation of the document’s 
content and layout. 
The choice of the conversion tool is based on document characteristics: Marker for complex layouts 
and equations, standard text documents, and highly structured formats. This strategy ensures optimal 
performance across diverse document types, as supported by research on document conversion 
challenges (Livathinos et al., 2025). 
When a user uploads a PDF, the frontend enqueues the task in Redis, which serves as the message 
broker for Celery workers. These workers asynchronously process each job, ensuring non-blocking 
uploads and horizontal scalability (Celery Project, Redis). Redis’s in-memory task queuing enhances 
performance, enabling efficient handling of large document volumes. Preprocessing enhances image 
quality through binarization, de-skewing, and noise reduction, improving OCR accuracy 
(Technovators, 2021). 
The Surya layout engine analyzes document structure, detecting headers, paragraphs, lists, and tables, 
producing a JSON representation for Markdown reconstruction (Surya GitHub). This output is then 
passed to Marker, which converts the layout data into clean Markdown (Paruchuri, 2024b). Marker 
merges text blocks, formats equations and inline math, reconstructs tables, removes headers/footers, 
and corrects OCR artifacts. This Surya + Marker pipeline replaces the previously considered Docling 
and MarkItDown tools and ensures highly accurate Markdown extraction from scanned and 
image-based academic documents. 
The Surya + Marker pipeline orchestrates block merging, inline-math formatting, and table 
reconstruction, followed by a post-processing pass to correct OCR errors. The resulting Markdown 
files and metadata are stored on the server, with pointers logged in PostgreSQL (AWS S3, 
PostgreSQL). 
` 
Figure 3.2.1  OCR Pipeline  
3.4.3 
Document Summarization and Metadata Extraction 
After ingestion, each document undergoes summarization using a map-reduce workflow implemented 
via LangGraph. In the "map" phase, each chunk (with a larger overlap than in retrieval) is summarized 
by an LLM. These summaries are processed in parallel to improve throughput and efficiency 
(LangChain, 2024b). The final "reduce" step combines the summaries into a single coherent abstract. 
` 
This technique improves coverage and cohesion of long document summarization. Additionally, 
metadata such as a document title, publication date, and 3–5 topic tags are extracted using LLM-based 
keyphrase generation. These details are stored in the database for use in filtering and enhancing the 
retrieval and display experience. This method addresses the challenge of processing long documents by 
breaking them into smaller, manageable chunks, summarizing each, and combining the results into a 
coherent summary, enabling efficient handling of large texts (Sojasingarayar, 2024). 
● Chunking: The Markdown content is segmented into logical chunks based on structural 
elements like sections or paragraphs, ensuring semantic coherence. 
● Mapping: Each chunk is summarized individually using an LLM, producing concise partial 
summaries that capture key information. 
● Reducing: Partial summaries are aggregated and further summarized to generate a final 
document summary, maintaining factual accuracy and coherence. 
This hierarchical approach scales effectively for lengthy documents, as it parallelizes the mapping step 
and focuses on local context before global synthesis, improving summary quality (Gupta & Lehal, 
2015). LangGraph’s graph-based orchestration ensures efficient execution, supporting parallel 
processing and error recovery. 
Metadata extraction enhances document querying and organization: 
● Title Generation: The LLM generates a concise, descriptive title based on the document’s 
summary or introduction, following methods for automatic title generation that leverage 
transformer models to capture document essence (Sarkar et al., 2021). 
● Year Extraction: Publication years are identified by scanning for date patterns or using the 
LLM to extract years from contextual clues, such as references or copyright notices. 
● Tag Generation: Key topics are extracted as tags using LLM-based keyphrase extraction, 
prompted to identify 3–5 keywords from the summary, ensuring consistency and relevance 
(Agarwal et al., 2020). 
These metadata elements are stored alongside the Markdown and summary, facilitating efficient search 
and filtering within the system. 
` 
Figure 3.2.2 Document Summarization and Metadata Extraction Pipeline 
3.4.4 
Text Chunking & Embedding 
To prepare documents for vector storage, CatSight AI uses the RecursiveCharacterTextSplitter from 
LangChain to segment Markdown text into chunks (LangChain Text Splitters). This method recursively 
splits text by a list of separators (e.g., double newlines, newlines, spaces) until chunks are within a 
specified size limit, preserving semantic units like paragraphs or sentences. The splitter uses a 
hierarchy of breakpoints—paragraphs, line breaks, spaces—to avoid splitting mid-sentence or 
mid-idea. We configured the tool with a chunk size of 1000 tokens and a chunk overlap of 100 tokens 
(10%), which captures more semantic context in each segment and ensures continuity between chunks 
(TryChroma, 2023a).  
Unlike 
dynamic 
chunking, 
which 
combines 
rule-based 
and 
semantic 
methods, 
RecursiveCharacterTextSplitter offers simplicity and efficiency, making it suitable for MSU-IIT’s 
diverse document set (Svenson, 2025).  
Each chunk is encoded into a dense vector using mxbai-embed-large, a state-of-the-art embedding 
model from mixedbread.ai (mxbai-embed-large-v1). This model was selected over bge-m3 due to its 
` 
superior performance in capturing semantic nuances, particularly for names, numbers, and native terms, 
which are critical for accurate retrieval in institutional documents. Trained on over 700 million text 
pairs and fine-tuned with 30 million high-quality triplets using the AnglE loss function, 
mxbai-embed-large outperforms models like OpenAI’s text-embedding-ada-002 on benchmarks like 
MTEB, ensuring robust generalization across domains (mixedbread.ai, 2024). The resulting 
embeddings, typically 512-dimensional vectors, are normalized for cosine similarity searches and 
stored in a PostgreSQL database with the pgvector extension. 
Figure 3.2.3. Detailed Chunking & Embedding Pipeline 
3.4.5 
Vector Storage & Retrieval  
Embeddings are managed using pgvector, a PostgreSQL extension that supports vector similarity 
searches with efficient indexing (pgvector GitHub). Pgvector integrates seamlessly with PostgreSQL, 
allowing SQL-based vector operations and supporting both exact and approximate nearest-neighbor 
(ANN) searches. Its performance is optimized for large-scale datasets, making it ideal for CatSight AI’s 
document corpus (Neon, 2023). 
Two ANN indexing methods are utilized: 
● IVFFlat: Partitions the vector space into clusters, probing a subset during queries to balance 
speed and recall. It is faster to build and uses less memory, suitable for moderate-sized 
datasets. 
` 
● HNSW (Hierarchical Navigable Small World): Constructs a multilayer proximity graph for 
logarithmic search performance, offering superior speed-recall trade-offs but requiring more 
memory and build time (Crunchy Data, 2023). 
For MSU-IIT’s use case, HNSW is preferred for its high performance, though IVFFlat is used for 
initial testing due to faster indexing. When a user query is received, it is embedded using 
mxbai-embed-large, and a SELECT query with an ORDER BY embedding <-> query_vector clause 
retrieves the top-k most similar chunks. These chunks are reassembled and passed to the LLM for 
response generation, completing the retrieval-augmented pipeline (Brahma, 2024). 
Figure 3.2.4 Vector Storage & Retrieval Pipeline 
3.4.6 
Interactive Chat Interface 
The CatSight AI interface includes a React frontend and a Django backend API. It uses a 
retrieval-augmented generation (RAG) pipeline powered by LangGraph and Llama 3.1. When a user 
submits a question, the query is embedded using mxbai-embed-large and compared against existing 
chunk vectors in pgvector. To reduce noise, chunks with a cosine similarity score below 0.4 are 
discarded (TryChroma, 2023b). This filtering improves accuracy by eliminating irrelevant documents. 
Next, the remaining chunks are passed to the LLMListwiseRerank utility, which applies zero-shot 
listwise ranking to determine their relevance. The top-ranked passages are then used to construct a 
prompt for the Llama 3.1 8B Q4 model, which generates a response. The output is streamed back in 
` 
real-time via server-sent events (SSE), providing users with a conversational interface grounded in 
trusted source materials. 
The chatbot operates in three key steps: 
● Retrieval: User queries are converted into embeddings using the mxbai-embed-large model, 
known for its robust performance in capturing semantic nuances, including names, numbers, 
and native terms (mxbai-embed-large-v1). A top-k approximate nearest-neighbor (ANN) 
search is performed using the pgvector extension in PostgreSQL, retrieving document chunks 
that align with the query’s semantic content (pgvector GitHub). 
● Reranking with LLMListwiseRerank: To enhance the relevance of retrieved chunks, 
CatSight AI employs the LLMListwiseRerank tool, which uses zero-shot listwise document 
reranking. This method leverages a large language model to evaluate and reorder the top-k 
chunks based on their contextual relevance to the query, considering the entire list of 
candidates simultaneously. Unlike traditional pointwise or pairwise reranking, listwise 
reranking optimizes the ranking order by modeling inter-document relationships, improving 
the selection of the most pertinent chunks (Liu, 2009). This approach is particularly effective 
in RAG systems, as it ensures that only the most relevant content is passed to the response 
generation phase, reducing noise and enhancing answer quality (Es et al., 2024). 
● Response Generation: The reranked chunks are concatenated into a RAG prompt template 
and passed to Llama 3.1 8B Q4, which generates a response streamed to the frontend via 
server-sent events for real-time interaction (Meta AI). Llama 3.1 8B Q4 was fine-tuned on a 
subset of MSU-IIT documents to optimize domain-specific performance, ensuring responses 
are contextually accurate and institutionally relevant (Lewis et al., 2020). 
The interface supports user-friendly features such as response regeneration, context copying, and error 
handling via toast notifications, enhancing usability and debuggability (Apideck). System integration 
testing ensures robustness under various conditions, including corrupted file uploads and network 
interruptions. The use of LLMListwiseRerank aligns with advanced RAG techniques, improving the 
chatbot’s ability to deliver precise and relevant answers by prioritizing high-quality document chunks 
(Nielson, 2025). 
` 
Figure 3.2.5 Interactive Chat Interface Pipeline 
This compact flowchart captures the essential steps: query input, combined embedding, retrieval, and 
reranking with LLMListwiseRerank, relevance checking, response generation, streaming, and user 
options for regeneration, with error handling for robustness. 
Component 
Document Ingestion 
Technology 
Marker, Surya 
Key Features 
Layout detection, 
equation recognition, 
vision-based parsing 
Reference 
Huang et al., 2022; 
Blecher et al., 2023; 
Nassar et al., 2022 
Summarization 
Chunking 
Embedding 
Vector Storage and 
Retrieval 
Reranking 
Chat Interface 
3.5 
LLM, LangGraph for 
orchestration 
RecursiveCharacterTe
 xtSplitter 
mxbai-embed-large 
pgvector, 
llama3.1:8b-q4 
LLMListwiseRerank 
React, Django, 
LangGraph 
Map-reduce, parallel 
processing 
Recursive splitting by 
separators 
High performance on 
names, numbers, 
native terms 
ANN search with 
IVFFlat, HNSW 
Zero-shot listwise 
reranking 
RAG, relevance 
grading, streaming 
Table 3. Summary of Technologies Used 
Performance Evaluation of the DRS Prototype 
Gupta & Lehal, 2015 
Svenson, 2025 
mixedbread.ai, 2024 
Crunchy Data, 2023 
Liu, 2009 
Lewis et al., 2020; Es 
et al., 2024 
To measure the system’s efficacy, approximately 50 test files with predetermined content are uploaded. 
Automated scripts simulate user actions—such as searching for specific terms, browsing results, and 
engaging in chat-based queries—to verify that the system returns accurate and context-relevant 
information. 
` 
Evaluation on Processing Accuracy 
3.5.1  
To evaluate the accuracy of the system in providing relevant and correct document retrieval, the 
proponents conducted a series of tests using the annotated dataset prepared during the document 
ingestion phase. Both scanned and digital PDFs were uploaded into the system to ensure 
comprehensive testing. Multiple test queries were then initiated to simulate real user information needs, 
with particular focus on evaluating the system’s ability to retrieve semantically relevant documents 
even when queries were phrased differently from the source material. Each system output was carefully 
reviewed and compared against the ground truth annotations, and the relevance of the retrieved 
documents was manually assessed based on their semantic alignment with the user queries. 
3.5.2  
Usability Test 
Usability testing is a method in which researchers ask participants to perform tasks using one or more 
specific interfaces, followed by collecting feedback to assess system effectiveness and user satisfaction 
(Moran, 2023). Since this study involves a comparative analysis, group sizes between 8 to 25 
participants are typically sufficient to yield valid results, with 10–12 participants considered a solid 
baseline (Six & Macefield, 2016). For statistically significant outcomes, larger sample sizes are 
recommended. 
In this study, the user evaluation was conducted on May 13, 2025, at Mindanao State University – 
Iligan Institute of Technology (MSU-IIT). Its purpose was to collect usability data for both the 
traditional document retrieval systems (IIT Docs and BOR Resolution Archive) and the proposed 
system, CatSight AI. A total of 15 participants: staff, faculty members, administrative personnel 
participated in the study. Participants were selected based on their availability and willingness to 
participate. 
CatSight AI was deployed online for testing purposes to allow participants to access it on devices they 
were most comfortable with. For participants without personal devices, access was provided via the 
Computer Science Laboratory. 
Participants were first instructed to use the traditional document retrieval systems: IIT Docs and the 
Board of Regents (BOR) Resolutions Archive. After completing the tasks, they answered a printed 
System Usability Scale (SUS) questionnaire and provided optional comments about their experience. 
` 
The same process was followed after they tested CatSight AI. Figure 3.2 shows the flowchart for the 
data collection process. 
Figure 3.2. Flowchart of the Usability Testing and Data Collection Process 
The SUS questionnaire consists of 10 statements rated on a five-point Likert scale ranging from 
"Strongly Disagree" (1) to "Strongly Agree" (5): 
1. I think that I would like to use this sytem frequently. 
2. I found the system unnecessarily complex. 
3. I think the system is simple and easy to use. 
4. I think I need technical support to use this system. 
5. I find the system functioning smoothly and is well- integrated. 
6. I think there are a lot of irregularities in the system. 
7. I think most people can learn this system quickly 
8. I find this system to be time-consuming. 
9. I felt very confident using the system. 
10. I think there are a lot of things to learn before I can start using this system. 
The SUS score for each participant was calculated using the standard formula as seen in Equation 3.4, 
resulting in a score from 0 to 100, where higher scores indicate better usability (Bhat, 2018).  
X = Sum of odd numbered items - 5 
Y = 25 - Sum of even-numbered items 
SUS Score = (x+y) × 2.5    
(3.4) 
Table 3.4.1 presents the SUS score ranges and their corresponding interpretation in relation to 
percentiles, grades, and adjectives as interpretations. An average score is considered as the average 
across literatures (Sauro, 2018). 
` 
Grade 
SUS 
Percentile Range 
Adjective 
Acceptable 
A+ 
84.1-100 
96-100 
Best Imaginable 
Acceptable 
A 
A- 
B+ 
B 
B- 
C+ 
C 
C- 
D 
F 
F  
80.8-84.0 
78.9-80.7 
77.2-78.8 
74.1 – 77.1 
72.6 – 74.0 
71.1 – 72.5 
65.0 – 71.0 
62.7 – 64.9 
51.7 – 62.6 
25.1 – 51.6 
90-95 
85-89  
80-84  
70 – 79  
65 – 69  
60 – 64 
41 – 59  
35 – 40  
15 – 34 
2– 14 
0-1.9 
Excellent 
Good 
OK 
Poor 
Worst Imaginable 
Acceptable 
Acceptable 
Acceptable 
Acceptable 
Acceptable 
Acceptable 
Marginal 
Marginal 
Marginal 
Not Acceptable 
Not Acceptable 
0-25 
Table 3.4.1. Interpretations for Raw SUS Score 
The questionnaire also featured a section where participants could elaborate on any issues they 
encountered with the application's design and offer suggestions for improvement 
3.6  
Analysis of Evaluation Results and Final Documentation 
This section synthesizes the empirical findings from Catsight AI’s evaluation, comparing its 
performance against MSU-IIT’s traditional keyword-based system. Results are analyzed across two 
dimensions: processing accuracy, and usability, followed by recommendations for future work. 
3.6.1 
Processing Accuracy 
To evaluate the effectiveness of the retrieval component of CatSight AI, the system was tested using 
cosine similarity as the primary distance metric for comparing vector embeddings. Cosine similarity 
measures the angular difference between the query vector and document chunk vectors, which is ideal 
for determining semantic closeness in high-dimensional embedding spaces. 
` 
A similarity score threshold of 0.4 was applied to filter out low-relevance results. Chunks with a 
similarity score below this threshold were excluded from the final result set to prevent semantically 
weak matches from being passed to the LLM for response generation. This threshold was chosen based 
on empirical tuning, balancing between strict filtering and adequate recall.  
To further improve result ranking, the system implemented LLMListwiseRerank using a top-N 
reranking strategy, with top_n=10. After the initial top-10 chunks were retrieved based on cosine 
similarity, they were re-evaluated and reordered using LLM-based semantic scoring. This reranking 
step helped prioritize the most contextually accurate and informative results, especially when multiple 
chunks had similar similarity scores but differed in relevance to the query. 
3.6.2 
Usability  
Usability testing was conducted to evaluate and compare the user experience between the traditional 
document retrieval systems (IIT Docs and BOR Resolution Archive) and the proposed system, 
CatSight AI. Each participant was asked to interact with and observe both systems by performing 
typical tasks such as locating policy documents, designation orders, or resolutions. This process 
allowed users to form comparative impressions based on task completion, ease of navigation, and 
relevance of search results. 
After using both systems, participants completed the System Usability Scale (SUS) questionnaire, 
which consists of 10 standardized statements rated on a five-point Likert scale. The responses were 
scored using Equation 3.4. 
The resulting SUS scores, ranging from 0 to 100, were then analyzed and interpreted using Table 3.4.1: 
Interpretation for Raw SUS Score, which classifies the results based on percentile rank, grade, and 
adjective rating. 
This approach provided a standardized and quantifiable way to assess usability. By comparing the 
average SUS scores of the traditional systems and CatSight AI, the evaluation clearly demonstrated 
how the proposed system improved the overall user experience. 
` 
Chapter 4  Results and Discussion 
This chapter presents the outcomes of the system implementation following the guidelines of building 
an LLM–powered system. 
4.1 Document Collection and Preparation 
Following the data collection phase, a total of 50 documents in PDF were selected from the IIT Docs 
and Board of Regents (BOR) Resolutions Archive repositories. These documents were annotated and 
categorized based on the selection criteria outlined in Section 3.1.1, which emphasized relevance, 
content diversity, format variety, and structural complexity. Figure 4.1 shows the collected and prepared 
documents. 
The purpose of this preparation was to ensure that the sample dataset effectively represented the types 
of documents commonly retrieved by users at MSU-IIT. This prepared dataset served as the benchmark 
for evaluating the accuracy and effectiveness of the proposed system. 
Document Source 
IIT-Docs 
IIT-Docs 
Category 
Designation 
Policy 
Count 
5 
5 
IIT-Docs 
IIT-Docs 
IIT-Docs 
BOR Resolution Archives 
BOR Resolution Archives 
BOR Resolution Archives 
BOR Resolution Archives 
BOR Resolution Archives 
Incentives 
Travel Order 
Charter Day 
Designation 
Policy 
Incentive 
Travel Order 
Suspension 
Total 
Figure 4.1: Collected and Annotated Documents for Testing 
5 
5 
5 
5 
5 
5 
5 
5 
50 
` 
4.2 Prototype Building 
The prototype of CatSight AI was developed to address the limitations of traditional keyword-based 
document retrieval at Mindanao State University – Iligan Institute of Technology (MSU-IIT). The 
system integrates cutting-edge technologies—Optical Character Recognition (OCR), dynamic 
chunking, semantic vector search, and large language model (LLM)-powered interaction—into a 
unified document retrieval pipeline. This section presents the technical architecture, core components, 
and operational flow of the prototype system. 
4.2.1 Document Ingestion 
In the initial implementation of the OCR part, the proponents first tried the Docling; however, during 
the initial test, the proponents discovered that the output, which is in the markdown format, was not 
accurate compared to the ground truth. With this issue, the proponents tried other OCRs that are close 
to the ground truth. The proponents then discover Marker, a much more accurate PDF to markdown 
technology. According (Paruchuri (2024), Figure 4.2 shows the comparison of the performance of the 
different OCR models in terms of average time to extract PDF from Common Crawl. They also scored 
based on a heuristic that aligns text with ground truth text segments, and an LLM as a judge scoring 
method. 
Figure 4.2: Comparison of OCR Technologies 
Figure 4.3 shows the result of the PDF to markdown format using Marker in the interface of Catsight 
AI 
` 
Figure 4.3: PDF to Markdown 
However, the proponents observed that the marker component did not fully capture the entire content 
of some PDF files, as illustrated in Figure 4.4. This limitation indicates that certain segments of the 
document, especially those with complex layouts or non-standard formatting, may not be accurately 
represented in the extracted output. Therefore, the proponents implemented a feature that allows users 
to preview the generated markdown and manually edit it when irregularities or omissions are detected. 
This additional step ensures that the document content is accurately preserved and properly indexed for 
retrieval. 
Figure 4.4: Incomplete Content Capture by the Marker Component in a PDF with Complex Layout 
` 
4.2.2 Text Chunking and Embedding  
To segment raw text into manageable and meaningful units, the system employed the 
RecursiveCharacterTextSplitter from LangChain. This method recursively breaks down text using a 
prioritized list of separators (such as double newlines, single newlines, and spaces) until each chunk fits 
within a specified size limit. In the initial implementation, the proponents used bge-m3 due to its strong 
performance across multilingual retrieval tasks. However, during testing, it was observed that certain 
native Filipino terms were not effectively captured. For example, when querying "Who are the winners 
of 'Sa Umaabot' competition?", the model struggled to retrieve relevant results, even though 'Sa 
Umaabot' is a key phrase in the context.  
In contrast, when using mxbai-embed-large-v1, the system was able to retrieve the correct information, 
demonstrating better semantic alignment with Filipino terms as seen in figure 4.6. This led the 
proponents to adopt mxbai-embed-large-v1 for improved accuracy in handling localized content.   
Figure 4.6: Query Using mxbai-embed-large-v1 
` 
Figure 4.7: Document Provided by the System 
For this system, each document was split into chunks of 1000 characters with a 100-character overlap 
between consecutive segments. This configuration was designed to preserve contextual continuity 
across chunks, ensuring that important information located at the boundaries of text segments was 
retained. By maintaining this overlap, the system was able to capture semantically coherent units, such 
as full paragraphs or policy statements—without breaking the logical flow of the content. 
4.2.3 Vector Storage and Retrieval 
After the generated embeddings were stored and queried using pgvector, a PostgreSQL extension that 
supports high-performance vector silimilarity searches (Winslett, 2023). During testing, IVFFlat was 
used to quickly validate retrieval logic and system integration. However, for the final prototype 
evaluation, HNSW indexing was adopted due to its significantly better query precision and 
responsiveness, especially when retrieving semantically similar results from the annotated 
50-documents.  
4.2.4 Interactive Chat Interface 
Figure 4.8 shows the interactive chat interface of the system.  
` 
Figure 4.8:  Interactive Chat Interface of Catsight.AI 
4.3 System Evaluation and Analysis 
This subsection consolidates the system’s performance metrics derived from user responses, focusing 
on its accuracy in retrieving relevant documents based on user queries. It further evaluates the system’s 
usability through the System Usability Scale (SUS), providing a quantitative assessment to determine 
improvements introduced by the proposed solution. 
4.3.1 Performance Evaluation 
After the proponents uploaded the 50 annotated documents to evaluate the system if it can retrieved 
documents, the proponents put the query on the figure 4.9. The proponents call each prompt using the 
queries: “Who is Dante Dinawanao” and “When was Dante Dinawanao went to the United States” both 
mentioning the person but in the different context. Figure 4.10 and 4.11 shows the retrieval pipeline 
and ranking effectiveness. See that at first is the ranking of chunks by cosine similarity score. Chunks 
below 0.4 threshold were filtered out. The top 10 are reranked using LLMListwiseRerank based on 
contextual relevance.  
` 
Figure 4.9: Document Search Interface of Catsight AI 
` 
 
Figure 4.10: Result on query number 1 
 
 
 
` 
 
Figure 4.11: Result on Query Number 2 
 
 
 
` 
4.3.2 System Usability Survey (SUS) Evaluation 
The proponents conducted a System Usability Survey (SUS) with 15 respondents, consisting of 
students, faculty, and staff of MSU-IIT, to determine the satisfaction level of Catsight AI in comparison 
to the IIT Docs and BOR Resolution Archives. The initial SUS score of the old system was 50.33% as 
shown in Figure 4.8. While the Catsight AI scored 77.17% as shown in Figure 4.9. Based on the SUS 
score of both systems, the old system showed that it is a poor and unacceptable system, based on Table 
3.4.1 Interpretation of Raw SUS Score. On the other hand, the Catsight AI has been shown to be good 
and acceptable. Therefore, the respondents are satisfied with the proposed system. 
Figure 4.12. System Usability Score (SUS) of IIT-Docs and BOR Resolution Archive
 Figure 4.13. System Usability Score (SUS) of Catsight AI 
` 
Chapter 5 Conclusion and Future Works 
This chapter presents the conclusion of the study and recommendations for future work to improve the 
system.  
5.1 Conclusion 
This study successfully developed and evaluated CatSight AI, an advanced document retrieval system 
designed to address the limitations of traditional keyword-based search at Mindanao State University – 
Iligan Institute of Technology (MSU-IIT). By integrating Optical Character Recognition (OCR), vector 
similarity search, and LLM-powered conversational interfaces, the system significantly enhanced 
search accuracy, user interaction, and retrieval efficiency. The system demonstrated improved semantic 
understanding by outperforming traditional keyword-based methods through the use of vector 
embeddings and semantic search, enabling context-aware retrieval even with paraphrased or 
synonym-rich queries—for example, recognizing the equivalence between “academic calendar” and 
“term schedule.” Accessibility was also enhanced through OCR, which enabled text extraction from 
scanned and image-based PDFs, while dynamic chunking ensured the structural coherence of retrieved 
information. Usability testing using the System Usability Scale (SUS) showed a satisfaction rate of 
77.17% for CatSight AI, significantly higher than the 50.33% reported for the legacy system, indicating 
improved intuitiveness and efficiency. Technically, the system exhibited strong performance through its 
hybrid architecture, combining mxbai-embed-large for semantic embeddings, pgvector for storage, 
and Llama 3.1 8B Q4 for conversational response generation. The inclusion of LLMListwiseRerank 
further refined search relevance by improving result ranking. However, the study also identified 
limitations, particularly in OCR performance when processing documents with complex layouts, which 
occasionally led to incomplete content capture. To address these limitations, future development may 
focus on expanding multilingual support, integrating table and image analysis, and enabling real-time 
collaborative features. Overall, CatSight AI sets a strong precedent for modernizing institutional 
document retrieval, aligning with global trends in AI-powered knowledge management systems. 
` 
5.2 Recommendation 
To further enhance the performance, reliability, and scope of catsight.ai, the proponents recommend 
several strategic improvements based on their findings and system evaluation. First, the knowledge 
base should be expanded beyond uploaded documents to include comprehensive information about 
Mindanao State University – Iligan Institute of Technology (MSU-IIT). This includes the institution’s 
history, academic structure, mission and vision, and notable achievements. Integrating this foundational 
knowledge will enable the system to provide more context-aware and institutionally grounded 
responses, particularly for users seeking general information about MSU-IIT. 
Second, the proponents recommend enhancing the capabilities of the LangGraph-based conversational 
agent by incorporating additional tools. These tools should include a web search function to address 
queries that fall outside the scope of the internal document repository, an intent classifier to 
dynamically route queries to the most appropriate tool or retriever, and specialized retrievers dedicated 
to specific document categories such as Special Orders, Travel Orders, and Memoranda. These 
enhancements would allow the system to more accurately interpret user intent and deliver responses 
that are tailored to the type of inquiry. 
Third, the proponents suggest optimizing the selection of language models to favor those that are 
lightweight yet effective. This ensures responsiveness and efficiency, particularly in environments with 
limited computational resources. In relation to document conversion, the proponents recommend the 
adoption of Marker’s Hybrid Mode. This configuration utilizes both OCR and large language models to 
improve the accuracy of converting scanned or visually complex PDFs into structured Markdown 
format, which in turn enhances the quality of summari 
zation and retrieval. 
To further improve text processing, the proponents advise the implementation of a Markdown-based 
text splitting strategy. This approach will preserve the semantic coherence of content during chunking, 
resulting in better contextual representation for both summarization and embedding generation. 
Additionally, the system should extend support for document formats beyond PDF, including 
PowerPoint (PPTX), Word (DOCX), and Excel (XLSX) files. This will enable a more inclusive and 
practical solution for ingesting diverse institutional documents. 
Lastly, the summarization pipeline, particularly the LangGraph map-reduce architecture used for 
generating summaries, titles, tags, and document dates, should be further refined. The proponents 
` 
recommend optimizing prompt structures and token distribution to improve the factual consistency and 
informativeness of output. Moreover, retrieval accuracy can be improved by enhancing the 
post-retrieval validation process through fine-tuning or augmenting the grade_relevant tool with 
heuristic filters. These steps will help reduce semantic drift and ensure that chatbot responses remain 
accurate, relevant, and grounded in reliable source content. 
Collectively, these recommendations aim to strengthen catsight.ai’s capabilities as an intelligent, 
context-aware research assistant that effectively supports document analysis and conversational 
interaction within an academic and institutional setting. 
` 
Appendix A 
A.1: System Usability Survey (SUS) 
` 
Appendix B Bibliography 
A guide to usability testing sample size - Trymata. (2024, October 24). Trymata. 
https://trymata.com/learn/usability-testing-sample-size/? 
Ahmed, S. (2024, November 19). Mastering chunking strategies for retrieval-augmented generation 
(RAG). 
AI 
Bites. 
(2023, 
July). 
Chunking 
in 
Retrieval-Augmented 
Generation 
https://www.ai-bites.net/chunking-in-retrieval-augmented-generation-rag/ 
(RAG). 
Amazon Web Services. (2023, April 5). Accelerate HNSW indexing and searching with pgvector on 
Amazon 
Aurora 
PostgreSQL 
[Blog 
post]. 
AWS Database Blog. 
https://www.crunchydata.com/blog/hnsw-indexes-with-postgres-and-pgvector  
Amazon 
Web 
Services. 
(2024). 
Amazon 
https://docs.aws.amazon.com/textract/latest/dg/ 
Textract 
developer 
guide. 
Analytics Vidhya. (2024, October). 15 chunking techniques to build exceptional RAG systems. 
https://www.analyticsvidhya.com/blog/2024/10/chunking-techniques-to-build-exceptional-rag-systems/  
Analytics Vidhya. (2023, October). Build a RAG pipeline with the Llama Index. 
https://www.analyticsvidhya.com/blog/2023/10/rag-pipeline-with-the-llama-index/  
Anvari, Z., & Athitsos, V. (2021). A survey on deep learning based document image enhancement. 
arXiv. https://doi.org/10.48550/arXiv.2112.02719 
Anvari, Z., & Athitsos, V. (2021). A survey on deep learning based document image enhancement. 
arXiv. https://doi.org/10.48550/arXiv.2112.02719  
Apideck. (2024). Building a local RAG chat app with Reflex, LangChain, Huggingface, and Ollama. 
https://www.apideck.com/blog/building-a-local-rag-chat-app-with-reflex-langchain-huggingfa
 ce-and-ollama  
Archive - 
JDAIP - 
Scientific 
Research 
https://www.scirp.org/journal/home?journalid=2425 
Publishing. 
(2024). 
Scirp.org. 
Asai, A., Wu, Z., Wang, Y., Sil, A., & Hajishirzi, H. (2023). Self-RAG: Learning to retrieve, generate, 
and critique through self-reflection. arXiv preprint arXiv:2310.11511. Retrieved from 
https://arxiv.org/abs/2310.11511 
` 
Bazzo, G. T., Lorentz, G. A., Suarez Vargas, D., & Moreira, V. P. (2020). Assessing the Impact of OCR 
Errors in Information Retrieval. Lecture Notes in Computer Science, 102–109. 
https://doi.org/10.1007/978-3-030-45442-5_13 
Beck, K., et al. (2001). Manifesto for Agile Software Development. https://agilemanifesto.org/ 
Bhat, A. (2018, May 31). What is System Usability Scale? | QuestionPro. QuestionPro. 
https://www.questionpro.com/blog/system-usability-scale/ 
Brahma, A. (2024, January 20). Building a production-grade RAG document ingestion pipeline with 
LlamaIndex 
and 
Qdrant. 
Medium. 
https://medium.com/@abhishek.brahma/building-a-production-grade-rag-document-ingestion
pipeline-with-llamaindex-and-qdrant-2c4e668d2cef  
Bruch, S., Gai, S., & Ingber, A. (2022). An analysis of fusion functions for hybrid retrieval. arXiv 
preprint arXiv:2210.11934. Retrieved from https://arxiv.org/abs/2210.11934 
Butterfield, E. (2014). High-tech investigations of cybercrime. In Elsevier eBooks (pp. 59–70). 
https://doi.org/10.1016/b978-0-12-800743-3.00006-2 
Carvallo, A., Parra, D., Lobel, H., & Soto, A. (2020). Automatic document screening of medical 
literature using word and text embeddings in an active learning setting. Scientometrics, 
125(3), 3047–3084. https://doi.org/10.1007/s11192-020-03648-6 
Celery Project. (n.d.). Celery 5.5.2 documentation. https://docs.celeryproject.org/ 
Chowdhury, A. N., Sami, A. A., Shah, Shakib Absar, & Rahman, S. (2025). Performance Analysis of 
Tesseract and EasyOCR for Bangla Optical Character Recognition on the Novel Bangla 
CrossHair Dataset. 2025 3rd International Conference on Intelligent Systems, Advanced 
Computing 
and 
Communication 
https://doi.org/10.1109/ISACC65211.2025.10969286 
(ISACC). 
Clark, D., Nguyen, T., & Smith, J. (2009). Challenges in data extraction from PDF documents: 
Rule-based 
approaches. 
Journal 
https://doi.org/10.1016/j.jip.2009.03.015 
of 
Information Processing, 28(3), 123–135. 
Cobus Greyling. (2025, February). Building a simple chat UI with LlamaIndex: The power of REPL. 
Medium. 
https://cobusgreyling.medium.com/building-a-simple-chat-ui-with-llamaindex-showing-the-po
 wer-of-repl-ea2e01f57485  
` 
on 
Digital 
Libraries 
(pp. 
123–132). 
ACM. 
Retrieved 
from 
Conference 
https://www.gipp.com/wp-content/papercite-data/pdf/meuschke2023.pdf 
Croft, W. B., & Harper, D. J. (2023). Document retrieval models and implementation. University of 
California, Riverside. 
Crunchy Data. (2022, November 12). HNSW indexes with Postgres and pgvector. Crunchy Data Blog. 
https://www.crunchydata.com/blog/hnsw-indexes-with-postgres-and-pgvector  
Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of deep bidirectional 
transformers for language understanding. arXiv preprint arXiv:1810.04805. 
Do, V.-T., et al. (2024). Automatic prompt selection for large language models. arXiv preprint 
arXiv:2404.02717. Retrieved from https://arxiv.org/abs/2404.02717 
Doan, N. N., Harma, A., Celebi, R., & Gottardo, V. (2024). A hybrid retrieval approach for advancing 
retrieval-augmented generation systems. Proceedings of the 2024 International Conference on 
Natural 
Language 
and 
Speech 
https://aclanthology.org/2024.icnlsp-1.41.pdf 
Processing. 
Retrieved 
from 
Feng, J., Tao, C., Geng, X., Shen, T., Xu, C., Long, G., Zhao, D., & Jiang, D. (2024). Synergistic 
interplay between search and large language models for information retrieval. Proceedings of 
the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long 
Papers) 
(pp. 
9571–9583). 
Association 
https://aclanthology.org/2024.acl-long.517/ 
for 
Computational 
Linguistics. 
Frost, J. (2023, July 30). Wilcoxon signed rank test explained. Statistics by Jim. Retrieved from 
https://statisticsbyjim.com/hypothesis-testing/wilcoxon-signed-rank-test/ 
Gao, L., Dai, Z., & Callan, J. (2021). COIL: Revisit exact lexical match in information retrieval with 
contextualized inverted list. Proceedings of the 2021 Conference of the North American 
Chapter of the Association for Computational Linguistics: Human Language Technologies, 
3030–3042. Retrieved from https://www.cs.cmu.edu/~callan/Papers/naacl21-Luyu-Gao.pdf 
Gao, L., Dai, Z., Chen, T., Fan, Z., Van Durme, B., & Callan, J. (2020). Complementing lexical 
retrieval with semantic residual embedding. arXiv preprint arXiv:2004.13969. Retrieved from 
https://arxiv.org/abs/2004.13969 
Google Cloud. (2024). Cloud Vision API documentation. https://cloud.google.com/vision/docs/ 
` 
Gupta, A., Jain, N., & Verma, R. (2018). Deep learning techniques for automatic information extraction 
from PDF documents. Journal of Data Science and Applications, 14(2), 47–58. 
https://doi.org/10.1007/s10844-018-0482-x 
Hsain, F., & El Housni, Z. (2024). Chatbot technology in higher education: Leveraging LangChain and 
GPT for internationalization and digital transformation. arXiv preprint arXiv:2403.14702. 
Retrieved from https://arxiv.org/abs/2403.14702 
Huang, A. (2008). Similarity measures for text document clustering. In Proceedings of the Sixth New 
Zealand Computer Science Research Student Conference (NZCSRSC), Christchurch, New 
Zealand (pp. 49–56). 
Huang, P.-S., et al. (2020). Embedding-based retrieval in Facebook search. arXiv preprint 
arXiv:2006.11632. 
Huh, S., Kim, J., & Park, S. H. (2023). Generating breast ultrasound reports using LangChain for 
standardized medical documentation. arXiv preprint arXiv:2312.03013. Retrieved from 
https://arxiv.org/abs/2312.03013 
Jeong, S., Baek, J., Cho, S., Hwang, S. J., & Park, J. C. (2024). Adaptive-RAG: Learning to adapt 
retrieval-augmented large language models through question complexity. arXiv preprint 
arXiv:2403.14403. Retrieved from https://arxiv.org/abs/2403.14403 
Jurafsky, D., & Martin, J. (2024). Speech and Language Processing An Introduction to Natural 
Language Processing, Computational Linguistics, and Speech Recognition with Language 
Models Third Edition draft. https://web.stanford.edu/~jurafsky/slp3/ed3book_Jan25.pdf 
Klink, S., Kise, K., Dengel, A., Junker, M., & Agne, S. (2007). Document information retrieval. In 
Advances 
in 
pattern 
https://doi.org/10.1007/978-1-84628-726-8_16 
recognition 
(pp. 
351–378). 
Kuzi, S., Zhang, M., Li, C., Bendersky, M., & Najork, M. (2020). Leveraging semantic and lexical 
matching to improve the recall of document retrieval systems: A hybrid approach. arXiv 
preprint arXiv:2010.01195. Retrieved from https://arxiv.org/abs/2010.01195 
LangChain Team. (2022). LangChain documentation: Retrieval-augmented generation. Retrieved from 
https://python.langchain.com/docs/tutorials/rag/ 
LangChain Team. (2023). LangChain documentation. https://python.langchain.com/docs/  
` 
LangChain. (2024b). MapReduce summarization with LangGraph. LangChain Docs. 
https://python.langchain.com/docs/expression_language/cookbook/map_reduce_summarizatio
 n 
LangChain. (2024a). Text splitters: RecursiveCharacterTextSplitter. LangChain Documentation. 
https://python.langchain.com/docs/modules/data_connection/text_splitters/ 
LangSmith. 
(2024). 
LangSmith 
tutorial: 
https://python.langchain.com/docs/tutorials/rag/  
Tracing 
RAG 
applications. 
Leung, K. (2021, June 24). Evaluate OCR Output Quality with Character Error Rate (CER) and Word 
Error 
Rate 
(WER). 
Medium; 
TDS 
Archive. 
https://medium.com/data-science/evaluating-ocr-output-quality-with-character-error-rate-cer-a
 nd-word-error-rate-wer-853175297510 
Liddy, E. D. (2005). Document retrieval, automatic. New York, NY: Syracuse University. 
Livathinos, C., Parra, M., & Lopes, H. (2021). Recovering document structure from PDF data using 
neural 
networks. 
arXiv 
https://arxiv.org/abs/2102.09395 
LlamaIndex. 
(2023). 
Introducing 
preprint 
arXiv:2102.09395. 
Retrieved 
from 
RAGs: Personalized ChatGPT over your data. 
https://www.llamaindex.ai/blog/introducing-rags-your-personalized-chatgpt-experience-over-y
 our-data-2b9d140769b1  
Ma, X., Wang, L., Yang, N., Wei, F., & Lin, J. (2024). Fine-tuning LLaMA for multi-stage text 
retrieval. Proceedings of the 2024 ACM SIGIR Conference on Research and Development in 
Information 
Retrieval. 
Retrieved 
https://cs.uwaterloo.ca/~jimmylin/publications/Ma_etal_SIGIR2024.pdf 
from 
Macdonald, C., & Tonellotto, N. (2020). Declarative experimentation in information retrieval using 
PyTerrier. Proceedings of the 2020 ACM SIGIR on International Conference on Theory of 
Information Retrieval, 161–168. https://doi.org/10.1145/3409256.3409829 
Malve, A., & Chawan, P. M. (2015). A comparative study of keyword and semantic-based search 
engines. ResearchGate. https://doi.org/10.15680/IJIRSET.2015.0411039 
Manning, C. D., Raghavan, P., & Schütze, H. (2008). Introduction to information retrieval. Cambridge 
University Press. 
` 
Marker Project. (n.d.). VikParuchuri/marker: Convert PDF to markdown + JSON (Version 2). GitHub. 
https://github.com/VikParuchuri/marker 
Marker Project. (n.d.). Marker pipeline architecture and Surya integration. GitHub Issues. 
https://github.com/VikParuchuri/marker/issues/123 
Mathew, E., Karthikeyan, L., & Senthil, B. M. (2020). Keyword-based text document retrieval system. 
i-Manager's Journal on Information Technology, 9(4), 1. 
Meta AI. (2025). Llama 3 release notes. https://ai.meta.com/blog/llama-3/  
Meuschke, N., Schubotz, M., & Gipp, B. (2023). A benchmark of PDF information extraction tools 
using a multi-task and multi-domain evaluation. Proceedings of the 16th ACM/IEEE-CS Joint  
Microsoft. (2024). Partitioning large documents into smaller chunks. Microsoft Learn. 
https://learn.microsoft.com/azure/search/vector-search-how-to-chunk-documents  
Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Efficient estimation of word representations in 
vector space. arXiv preprint arXiv:1301.3781. 
Mindanao State University - Iligan Institute of Technology. (n.d.-a). IIT Docs. Retrieved from 
https://repository.msuiit.edu.ph/bor/index.php 
Mindanao State University - Iligan Institute of Technology. (n.d.-b). IIT Docs. Retrieved from 
https://myiit.msuiit.edu.ph/my/v2/apps/iitdocs/index.php?ref=home 
Moran, K. (2023). Qualitative Usability Testing: Study Guide (K. Moran, Ed.). Nielsen Norman Group. 
https://www.nngroup.com/articles/qual-usability-testing-study-guide/#:~:text=In%20a%20usa
 bility%2Dtesting%20session,behavior%20and%20listens%20for%20feedback. 
Neon Tech. (2023, October 18). Understanding vector search and HNSW index with pgvector. Neon 
Blog. https://neon.tech/blog/understanding-vector-search-and-hnsw-index-with-pgvector  
Okon, G., Umoren, E. E., & Philips, K. (n.d.). Academic records management systems (ARMS) and 
students’ 
academic 
records 
DigitalCommons@University 
of 
maintenance 
Nebraska 
https://digitalcommons.unl.edu/libphilprac/7936/ 
OpenAI. 
(2024). 
OpenAI 
embeddings 
https://platform.openai.com/docs/guides/embeddings 
in - 
Nigerian 
Lincoln. 
universities. 
Retrieved 
API 
from 
documentation. 
` 
Palm, R., Bertelsen, N., & Foged, T. (2017). Machine learning approaches to document layout 
recognition in PDFs. Proceedings of the International Conference on Document Analysis and 
Recognition (ICDAR), 567–572. https://doi.org/10.1109/icdar.2017.89 
Pandya, S., & Holia, R. (2023). Automating customer service with LangChain: A custom open-source 
GPT 
chatbot. 
arXiv 
https://arxiv.org/abs/2310.05421 
preprint 
arXiv:2310.05421. 
Retrieved 
from 
Parsio. (2023). 5 effective techniques for extracting information from PDF documents. Retrieved from 
https://parsio.io/blog/5-effective-techniques-for-extracting-information-from-pdf-documents/ 
Paruchuri, V. (2024a). Surya: OCR, layout analysis, reading order, table recognition in 90+ languages 
[Computer software]. GitHub. https://github.com/VikParuchuri/surya 
Paruchuri, V. (2024b). Marker: Markdown converter for structured document data [Computer 
software]. GitHub. https://github.com/VikParuchuri/marker 
Patel, R., Smith, J., & Kumar, P. (2019). Challenges in information retrieval systems: A review of 
keyword-based limitations. Journal of Digital Information Management, 17(1), 25–31. 
pgvector Contributors. (2023). pgvector: Open-source vector similarity search for Postgres 
[Repository]. GitHub. https://github.com/pgvector/pgvector  
Pinecone. 
(2023, 
June 
30). 
Chunking 
strategies 
https://www.pinecone.io/learn/chunking-strategies/  
for 
LLM applications. 
Powell, M. (2023, September 6). Document retrieval and search techniques. CPO Magazine. Retrieved 
from https://www.cpomagazine.com/tech/document-retrieval-and-search-techniques/ 
Prajna AI Wisdom. (2024, February). Semantic chunking in RAG: Balancing context and relevance. 
https://prajnaaiwisdom.medium.com/semantic-chunking-in-rag-balancing-context-and-relevan
 ce-2325451b4507  
Sarmah, B., Hall, B., Rao, R., Patel, S., & Mehta, D. (2024). HybridRAG: Integrating knowledge 
graphs and vector retrieval augmented generation for efficient information extraction. arXiv 
preprint arXiv:2408.04948. Retrieved from https://arxiv.org/abs/2408.04948 
Sauro, J. (2018, September 19). MeasuringU: 5 Ways to Interpret a SUS Score. Measuringu.com. 
https://measuringu.com/interpret-sus-score/ 
` 
P. 
(2023). 
Building 
LLM-Powered Applications: An End-to-End Guide. 
Sinha, 
https://medium.com/@pallavisinha12/building-llm-powered-applications-an-end-to-end-guide-dd3ea8dddd8b 
Six, J. M., & Macefield, R. (2016, January 4). How to Determine the Right Number of Participants for 
Usability 
Studies 
:: 
UXmatters. 
Www.uxmatters.com. 
https://www.uxmatters.com/mt/archives/2016/01/how-to-determine-the-right-number-of-partic
 ipants-for-usability-studies.php 
Suh, J., Lee, Y., & Park, M. (2024). A conversational agent for promoting cultural awareness in Seoul 
using 
LangChain. 
arXiv 
https://arxiv.org/abs/2402.06929 
preprint 
arXiv:2402.06929. 
Retrieved 
from 
Tembo. (2023, February 15). Vector indexes in Postgres using pgvector: IVFFlat vs HNSW. Tembo 
Learn. https://tembo.io/blog/vector-indexes-in-pgvector  
Thakur, N., Reimers, N., Rücklé, A., Srivastava, A., & Gurevych, I. (2021). BEIR: A heterogeneous 
benchmark for zero-shot evaluation of information retrieval models. arXiv preprint 
arXiv:2104.08663. 
TryChroma. (2023a). Evaluating chunking strategies for retrieval-augmented generation (RAG). 
Chroma Research Blog. https://research.trychroma.com/evaluating-chunking 
TryChroma. (2023b). Top-K retrieval and vector filtering strategies. Chroma Research Blog. 
https://research.trychroma.com/vector-search-topk-filtering 
Uddin, M. S., & Zhuang, H. (2021). Enhancing search systems with semantic technologies: A case for 
academic institutions. Information Retrieval Journal, 24(2), 97–115. 
Unstructured. 
(2024). 
Chunking 
for 
RAG: 
https://www.unstructured.io/blog/chunking-for-rag  
Best 
practices. 
Unstructured.io. 
Versatile-OCR-Program. (n.d.). OCR preprocessing pipelines for ML training. GitHub. 
https://github.com/ses4255/Versatile-OCR-Program 
Wang, J., Lee, S., Zhang, H., & Chen, T. (2022). Enhancing retrieval systems with LangChain: A new 
paradigm for information processing. arXiv preprint arXiv:2205.11815. Retrieved from 
https://arxiv.org/abs/2205.11815 
Wei, X., et al. (2023). ChatIE: Zero-shot information extraction via chatting with ChatGPT. arXiv 
preprint arXiv:2302.10205. Retrieved from https://arxiv.org/abs/2302.10205 
` 
Winslett, C. (2023, May). Performance Tips Using Postgres and pgvector | Crunchy Data Blog. 
Crunchy Data. https://www.crunchydata.com/blog/pgvector-performance-for-developers 
Xu, D., et al. (2023). Large language models for generative information extraction: A survey. Frontiers 
of 
Computer 
Science. 
https://link.springer.com/article/10.1007/s11704-024-40555-y 
Retrieved 
from 
Xu, J., et al. (2024). ChatUIE: Exploring chat-based unified information extraction using large 
language models. Proceedings of the 2024 Joint International Conference on Computational 
Linguistics, 
Language 
Resources 
https://aclanthology.org/2024.lrec-main.279/ 
and 
Evaluation. 
Retrieved 
from 
Yoon, J., Arik, S. O., Chen, Y., & Pfister, T. (2023). Search-Adaptor: Embedding customization for 
information 
retrieval. 
arXiv 
https://arxiv.org/abs/2310.08750 
preprint 
arXiv:2310.08750. 
Retrieved 
from 
Zhan, J., Mao, J., Liu, Y., Zhang, M., & Ma, S. (2020). RepBERT: Contextualized text embeddings for 
first-stage retrieval. arXiv preprint arXiv:2006.15498. 
Zhao, L., & Callan, J. (2010). Term necessity prediction. Proceedings of the 19th ACM Conference on 
Information and Knowledge Management (pp. 259–268). 
Zhu, Y., Yuan, H., Wang, S., Liu, J., Liu, W., Deng, C., Chen, H., Dou, Z., & Wen, J.-R. (2023). Large 
language models for information retrieval: A survey. arXiv preprint arXiv:2308.07107. 
Retrieved from https://arxiv.org/abs/2308.07107 
Zilliz. (2023). A guide to chunking strategies for Retrieval-Augmented Generation (RAG). 
https://zilliz.com/learn/guide-to-chunking-strategies-for-rag 
Çöplü, T., et al. (2024). Prompt-time symbolic knowledge capture with large language models. arXiv 
preprint arXiv:2402.00414. Retrieved from https://arxiv.org/abs/2402.00414 
` 
Appendix C Personal Vitae 
Name: Carlo P. Arellano 
Email: carlo.arellano@g.msuiit.edu.ph 
Mobile: +639165391190 
Name: Michael James M. Carnaje 
Email: michaeljames.carnaje@g.msuiit.edu.ph 
Mobile: +639567313009 
Name: Fulgent Kvasir E. Lavesores 
Email: fulgentkvasir.lavesores@g.msuiit.edu.ph 
Mobile: +639919031930