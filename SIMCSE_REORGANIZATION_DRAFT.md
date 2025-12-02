# SimCSE Architecture Implementation - Reorganization Draft

## 4.3.2 SimCSE Architecture Implementation

The SimCSE architecture forms the core of Consol's semantic similarity assessment, implementing sophisticated contrastive learning mechanisms optimized for educational content evaluation. Figure \ref{fig:simcse_architecture} illustrates the complete SimCSE processing pipeline from input tokenization through embedding generation to similarity computation, demonstrating the systematic flow from training phase through local deployment to inference and response generation.

### 4.3.2.1 Training Phase (Pre-trained at Princeton NLP)

The SimCSE model implementation in Consol utilizes a pre-trained model developed at Princeton NLP, implementing contrastive learning mechanisms for robust sentence representation. The training phase, completed prior to system deployment, establishes the foundational capabilities for educational content assessment.

#### 4.3.2.1.1 Large Text Corpus Foundation (Step 1-2)

The training process begins with large-scale text corpus preparation using datasets including Wikipedia, BookCorpus, and educational text collections. The corpus undergoes preprocessing to ensure educational domain relevance while maintaining diverse linguistic patterns essential for robust similarity assessment. The foundation utilizes BERT-base-uncased as the base model, providing 12 transformer layers, 768 hidden dimensions, and 110M parameters optimized for English language processing.

#### 4.3.2.1.2 Contrastive Learning Setup (Step 3)

The contrastive learning mechanism employs dropout as a data augmentation strategy, creating positive pairs from identical sentences with different dropout masks while treating all other sentences in the batch as negative examples. This approach eliminates the need for manually curated positive and negative pairs, enabling scalable training on educational content without extensive annotation requirements.

#### 4.3.2.1.3 Loss Function and Optimization (Step 4-5)

The training employs the contrastive loss function:

$$\ell_i = -\log \frac{e^{\text{sim}(h_i, h_i^+)/\tau}}{\sum_{j=1}^{N} e^{\text{sim}(h_i, h_j^+)/\tau}}$$

where $h_i$ represents the hidden representation of input sentence $i$, $h_i^+$ denotes the positive sample (same sentence with different dropout), $\text{sim}(\cdot,\cdot)$ computes cosine similarity, $\tau$ is the temperature parameter, and $N$ represents the batch size. Model training optimizes sentence embeddings through this contrastive objective, resulting in the final SimCSE model with enhanced semantic understanding capabilities.

#### 4.3.2.1.4 Pre-trained Model Output (Step 6)

The training phase produces the final SimCSE model (unsup-simcse-bert-base-uncased) that demonstrates superior performance on semantic similarity tasks. This pre-trained model serves as the foundation for Consol's local deployment, providing robust sentence embedding capabilities without requiring additional fine-tuning for educational content assessment.

### 4.3.2.2 Local Deployment Phase 

The local deployment phase transforms the pre-trained SimCSE model into an operational component within Consol's architecture, enabling real-time similarity assessment for educational content evaluation.

#### 4.3.2.2.1 Model Download and Storage (Step 7-8)

The deployment process begins with downloading the pre-trained model from HuggingFace repositories using the identifier `princeton-nlp/unsup-simcse-bert-base-uncased`. The model files, including `config.json`, `model.safetensors`, tokenizer configurations, and vocabulary mappings, are stored locally in the `./simcse-model/` directory to ensure consistent access and eliminate runtime dependencies on external model repositories.

#### 4.3.2.2.2 Flask Server Initialization (Step 9)

The SimCSE capabilities are exposed through a Python Flask microservice running on port 5000, providing RESTful API endpoints for similarity computation. The server implements Cross-Origin Resource Sharing (CORS) configuration to enable secure communication with the Next.js frontend, while maintaining separation between natural language processing and web application concerns.

#### 4.3.2.2.3 Model Loading and Tokenizer Setup (Step 10-11)

Upon server initialization, the system loads the AutoTokenizer and AutoModel components from the local model directory. The tokenizer handles text preprocessing, including special token insertion, vocabulary mapping, and sequence formatting, while the model provides the transformer architecture for embedding generation. Both components are loaded globally to prevent repeated initialization overhead during similarity computations.

#### 4.3.2.2.4 Server Readiness (Step 12)

The deployment phase concludes with the Flask server achieving operational readiness on port 5000, exposing the `/score` endpoint for similarity computation and the `/upload-file` endpoint for document preprocessing. The server maintains persistent model state to ensure consistent response times for educational assessment scenarios.

### 4.3.2.3 Inference Phase (Two-Sentence Processing)

The inference phase processes user input through systematic text preparation, model computation, and similarity assessment, transforming raw educational content into meaningful assessment scores.

#### 4.3.2.3.1 Input Processing (Step 13)

The inference process receives two text inputs: the reference note content and the student's recalled text. Input validation ensures both texts are provided and contain meaningful content suitable for similarity assessment. The system handles various text formats while maintaining content integrity essential for accurate educational evaluation.

#### 4.3.2.3.2 Tokenization Process (Step 14a-14d)

Text tokenization transforms input sentences into model-compatible format through systematic preprocessing stages:

**Step 14a - Basic Preprocessing:** Input text undergoes lowercase conversion, special character normalization, and whitespace standardization to ensure consistent token generation across diverse input formats.

**Step 14b - WordPiece Tokenization:** The tokenizer applies WordPiece segmentation, splitting words into subword units that handle out-of-vocabulary terms while maintaining semantic coherence essential for educational content assessment.

**Step 14c - Sequence Formatting:** Token sequences receive special token insertion, including [CLS] tokens for sentence representation and [SEP] tokens for sequence boundaries, following BERT's expected input format for optimal model performance.

**Step 14d - Attention Masks:** The system generates attention masks distinguishing actual tokens from padding tokens, ensuring the model focuses computational resources on meaningful content rather than padding artifacts during embedding generation.

#### 4.3.2.3.3 Model Forward Pass (Step 15a-15d)

The tokenized sequences undergo transformer processing through BERT's architecture:

**Step 15a - Input Embeddings:** Token IDs convert to 768-dimensional embeddings through the vocabulary mapping, providing rich semantic representations for each token in the educational content.

**Step 15b - Positional Encoding:** Position information integrates with token embeddings to preserve word order relationships essential for semantic understanding in educational contexts.

**Step 15c - Transformer Layers:** Twelve multi-head attention layers process the embedded sequences, capturing complex linguistic patterns and semantic relationships through self-attention mechanisms optimized for contrastive learning objectives.

**Step 15d - Hidden State Output:** The model generates hidden states with batch_size × sequence_length × 768 dimensions, providing comprehensive token-level representations ready for sentence-level aggregation.

#### 4.3.2.3.4 Embedding Extraction (Step 16a-16b)

Sentence representation extraction utilizes BERT's [CLS] token strategy:

**Step 16a - CLS Token Selection:** The system extracts embeddings from position 0 of each sequence, corresponding to the [CLS] token that aggregates information from all sequence tokens through attention mechanisms.

**Step 16b - Sentence Embeddings:** The extracted [CLS] embeddings provide 768-dimensional sentence representations (embedding1 and embedding2) that capture semantic content essential for educational similarity assessment.

### 4.3.2.4 Similarity Computation and Response

The final processing phase transforms sentence embeddings into educational assessment scores through mathematical computation and threshold-based evaluation.

#### 4.3.2.4.1 Cosine Similarity Calculation (Step 17a-17b)

**Step 17a:** The system computes cosine similarity between the two sentence embeddings using the formula:

$$\text{similarity} = \frac{\mathbf{A} \cdot \mathbf{B}}{||\mathbf{A}|| \times ||\mathbf{B}||}$$

where $\mathbf{A}$ and $\mathbf{B}$ represent the 768-dimensional embeddings for the reference and recalled content respectively.

**Step 17b:** The cosine similarity produces a normalized score between 0.0 and 1.0, providing a standardized measure of semantic similarity suitable for educational assessment interpretation.

#### 4.3.2.4.2 Scoring and Threshold Evaluation (Step 18a-18b)

**Step 18a - Star Thresholds:** The similarity score undergoes threshold evaluation to determine star ratings:
- ≥0.81: 3 stars (Excellent understanding)
- ≥0.60: 2 stars (Good recall with minor gaps)
- ≥0.44: 1 star (Basic understanding requiring improvement)
- <0.44: 0 stars (Significant improvement needed)

**Step 18b:** The final result combines the numerical similarity score with the categorical star rating, providing both precise measurement and interpretable feedback for educational assessment.

#### 4.3.2.4.3 Response Generation (Step 19-21)

**Step 19 - JSON Response:** The system formats assessment results as JSON response containing similarity score, star rating, and processing metadata for frontend consumption.

**Step 20-21 - Frontend Integration:** The response enables immediate feedback display in the user interface while supporting database storage for learning analytics and progress tracking across multiple assessment sessions.

## Technical Implementation Considerations

### Temperature Parameter Configuration

The temperature parameter $\tau = 0.05$ controls the sharpness of the similarity distribution in the contrastive learning formula. This calibration balances discriminative power with generalization ability, preventing over-confident predictions that could lead to poor assessment reliability in educational contexts.

### Encoder Design Rationale

The architectural choice of [CLS] pooling over mean pooling is motivated by: 1) concentrated representation where the [CLS] token is specifically designed to encode sentence-level information, 2) computational efficiency where single token extraction requires less processing than mean aggregation, and 3) empirical performance where previous studies demonstrate superior results for similarity tasks.

### 768-Dimensional Embedding Structure

The semantic vector representation employs structured organization: dimensions 1-200 focus on syntactic patterns, dimensions 201-300 capture semantic relationships, dimensions 301-500 represent domain knowledge, and dimensions 501-768 encode contextual understanding essential for educational assessment accuracy.