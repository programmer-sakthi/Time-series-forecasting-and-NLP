Multi File Programming Question
Problem Overview 



A data science team is developing a text preprocessing and feature extraction pipeline for a sports news analysis system. The raw text contains unstructured content with noise such as stop words, punctuation, and inconsistent capitalization, which can impact the performance of downstream text mining algorithms. To prepare the data for tasks like classification, clustering, and similarity analysis, the team must implement a multi‑faceted feature extraction approach that includes Bag‑of‑Words, TF‑IDF, and word embeddings. 



The team needs to preprocess the text by removing noise, extracting meaningful tokens, and generating multiple numerical representations to analyze word importance and semantic meaning across several sports news articles. 



Objectives 



As part of this text preprocessing and feature extraction task, the team needs to: 



Load and preview the text file – Import the sports news text file and display the first 300 characters to verify successful data loading and understand content structure. 
Load spaCy model – Initialize the spaCy English model for text processing. 
Preprocess text – Clean text by converting to lowercase and removing stop words, punctuation, and whitespace tokens. 
Generate Bag‑of‑Words matrix – Use CountVectorizer to create a word‑frequency representation of the cleaned documents. 
Generate TF‑IDF matrix – Use TfidfVectorizer to create a TF‑IDF representation that highlights important terms across documents. 
Generate word embeddings – Use spaCy’s pre‑trained model to produce dense vector representations for each document. 
Display TF‑IDF features and values – Show the vocabulary (feature names) and IDF values for each term. 
Display TF‑IDF matrix – Show the TF‑IDF matrix as a numerical array where rows represent documents and columns represent words. 
Compare vector shapes – Output the dimensions of BoW, TF‑IDF, and embedding matrices. 
Compute cosine similarity – Calculate and display cosine similarity matrices for BoW, TF‑IDF, and embedding representations to compare document relationships. 
Summarize observations – Provide insights on the differences between frequency‑based and semantic‑based representations. 

This analysis will help the team transform unstructured sports news into structured, multi‑view numerical data suitable for machine learning models. 



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



Original Text Sample 

Displays the first 300 characters of the loaded text content. 
Preceded by the header: === Original Text Sample (First 300 chars) === 
Followed by a blank line. 


Cleaned Text Sample 

Displays the first 50 cleaned tokens. 
Preceded by the header: === Cleaned Text Sample === 
Followed by a blank line. 


TF‑IDF Features 

Displays all vocabulary words. 
Preceded by the header: === TF‑IDF Features === 
Followed by a blank line. 


IDF Values 

Displays each word and its IDF value. 
Preceded by the header: === IDF Values === 
Each line format: word : idf_value 
Followed by a blank line. 


TF‑IDF Matrix 

Displays the TF‑IDF matrix as a DataFrame rounded to 4 decimal places. 
Preceded by the header: === TF‑IDF Matrix === 
Followed by a blank line. 


Word Embedding Vectors 

Displays the dense embedding matrix for each document. 
Preceded by the header: === Word Embedding Vectors === 
Followed by a blank line. 


Vector Shapes 

Shows dimensions of BoW, TF‑IDF, and embedding matrices. 
Preceded by the header: === Vector Shapes === 
Followed by a blank line. 


Cosine Similarity Matrices 

Displays cosine similarity for BoW, TF‑IDF, and embedding representations. 
Preceded by respective headers: 
=== Cosine Similarity (BoW) === 
=== Cosine Similarity (TF‑IDF) === 
=== Cosine Similarity (Embeddings) === 
Each followed by a blank line. 


Observations 

Summarizes key differences between the three feature extraction methods. 
Preceded by the header: === Observations === 
﻿

Refer to the sample output for exact formatting specifications. 

Code constraints :
File Constraints: 

File must be a valid text file with .txt extension. 
File must exist in the same directory as the Python script (using sys.path[0]). 
File encoding must be UTF‑8 compatible. 
If the file is not found, the program prints: 
Error: File '{filename}' not found. 
and exits with status code 1. 


Library Requirements: 

The program uses spaCy for text processing and word embeddings. 
Requires en_core_web_sm language model to be installed. 
If the spaCy model is not found, the program prints installation instructions and exits. 
Uses scikit‑learn’s CountVectorizer and TfidfVectorizer. 
Uses spaCy’s built‑in stop words list for filtering. 


Processing Constraints: 

Warnings are suppressed using warnings.simplefilter(action='ignore'). 
TensorFlow warnings are suppressed via environment variable TF_CPP_MIN_LOG_LEVEL = '3'. 
Text preprocessing includes: 
Converting to lowercase. 
Removing stop words using spaCy’s is_stop. 
Removing punctuation tokens. 
Removing whitespace tokens. 
Documents are stored in a list for vectorization. 


Vectorization Constraints: 

CountVectorizer and TfidfVectorizer are used without custom parameters (default settings). 
Vocabulary is built from all cleaned documents. 
IDF values are extracted using vectorizer.idf_. 
Feature names are extracted using vectorizer.get_feature_names(). 
Word embeddings are generated via nlp(doc).vector. 


Output Constraints: 

The original text preview displays exactly the first 300 characters using slicing content[:300]. 
The cleaned text preview displays exactly the first 50 cleaned tokens. 
TF‑IDF matrix is displayed using pd.DataFrame rounded to 4 decimal places. 
All section headers use === for emphasis. 
Blank lines separate all major output sections. 
All print statements match the exact format shown in the solution code. 
Sample test cases :
Input 1 :
Sample.txt
Output 1 :
Enter sports news text file name: 
=== Original Text Sample (First 300 chars) ===
News Article 1

Claxton hunting first major medal

British hurdler Sarah Claxton is confident she can win her first major medal at next month's European Indoor Championships in Madrid.

The 25-year-old has already smashed the British record over 60m hurdles twice this season, setting a new mark of 7

=== Cleaned Text Sample ===
['news', 'article', '1', 'claxton', 'hunting', 'major', 'medal', 'british', 'hurdler', 'sarah', 'claxton', 'confident', 'win', 'major', 'medal', 'month', 'european', 'indoor', 'championships', 'madrid', '25', 'year', 'old', 'smashed', 'british', 'record', '60', 'm', 'hurdles', 'twice', 'season', 'setting', 'new', 'mark', '7.96', 'seconds', 'win', 'aaas', 'title', 'confident', 'said', 'claxton', 'race', 'comes', 'long', 'training', 'think', 'chance', 'medal', 'claxton']

=== TF-IDF Features ===
['17', '19', '20', '25', '35', '60', '96', 'aaas', 'agio', 'announced', 'april', 'article', 'athlete', 'athletics', 'attentions', 'australia', 'automatic', 'base', 'birmingham', 'boost', 'born', 'british', 'britton', 'bronze', 'bupa', 'byrne', 'campaign', 'championships', 'chance', 'claxton', 'cobh', 'colchester', 'comes', 'confident', 'contested', 'country', 'course', 'cross', 'currentily', 'dividends', 'domestic', 'dublin', 'equal', 'etienne', 'european', 'event', 'explain', 'fastest', 'favourite', 'fifth', 'fionnualla', 'focused', 'form', 'france', 'grand', 'great', 'hinted', 'hunting', 'hurdler', 'hurdles', 'included', 'indicated', 'indoor', 'indoors', 'international', 'ireland', 'irina', 'jolene', 'jump', 'leap', 'left', 'like', 'likely', 'line', 'london', 'long', 'madrid', 'major', 'marathon', 'march', 'maria', 'mark', 'mccambridge', 'medal', 'month', 'moving', 'national', 'nationals', 'new', 'news', 'official', 'officially', 'old', 'owns', 'participate', 'participation', 'past', 'pays', 'place', 'preparing', 'present', 'previous', 'prix', 'provincial', 'race', 'record', 'regime', 'run', 'runner', 'russian', 'said', 'santry', 'sarah', 'saturday', 'scotland', 'season', 'seasons', 'seconds', 'selected', 'selections', 'setting', 'shevchenko', 'sixth', 'smashed', 'sonia', 'spot', 'st', 'stage', 'struggled', 'success', 'sullivan', 'team', 'teams', 'think', 'time', 'title', 'trailing', 'training', 'translate', 'twice', 'week', 'win', 'won', 'world', 'worlds', 'year', 'years']

=== IDF Values ===
17 : 1.4055
19 : 1.4055
20 : 1.4055
25 : 1.4055
35 : 1.4055
60 : 1.4055
96 : 1.4055
aaas : 1.4055
agio : 1.4055
announced : 1.4055
april : 1.4055
article : 1.0000
athlete : 1.4055
athletics : 1.4055
attentions : 1.4055
australia : 1.4055
automatic : 1.4055
base : 1.4055
birmingham : 1.4055
boost : 1.4055
born : 1.4055
british : 1.4055
britton : 1.4055
bronze : 1.4055
bupa : 1.4055
byrne : 1.4055
campaign : 1.4055
championships : 1.0000
chance : 1.4055
claxton : 1.4055
cobh : 1.4055
colchester : 1.4055
comes : 1.4055
confident : 1.4055
contested : 1.4055
country : 1.4055
course : 1.4055
cross : 1.4055
currentily : 1.4055
dividends : 1.4055
domestic : 1.4055
dublin : 1.4055
equal : 1.4055
etienne : 1.4055
european : 1.4055
event : 1.4055
explain : 1.4055
fastest : 1.4055
favourite : 1.4055
fifth : 1.4055
fionnualla : 1.4055
focused : 1.4055
form : 1.0000
france : 1.4055
grand : 1.4055
great : 1.4055
hinted : 1.4055
hunting : 1.4055
hurdler : 1.4055
hurdles : 1.4055
included : 1.4055
indicated : 1.4055
indoor : 1.4055
indoors : 1.4055
international : 1.4055
ireland : 1.4055
irina : 1.4055
jolene : 1.4055
jump : 1.4055
leap : 1.4055
left : 1.4055
like : 1.4055
likely : 1.4055
line : 1.4055
london : 1.0000
long : 1.0000
madrid : 1.4055
major : 1.4055
marathon : 1.4055
march : 1.0000
maria : 1.4055
mark : 1.4055
mccambridge : 1.4055
medal : 1.4055
month : 1.0000
moving : 1.4055
national : 1.4055
nationals : 1.4055
new : 1.4055
news : 1.0000
official : 1.4055
officially : 1.4055
old : 1.0000
owns : 1.4055
participate : 1.4055
participation : 1.4055
past : 1.4055
pays : 1.4055
place : 1.4055
preparing : 1.0000
present : 1.4055
previous : 1.4055
prix : 1.4055
provincial : 1.4055
race : 1.4055
record : 1.4055
regime : 1.4055
run : 1.4055
runner : 1.4055
russian : 1.4055
said : 1.4055
santry : 1.4055
sarah : 1.4055
saturday : 1.4055
scotland : 1.4055
season : 1.4055
seasons : 1.4055
seconds : 1.4055
selected : 1.4055
selections : 1.4055
setting : 1.4055
shevchenko : 1.4055
sixth : 1.4055
smashed : 1.4055
sonia : 1.4055
spot : 1.4055
st : 1.4055
stage : 1.4055
struggled : 1.4055
success : 1.4055
sullivan : 1.4055
team : 1.4055
teams : 1.4055
think : 1.4055
time : 1.4055
title : 1.4055
trailing : 1.4055
training : 1.0000
translate : 1.4055
twice : 1.4055
week : 1.0000
win : 1.4055
won : 1.0000
world : 1.0000
worlds : 1.4055
year : 1.0000
years : 1.0000

=== TF-IDF Matrix ===
       17      19      20      25  ...   world  worlds    year   years
0  0.0000  0.0000  0.0000  0.1426  ...  0.0507  0.0000  0.1522  0.0507
1  0.0944  0.0944  0.0944  0.0000  ...  0.0672  0.0944  0.0672  0.0672

[2 rows x 147 columns]

=== Word Embedding Vectors ===
[[ 2.57860422e-01  2.39338011e-01 -4.99767251e-02 -7.16769323e-02
  -1.60313621e-01  1.92871511e-01 -1.82966366e-01 -2.37727836e-01
   6.90623522e-01 -8.52414817e-02  2.48107702e-01  6.03994787e-01
   2.09700540e-01 -7.03193724e-01 -1.46460041e-01  1.54236794e-01
   3.36303860e-01 -3.17383409e-02 -2.74984002e-01 -1.21971160e-01
   2.87306935e-01 -4.47122931e-01  2.19564512e-01  1.01751521e-01
   2.70045340e-01 -4.94360439e-02 -4.30632532e-01  1.53200462e-01
  -2.19446644e-01  2.99711078e-01 -1.27210394e-01  2.87383765e-01
  -4.34253097e-01 -4.56211716e-01  3.72355372e-01 -4.50181156e-01
   1.82020180e-02  5.32645226e-01 -5.37793458e-01  2.09685601e-02
   1.59625068e-01  4.00421172e-02  6.27019554e-02 -9.18096900e-01
   3.46900910e-01  5.40515147e-02 -1.69355353e-05  4.16359752e-01
   3.05579603e-01 -2.96293348e-01  3.33541632e-01  4.37914394e-02
  -3.52527708e-01 -1.95172220e-01 -1.52842909e-01  1.10034637e-01
   7.00496614e-01 -3.07780951e-01 -2.36073688e-01  7.23225698e-02
  -1.62899524e-01 -2.66228169e-01  1.78226009e-01 -6.40922904e-01
  -1.21360041e-01 -6.49711907e-01 -2.98021466e-01 -6.54602349e-02
  -1.78822756e-01 -6.90177023e-01  3.25317442e-01  1.07815400e-01
  -9.21567753e-02 -1.41007319e-01 -1.93921663e-02  5.76368153e-01
  -1.31321594e-01  2.36232936e-01 -7.92043090e-01 -7.54714459e-02
  -1.54566690e-01 -6.09519064e-01  3.98895472e-01  3.21631461e-01
   3.60193163e-01  3.06052357e-01  1.97914705e-01 -3.52567554e-01
  -1.57335043e-01  4.74708349e-01 -2.89923221e-01 -5.26184678e-01
  -2.55940318e-01  9.64594007e-01  1.04901142e-01  5.32600045e-01]
 [ 5.33165216e-01  1.68646455e-01  1.38349116e-01 -3.04048091e-01
  -2.43290633e-01  4.20771390e-01 -4.54783469e-01 -1.21868975e-01
   7.53116667e-01 -1.09975472e-01  3.66390973e-01  2.79889524e-01
   9.20385569e-02 -5.87427735e-01 -1.91999108e-01  1.27320781e-01
   2.30510041e-01 -1.82672571e-02 -2.29204714e-01 -5.49729653e-02
   2.71857917e-01 -4.27529722e-01  5.65150119e-02  1.41017184e-01
   4.06138539e-01 -6.89823404e-02 -4.25114572e-01  3.08607072e-01
  -2.49752939e-01  1.04844235e-01  4.92360108e-02  2.10560307e-01
  -6.33557737e-01 -5.41957438e-01  5.09055912e-01 -3.85017037e-01
   3.40655118e-01  7.58586347e-01 -5.85636079e-01  3.37184787e-01
   2.75410339e-02  4.33774106e-03 -8.92759115e-02 -9.50292170e-01
   3.78908336e-01 -1.06797673e-01 -5.50040752e-02  5.17672002e-01
   2.43517831e-01 -5.74083865e-01  4.18639690e-01  1.56333297e-01
  -2.87736773e-01 -3.29183728e-01 -1.63288400e-01  2.60929316e-01
   6.77470744e-01 -5.05098164e-01 -2.36264512e-01 -4.96175177e-02
  -4.48064268e-01 -3.42234999e-01  1.92568555e-01 -6.46826506e-01
   7.84608573e-02 -7.36528635e-01 -1.42362878e-01  6.06404245e-02
  -2.83968489e-04 -6.28306031e-01  3.40358347e-01  1.65109485e-01
  -2.50760734e-01 -9.25745666e-02 -1.00492962e-01  1.53181493e-01
  -1.16992719e-01  1.46986589e-01 -8.87054503e-01 -9.80685502e-02
  -1.92435995e-01 -5.05265594e-01  3.59364480e-01  4.88259435e-01
   6.72824800e-01  4.83946323e-01  1.19981721e-01 -2.03514770e-01
  -3.60027581e-01  3.12032342e-01 -1.64887816e-01 -5.96461415e-01
  -3.97763997e-01  1.27465868e+00  9.12675112e-02  1.03418088e+00]]

=== Vector Shapes ===
BoW shape: (2, 147)
TF-IDF shape: (2, 147)
Embedding shape: (2, 96)

=== Cosine Similarity (BoW) ===
[[1.         0.13135266]
 [0.13135266 1.        ]]

=== Cosine Similarity (TF-IDF) ===
[[1.         0.07159252]
 [0.07159252 1.        ]]

=== Cosine Similarity (Embeddings) ===
[[1.0000001 0.9250263]
 [0.9250263 0.9999999]]

=== Observations ===
1. Bag-of-Words considers only word frequency.
2. TF-IDF highlights important words across documents.
3. Word embeddings capture semantic meaning and context.
4. Embedding similarity reflects deeper relationships between sports news articles.