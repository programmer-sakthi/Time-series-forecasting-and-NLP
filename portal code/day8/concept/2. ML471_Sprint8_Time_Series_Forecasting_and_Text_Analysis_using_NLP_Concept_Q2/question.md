Multi File Programming Question
Problem Overview 



A data science team is building a text preprocessing pipeline for a business news analysis system. The raw text contains various forms of words and noise (stop words, punctuation) that can affect the performance of text mining algorithms. To prepare the data for tasks like classification and clustering, the team needs to implement both Bag-of-Words (BoW) and TF-IDF models that convert text into numerical features. 



The team needs to preprocess the text by removing noise, extracting meaningful tokens, and generating both BoW and TF-IDF representations to analyze word frequency patterns and document importance across multiple business news articles. 



Objectives 



As part of this text preprocessing and feature extraction task, the team needs to: 



Load spaCy model – Initialize the spaCy English model (en_core_web_sm) for text processing with error handling. 
Load business news file – Import the business news text file (Sample.txt) containing articles about media companies, financial markets, and airline industry. 
Preprocess documents – Clean all documents by applying lowercase conversion, stop word removal, and punctuation filtering using spaCy. 
Generate TF-IDF matrix – Use scikit-learn's TfidfVectorizer to create a comprehensive TF-IDF representation of all cleaned documents. 
Display TF-IDF breakdown – Show Term Frequency (TF), Inverse Document Frequency (IDF), and TF-IDF scores for each word in each document. 
Provide interpretations – Explain key observations about common vs rare words and document-specific importance. 


This analysis will help the team transform unstructured business news into structured data suitable for machine learning models and document comparison tasks. 



The input file contains unstructured sports news articles separated by delimiters. Each article includes: 



Article title/heading 
Article body with multiple paragraphs 
Separator lines (dashes) between articles 


Sample Data 



News Article 1 

 

Claxton hunting first major medal 

 

British hurdler Sarah Claxton is confident she can win her first major medal at next month's European Indoor Championships in Madrid...



Program Structure 

The solution consists of two files: 



1. nlp_module.py (Utility Module) 

Contains reusable functions for text processing: 

read_from_file(filename) – Reads text file and returns list of documents 
read_from_sentence(sentence) – Preprocesses a single sentence 
preprocess_using_spaCy(documents) – Preprocesses multiple documents 
convert_bow_counter(clean_docs) – Converts documents to BoW using CountVectorizer 
prepare_output_text(vectorizer, bow_matrix) – Displays vocabulary and frequencies 
convert_bow_tfidf(clean_docs) – Converts documents to TF-IDF representation 
print_tfidf_result(features, idf_values, tfidf_matrix) – Displays TF-IDF breakdown 


2. main.py (Main Script) 

Orchestrates the text analysis workflow: 



Suppresses warnings and TensorFlow logs 
Loads spaCy model with error handling 
Reads business news file 
Preprocesses all documents 
Generates TF-IDF representation 
Displays detailed TF-IDF breakdown for each document 
Provides key observations and interpretations 
Input format :
Text File Input: 

The program prompts the user with: "Enter sports news text file name: " 
Input must include the file extension .txt 
File should be located in the same directory as the Python script 
File must be UTF-8 encoded 


Output format :
The program generates the following outputs in sequence: 



TF-IDF Breakdown (Multiple Documents) 

For each document, displays: 

Document Number – Header showing "Document 1:", "Document 2:", etc. 
Word Statistics – For each word with TF-IDF > 0:  
Word (left-aligned, 12 characters wide) 
TF (Term Frequency) – 4 decimal places 
IDF (Inverse Document Frequency) – 4 decimal places 
TF-IDF (Combined score) – 4 decimal places 
Format: word | TF: 0.xxxx | IDF: x.xxxx | TF-IDF: x.xxxx 



Key Observations & Interpretations 

The program concludes with analytical insights: 

Common words across documents have lower IDF values. 
Rare words receive higher TF-IDF scores. 
TF-IDF highlights important document-specific terms. 
It improves document comparison over simple BoW. 


Refer to the sample output for exact formatting specifications. 

Code constraints :
File Constraints 

File must be a valid text file with .txt extension 
File must exist at the path constructed using os.path.join(sys.path[0], filename) 
File encoding must be UTF-8 compatible 
If the file is not found, the program prints: "File not found" and exits with status code 1 
Each non-empty line in the file is treated as a separate document 


Library Requirements 

spaCy: Required for text processing and NLP operations 
en_core_web_sm model: spaCy's English language model must be installed 
If the spaCy model is not found, the program prints:  
"Install spaCy model using:" 
"python -m spacy download en_core_web_sm" 
Then exits with status code 1 
scikit-learn: Required for TfidfVectorizer 
NumPy: Required for array operations 
warnings module: Used to suppress warning messages 
sys module: Used for file path handling and program exit 


Processing Constraints 

The program suppresses all warnings using warnings.simplefilter(action='ignore') 
TensorFlow warnings are suppressed via environment variable TF_CPP_MIN_LOG_LEVEL = '3' (set before imports) 
File reading uses explicit UTF-8 encoding: open(file_path, "r", encoding="utf-8") 
Text preprocessing includes:  
Converting all text to lowercase using .lower() 
Tokenizing using spaCy's nlp pipeline 
Removing stop words using token.is_stop check 
Keeping only alphabetic tokens using token.is_alpha check (removes punctuation and numbers) 
Removing whitespace tokens automatically through is_alpha filter 
Each document/line is processed separately and stored in a list 
List comprehension is used for efficient token filtering 


Vectorization Constraints 

TfidfVectorizer() is instantiated without any custom parameters (uses all defaults) 
Default parameters mean:  
No additional stop word filtering (already done in preprocessing) 
Unigram features only (single words) 
Case sensitivity doesn't matter (text already lowercased) 
Vocabulary is automatically built from all cleaned documents during fit_transform() 
TF-IDF matrix is generated as a sparse matrix for memory efficiency 
IMPORTANT FIX: The solution uses get_feature_names() instead of the deprecated method, ensuring compatibility 
Feature names are extracted using the vectorizer's method 
IDF values are accessed via tfidf_vectorizer.idf_ 
TF is calculated as: TF = TF-IDF / IDF 
Matrix dimension: rows = number of documents, columns = vocabulary size 


Output Constraints 

Header: "TF-IDF Breakdown (Multiple Documents):" followed by blank line 
Each document section starts with "Document N:" where N is the document number (1-indexed) 
For each word in the document (where TF-IDF > 0):  
Word is left-aligned in a 12-character field 
TF, IDF, and TF-IDF values are displayed with 4 decimal places 
Format uses pipe separators: | 
Only words with non-zero TF-IDF scores are displayed 
Observations section provides interpretive analysis of the results 
Blank lines separate major output sections 
No additional formatting like bold, colors, or special characters 


Error Handling 

spaCy model loading: Try-except block catches model loading errors 
File reading: Try-except block catches file not found errors 
Exit codes: Program exits with sys.exit(1) on critical errors 
Error messages are descriptive and user-friendly 
Program provides clear installation instructions for missing dependencies 
Sample test cases :
Input 1 :
Sample.txt
Output 1 :

TF-IDF Breakdown (Multiple Documents):

Document 1:
article      | TF: 0.2710 | IDF: 2.6094 | TF-IDF: 0.7071
news         | TF: 0.2710 | IDF: 2.6094 | TF-IDF: 0.7071

Document 2:
ad           | TF: 0.1552 | IDF: 3.3026 | TF-IDF: 0.5125
boost        | TF: 0.1552 | IDF: 2.8971 | TF-IDF: 0.4496
profit       | TF: 0.1552 | IDF: 2.2040 | TF-IDF: 0.3420
sales        | TF: 0.1552 | IDF: 2.6094 | TF-IDF: 0.4050
time         | TF: 0.1552 | IDF: 2.2040 | TF-IDF: 0.3420
warner       | TF: 0.1552 | IDF: 2.3863 | TF-IDF: 0.3703

Document 3:
december     | TF: 0.1172 | IDF: 2.8971 | TF-IDF: 0.3396
earlier      | TF: 0.1172 | IDF: 2.3863 | TF-IDF: 0.2797
giant        | TF: 0.1172 | IDF: 3.3026 | TF-IDF: 0.3871
jumped       | TF: 0.1172 | IDF: 3.3026 | TF-IDF: 0.3871
media        | TF: 0.1172 | IDF: 3.3026 | TF-IDF: 0.3871
months       | TF: 0.1172 | IDF: 2.2040 | TF-IDF: 0.2583
profits      | TF: 0.1172 | IDF: 1.9163 | TF-IDF: 0.2246
quarterly    | TF: 0.1172 | IDF: 2.8971 | TF-IDF: 0.3396
timewarner   | TF: 0.1172 | IDF: 2.2040 | TF-IDF: 0.2583
year         | TF: 0.1172 | IDF: 2.0498 | TF-IDF: 0.2403

Document 4:
advert       | TF: 0.0608 | IDF: 3.3026 | TF-IDF: 0.2009
aol          | TF: 0.0608 | IDF: 2.6094 | TF-IDF: 0.1587
benefited    | TF: 0.0608 | IDF: 3.3026 | TF-IDF: 0.2009
biggest      | TF: 0.0608 | IDF: 3.3026 | TF-IDF: 0.2009
bros         | TF: 0.0608 | IDF: 3.3026 | TF-IDF: 0.2009
buoyed       | TF: 0.0608 | IDF: 3.3026 | TF-IDF: 0.2009
connections  | TF: 0.0608 | IDF: 3.3026 | TF-IDF: 0.2009
dip          | TF: 0.0608 | IDF: 3.3026 | TF-IDF: 0.2009
firm         | TF: 0.0608 | IDF: 3.3026 | TF-IDF: 0.2009
fourth       | TF: 0.0608 | IDF: 2.6094 | TF-IDF: 0.1587
gains        | TF: 0.0608 | IDF: 2.8971 | TF-IDF: 0.1762
google       | TF: 0.0608 | IDF: 2.8971 | TF-IDF: 0.1762
high         | TF: 0.0608 | IDF: 2.3863 | TF-IDF: 0.1451
higher       | TF: 0.0608 | IDF: 2.6094 | TF-IDF: 0.1587
internet     | TF: 0.0608 | IDF: 2.8971 | TF-IDF: 0.1762
investors    | TF: 0.0608 | IDF: 3.3026 | TF-IDF: 0.2009
offset       | TF: 0.0608 | IDF: 2.8971 | TF-IDF: 0.1762
profit       | TF: 0.0608 | IDF: 2.2040 | TF-IDF: 0.1341
profits      | TF: 0.0608 | IDF: 1.9163 | TF-IDF: 0.1166
quarter      | TF: 0.0608 | IDF: 2.0498 | TF-IDF: 0.1247
rose         | TF: 0.0608 | IDF: 2.3863 | TF-IDF: 0.1451
said         | TF: 0.0608 | IDF: 1.6931 | TF-IDF: 0.1030
sales        | TF: 0.1825 | IDF: 2.6094 | TF-IDF: 0.4762
speed        | TF: 0.0608 | IDF: 2.8971 | TF-IDF: 0.1762
timewarner   | TF: 0.0608 | IDF: 2.2040 | TF-IDF: 0.1341
users        | TF: 0.0608 | IDF: 3.3026 | TF-IDF: 0.2009
warner       | TF: 0.0608 | IDF: 2.3863 | TF-IDF: 0.1451

Document 5:
advertising  | TF: 0.0379 | IDF: 2.8971 | TF-IDF: 0.1097
aol          | TF: 0.1136 | IDF: 2.6094 | TF-IDF: 0.2965
broadband    | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
business     | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
close        | TF: 0.0379 | IDF: 2.8971 | TF-IDF: 0.1097
commission   | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
company      | TF: 0.0379 | IDF: 2.8971 | TF-IDF: 0.1097
concluding   | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
customers    | TF: 0.0757 | IDF: 3.3026 | TF-IDF: 0.2501
engine       | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
exceptional  | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
exchange     | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
existing     | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
following    | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
fortunes     | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
fourth       | TF: 0.0379 | IDF: 2.6094 | TF-IDF: 0.0988
free         | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
friday       | TF: 0.0379 | IDF: 2.6094 | TF-IDF: 0.0988
google       | TF: 0.0379 | IDF: 2.8971 | TF-IDF: 0.1097
high         | TF: 0.0379 | IDF: 2.3863 | TF-IDF: 0.0904
hopes        | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
increase     | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
internet     | TF: 0.1136 | IDF: 2.8971 | TF-IDF: 0.3291
items        | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
lost         | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
lower        | TF: 0.0379 | IDF: 2.8971 | TF-IDF: 0.1097
mixed        | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
offering     | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
online       | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
owns         | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
preceding    | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
probe        | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
profit       | TF: 0.0379 | IDF: 2.2040 | TF-IDF: 0.0835
profits      | TF: 0.0379 | IDF: 1.9163 | TF-IDF: 0.0726
quarter      | TF: 0.0379 | IDF: 2.0498 | TF-IDF: 0.0776
quarters     | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
restate      | TF: 0.0379 | IDF: 2.8971 | TF-IDF: 0.1097
results      | TF: 0.0379 | IDF: 2.2040 | TF-IDF: 0.0835
revenues     | TF: 0.0379 | IDF: 2.3863 | TF-IDF: 0.0904
rose         | TF: 0.0379 | IDF: 2.3863 | TF-IDF: 0.0904
said         | TF: 0.0757 | IDF: 1.6931 | TF-IDF: 0.1282
search       | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
sec          | TF: 0.0379 | IDF: 2.8971 | TF-IDF: 0.1097
securities   | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
service      | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
sign         | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
speed        | TF: 0.0379 | IDF: 2.8971 | TF-IDF: 0.1097
stronger     | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
subscribers  | TF: 0.0757 | IDF: 3.3026 | TF-IDF: 0.2501
time         | TF: 0.0379 | IDF: 2.2040 | TF-IDF: 0.0835
timewarner   | TF: 0.0757 | IDF: 2.2040 | TF-IDF: 0.1669
try          | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
underlying   | TF: 0.0379 | IDF: 3.3026 | TF-IDF: 0.1251
warner       | TF: 0.0379 | IDF: 2.3863 | TF-IDF: 0.0904

Document 6:
alexander    | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
analysts     | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
better       | TF: 0.0390 | IDF: 2.6094 | TF-IDF: 0.1018
boosted      | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
box          | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
catwoman     | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
chairman     | TF: 0.0390 | IDF: 2.6094 | TF-IDF: 0.1018
chief        | TF: 0.0390 | IDF: 2.8971 | TF-IDF: 0.1130
contrast     | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
division     | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
earlier      | TF: 0.0390 | IDF: 2.3863 | TF-IDF: 0.0931
earnings     | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
enhancing    | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
exceeding    | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
executive    | TF: 0.0390 | IDF: 2.8971 | TF-IDF: 0.1130
expectations | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
expects      | TF: 0.0390 | IDF: 2.8971 | TF-IDF: 0.1130
film         | TF: 0.0780 | IDF: 3.3026 | TF-IDF: 0.2576
final        | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
financial    | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
flexibility  | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
flops        | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
fourth       | TF: 0.0390 | IDF: 2.6094 | TF-IDF: 0.1018
greatly      | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
grew         | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
growth       | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
helped       | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
higher       | TF: 0.0390 | IDF: 2.6094 | TF-IDF: 0.1018
lord         | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
margins      | TF: 0.0390 | IDF: 2.8971 | TF-IDF: 0.1130
meeting      | TF: 0.0390 | IDF: 2.6094 | TF-IDF: 0.1018
objectives   | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
office       | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
operating    | TF: 0.0390 | IDF: 2.8971 | TF-IDF: 0.1130
parsons      | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
performance  | TF: 0.0780 | IDF: 3.3026 | TF-IDF: 0.2576
posted       | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
profit       | TF: 0.0780 | IDF: 2.2040 | TF-IDF: 0.1719
profits      | TF: 0.0780 | IDF: 1.9163 | TF-IDF: 0.1495
projecting   | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
quarter      | TF: 0.0390 | IDF: 2.0498 | TF-IDF: 0.0799
results      | TF: 0.0390 | IDF: 2.2040 | TF-IDF: 0.0860
revenue      | TF: 0.0390 | IDF: 2.3863 | TF-IDF: 0.0931
revenues     | TF: 0.0390 | IDF: 2.3863 | TF-IDF: 0.0931
richard      | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
rings        | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
said         | TF: 0.0390 | IDF: 1.6931 | TF-IDF: 0.0660
saw          | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
sharp        | TF: 0.0390 | IDF: 2.8971 | TF-IDF: 0.1130
slightly     | TF: 0.0390 | IDF: 2.8971 | TF-IDF: 0.1130
slump        | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
strong       | TF: 0.0390 | IDF: 2.8971 | TF-IDF: 0.1130
time         | TF: 0.0390 | IDF: 2.2040 | TF-IDF: 0.0860
timewarner   | TF: 0.0780 | IDF: 2.2040 | TF-IDF: 0.1719
trilogy      | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
warner       | TF: 0.0390 | IDF: 2.3863 | TF-IDF: 0.0931
wider        | TF: 0.0390 | IDF: 3.3026 | TF-IDF: 0.1288
year         | TF: 0.1170 | IDF: 2.0498 | TF-IDF: 0.2398

Document 7:
accounts     | TF: 0.0767 | IDF: 3.3026 | TF-IDF: 0.2533
adjust       | TF: 0.0383 | IDF: 3.3026 | TF-IDF: 0.1266
advertising  | TF: 0.0383 | IDF: 2.8971 | TF-IDF: 0.1111
aol          | TF: 0.1150 | IDF: 2.6094 | TF-IDF: 0.3002
aside        | TF: 0.0383 | IDF: 3.3026 | TF-IDF: 0.1266
bertelsmann  | TF: 0.0383 | IDF: 3.3026 | TF-IDF: 0.1266
book         | TF: 0.0383 | IDF: 3.3026 | TF-IDF: 0.1266
charges      | TF: 0.0383 | IDF: 3.3026 | TF-IDF: 0.1266
company      | TF: 0.0383 | IDF: 2.8971 | TF-IDF: 0.1111
deal         | TF: 0.0767 | IDF: 3.3026 | TF-IDF: 0.2533
efforts      | TF: 0.0383 | IDF: 3.3026 | TF-IDF: 0.1266
estimate     | TF: 0.0383 | IDF: 3.3026 | TF-IDF: 0.1266
europe       | TF: 0.0767 | IDF: 3.3026 | TF-IDF: 0.2533
german       | TF: 0.0383 | IDF: 3.3026 | TF-IDF: 0.1266
inquiry      | TF: 0.0383 | IDF: 3.3026 | TF-IDF: 0.1266
intends      | TF: 0.0383 | IDF: 3.3026 | TF-IDF: 0.1266
legal   