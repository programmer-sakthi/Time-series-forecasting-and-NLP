Multi File Programming Question
Problem Overview 



A data science team is building a text preprocessing pipeline for a sports news analysis system. The raw text contains various forms of words and noise (stop words, punctuation) that can affect the performance of text mining algorithms. To prepare the data for tasks like classification and clustering, the team needs to implement a Bag-of-Words (BoW) model that converts text into numerical features. 



The team needs to preprocess the text by removing noise, extracting meaningful tokens, and generating a BoW representation to analyze word frequency patterns across multiple sports news articles. 



Objectives 



As part of this text preprocessing and feature extraction task, the team needs to: 



Load and preview the text file – Import the sports news text file and display the first 300 characters to verify successful data loading and understand the content structure. 
Load spaCy model – Initialize the spaCy English model for text processing. 
Preprocess text – Apply text cleaning by converting to lowercase and removing stop words, punctuation, and whitespace tokens. 
Generate Bag-of-Words matrix – Use scikit-learn's CountVectorizer to create a BoW representation of the cleaned documents. 
Display BoW matrix – Show the BoW matrix as a numerical array where rows represent documents and columns represent words. 
Display word frequencies – List all words and their total frequencies across all documents, sorted in descending order. 
﻿

This analysis will help the team transform unstructured sports news into structured data suitable for machine learning models. 



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

Displays the first 300 characters of the loaded text content 
Preceded by the header: "=== Original Text Sample ===" 
Provides a preview of the raw text before processing 
Followed by a blank line separator
 

Preprocessed Text Sample 

Displays the first 300 characters of the cleaned text 
Preceded by the header: "=== Preprocessed Text Sample ===" 
Shows the effect of lowercase conversion and stop word removal 
Followed by a blank line separator 


Bag-of-Words Matrix 

Displays the BoW matrix as a 2D array 
Preceded by the header: "=== Bag-of-Words Matrix ===" 
Rows represent documents, columns represent vocabulary words 
Followed by a blank line separator 


Word Frequencies 

Displays a section header: "=== Word Frequencies ===" 
Shows all words in the vocabulary with their total frequencies 
Each line format: "word : frequency" 
Words are sorted by frequency in descending order 


Refer to the sample output for exact formatting specifications. 

Code constraints :
File Constraints 

File must be a valid text file with .txt extension 
File must exist in the same directory as the Python script (using sys.path[0]) 
File encoding must be UTF-8 compatible 
If the file is not found, the program prints: "Error: File '{filename}' not found." and exits with status code 1 


Library Requirements 

The program uses spaCy library for text processing 
Requires the en_core_web_sm language model to be installed 
If the spaCy model is not found, the program prints: 
"SpaCy model 'en_core_web_sm' not found." 
"Install using: python -m spacy download en_core_web_sm" 
Then exits with status code 1 
The program uses scikit-learn's CountVectorizer for BoW generation 
Uses spaCy's built-in stop words list for filtering 


Processing Constraints 

The program suppresses warnings using warnings.simplefilter(action='ignore') 
TensorFlow warnings are suppressed via environment variable TF_CPP_MIN_LOG_LEVEL = '3' 
File reading uses UTF-8 encoding explicitly 
Text preprocessing includes: 
Converting to lowercase 
Removing stop words using spaCy's STOP_WORDS 
Removing punctuation tokens 
Removing whitespace tokens 
Each document is processed separately and stored in a list 


Vectorization Constraints 

CountVectorizer is used without any custom parameters (uses default settings) 
Vocabulary is built from all cleaned documents 
Stop words are already removed during preprocessing, so CountVectorizer doesn't apply additional stop word filtering 
BoW matrix is generated as a sparse matrix and converted to array for display
 

Output Constraints 

The original text preview displays exactly the first 300 characters using slicing content[:300] 
The preprocessed text preview displays exactly the first 300 characters 
BoW matrix is displayed using .toarray() method 
Word frequencies are calculated by summing across all documents (axis=0) 
Words are sorted by frequency in descending order using sorted() with key=lambda x: x[1] 
All section headers use === for emphasis 
Blank lines (print()) separate all major output sections 
All print statements must match the exact format shown in the solution, including spacing and formatting 
Sample test cases :
Input 1 :
Sample.txt
Output 1 :
Enter sports news text file name: 
=== Original Text Sample ===
News Article 1


=== Preprocessed Text Sample ===
news article 1

=== Bag-of-Words Matrix ===
[[0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]
 ...
 [0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]
 [1 1 1 ... 0 1 1]]

=== Word Frequencies ===
claxton              : 7
sullivan             : 5
medal                : 4
year                 : 4
european             : 3
hurdles              : 3
ireland              : 3
long                 : 3
old                  : 3
training             : 3
25                   : 2
60                   : 2
april                : 2
article              : 2
british              : 2
championships        : 2
confident            : 2
form                 : 2
london               : 2
major                : 2
march                : 2
month                : 2
new                  : 2
news                 : 2
preparing            : 2
run                  : 2
santry               : 2
saturday             : 2
team                 : 2
time                 : 2
title                : 2
week                 : 2
win                  : 2
won                  : 2
world                : 2
years                : 2
17                   : 1
19                   : 1
20                   : 1
35                   : 1
96                   : 1
aaas                 : 1
agio                 : 1
announced            : 1
athlete              : 1
athletics            : 1
attentions           : 1
australia            : 1
automatic            : 1
base                 : 1
birmingham           : 1
boost                : 1
born                 : 1
britton              : 1
bronze               : 1
bupa                 : 1
byrne                : 1
campaign             : 1
chance               : 1
cobh                 : 1
colchester           : 1
comes                : 1
contested            : 1
country              : 1
course               : 1
cross                : 1
currentily           : 1
dividends            : 1
domestic             : 1
dublin               : 1
equal                : 1
etienne              : 1
event                : 1
explain              : 1
fastest              : 1
favourite            : 1
fifth                : 1
fionnualla           : 1
focused              : 1
france               : 1
grand                : 1
great                : 1
hinted               : 1
hunting              : 1
hurdler              : 1
included             : 1
indicated            : 1
indoor               : 1
indoors              : 1
international        : 1
irina                : 1
jolene               : 1
jump                 : 1
leap                 : 1
left                 : 1
like                 : 1
likely               : 1
line                 : 1
madrid               : 1
marathon             : 1
maria                : 1
mark                 : 1
mccambridge          : 1
moving               : 1
national             : 1
nationals            : 1
official             : 1
officially           : 1
owns                 : 1
participate          : 1
participation        : 1
past                 : 1
pays                 : 1
place                : 1
present              : 1
previous             : 1
prix                 : 1
provincial           : 1
race                 : 1
record               : 1
regime               : 1
runner               : 1
russian              : 1
said                 : 1
sarah                : 1
scotland             : 1
season               : 1
seasons              : 1
seconds              : 1
selected             : 1
selections           : 1
setting              : 1
shevchenko           : 1
sixth                : 1
smashed              : 1
sonia                : 1
spot                 : 1
st                   : 1
stage                : 1
struggled            : 1
success              : 1
teams                : 1
think                : 1
trailing             : 1
translate            : 1
twice                : 1
worlds               : 1