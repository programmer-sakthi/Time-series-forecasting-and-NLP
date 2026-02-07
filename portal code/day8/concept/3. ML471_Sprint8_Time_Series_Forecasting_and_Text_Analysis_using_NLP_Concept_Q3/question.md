Multi File Programming Question
Problem Overview 



system to measure similarity and relationships between words and documents using word embeddings. Before implementing advanced semantic search, document clustering, or recommendation systems, the team must build a foundation using word vectors and cosine similarity metrics. 



As the core component of this semantic analysis pipeline, the team needs to: 



Load and preprocess documents – Clean and normalize a collection of news articles by converting to lowercase, removing special characters, and standardizing whitespace. Display the cleaned documents to verify preprocessing quality. 
Generate word vectors – Extract dense vector representations for individual words using pre-trained word embeddings from spaCy. Display sample word vectors to understand the dimensionality and numerical representation of semantic meaning. 
Compute document embeddings – Generate document-level vector representations by aggregating word vectors. Display embedding shapes to verify successful vectorization of all documents. 
Calculate cosine similarity – Measure semantic similarity between documents and between words using cosine similarity metrics. Display similarity matrices to identify semantically related content. 
Analyze word relationships – Compute pairwise similarity between words in a test sentence to understand semantic relationships captured by word embeddings. 


This semantic analysis forms the foundation for subsequent NLP tasks including semantic search, document clustering, content recommendation, and similarity-based retrieval systems. 



The input file contains unstructured sports news articles separated by delimiters. Each article includes: 



Article title/heading 
Article body with multiple paragraphs 
Separator lines (dashes) between articles 


Sample Data 



News Article 1 

 

Claxton hunting first major medal 

 

British hurdler Sarah Claxton is confident she can win her first major medal at next month's European Indoor Championships in Madrid...

Input format :
Text File Input: 

The program prompts the user with: "Enter sports news text file name: " 
Input must include the file extension .txt 
File should be located in the same directory as the Python script 
File must be UTF-8 encoded 


Output format :
The program generates the following outputs in sequence: 



1. Cleaned Documents: 

Displays preprocessed documents numbered sequentially (1, 2, 3, ...) 
Format: {number}: {cleaned_text} 
Shows lowercase text with special characters removed 
Followed by a blank line separator 


2. Word Vector for 'king': 

Displays the first 10 dimensions of the word vector 
Format: NumPy array output showing floating-point values 
Example: [-0.123, 0.456, -0.789, ...] 
Followed by a blank line separator 


3. Document Embedding Shape: 

Displays the shape of the document embedding matrix 
Format: Document Embedding Shape: (num_documents, vector_dimensions) 
Example: (4, 300) for 4 documents with 300-dimensional vectors 
Followed by a blank line separator 


4. Cosine Similarity Between Documents: 

Displays a symmetric similarity matrix rounded to 3 decimal places 
Format: NumPy 2D array with values between -1 and 1 
Diagonal values are 1.000 (self-similarity) 
Followed by a blank line separator 


5. Word Similarity Matrix: 

Displays pairwise similarity scores between words with valid vectors 
Format: {word1} ↔ {word2} : {similarity_score} 
Only shows upper triangle pairs (j > i) to avoid duplicates 
Similarity scores rounded to 3 decimal places 
Followed by a blank line separator 


6. Observations: 

Provides interpretive insights about the similarity results 
Explains semantic relationships (e.g., 'dog' and 'cat' similarity) 
Notes out-of-vocabulary (OOV) word handling 
Compares embeddings to traditional methods like TF-IDF 


Refer to the sample output for exact formatting specifications. 

Code constraints :
Library Requirements: 

The program uses spaCy library for NLP processing and word vectors 
Requires the en_core_web_sm language model to be installed 
If the spaCy model is not found, the program raises a RuntimeError with installation instructions:  
"No spaCy English model found." 
"Install one using: python -m spacy download en_core_web_sm" 
Uses scikit-learn for cosine similarity calculations 
Uses NumPy for numerical operations and array handling 


Environment Configuration: 

TensorFlow warnings are suppressed via environment variable TF_CPP_MIN_LOG_LEVEL = '2' 
Environment variable must be set before importing TensorFlow-dependent libraries 


Text Processing Constraints: 

Text cleaning converts all text to lowercase using .lower() 
Removes all non-alphabetic characters except spaces using regex r"[^a-z\s]" 
Collapses multiple whitespace into single spaces using regex r"\s+" 
Strips leading and trailing whitespace using .strip() 
Empty or whitespace-only documents are filtered out 


Vector Processing Constraints: 

Default vector size is obtained from spaCy's vocabulary or defaults to 300 dimensions 
Words without pre-trained vectors are represented as zero vectors using np.zeros(VECTOR_SIZE) 
Document embeddings use batch processing via nlp.pipe() for efficiency 
Document vectors are stacked vertically using np.vstack()


Similarity Computation Constraints: 

Word similarity requires at least 2 words with valid (non-zero) vectors 
If fewer than 2 valid words exist, returns None for similarity matrix 
Cosine similarity values range from -1 (opposite) to 1 (identical) 
Similarity matrices are symmetric with diagonal values of 1.0 


Output Constraints: 

Document numbering starts from 1 (not 0) 
Word vectors display only first 10 dimensions for readability 
Similarity scores are rounded to 3 decimal places using np.round(_, 3) 
Word similarity displays only upper triangle pairs to avoid redundancy 
All print statements must match the exact format shown in the sample output, including spacing and line breaks 
Sample test cases :
Input 1 :
Sample.txt
Output 1 :

Cleaned Documents:
1: news article
2: ad sales boost time warner profit
3: quarterly profits at us media giant timewarner jumped to bn m
4: time warner said on friday that it now owns of searchengine google

Word Vector for 'king' (first 10 dims):
[ 1.2150608   0.747154   -0.04534233 -0.59702456  0.62348014  0.915103
 -0.032897   -0.5459178   1.5112422  -1.123439  ]

Document Embedding Shape: (4, 96)

Cosine Similarity Between Documents:
[[1.    0.593 0.392 0.314]
 [0.593 1.    0.57  0.387]
 [0.392 0.57  1.    0.381]
 [0.314 0.387 0.381 1.   ]]

Word Similarity Matrix (words with vectors):
dog ↔ cat : 0.641
dog ↔ car : 0.748
dog ↔ skym : 0.410
dog ↔ apple : 0.590
cat ↔ car : 0.662
cat ↔ skym : 0.504
cat ↔ apple : 0.700
car ↔ skym : 0.453
car ↔ apple : 0.763
skym ↔ apple : 0.412

Observations:
• 'dog' and 'cat' have high similarity due to both being animals.
• 'car' is moderately similar to 'dog' and 'cat' due to physical object context.
• 'skym' may be OOV → low similarity with other words.
• Embeddings capture meaning beyond frequency (unlike TF-IDF).