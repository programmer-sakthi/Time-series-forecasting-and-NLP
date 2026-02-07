Multi File Programming Question
Problem Overview 



A data science team is building a text preprocessing and feature extraction pipeline for a sports news analysis system. The raw text contains various forms of words and noise (stop words, punctuation, capitalization) that can affect the performance of text mining algorithms. To prepare the data for tasks like classification and clustering, the team needs to implement a TF-IDF (Term Frequency-Inverse Document Frequency) model to convert text into meaningful numerical features. 



The team needs to preprocess the text by removing noise, extracting meaningful tokens, and generating a TF-IDF representation to analyze word importance across multiple sports news articles. 



Objectives 



As part of this text preprocessing and feature extraction task, the team needs to: 



Load and preview the text file – Import the sports news text file and display the first 300 characters to verify successful data loading and understand the content structure. 
Load spaCy model – Initialize the spaCy English model for text processing. 
Preprocess text – Apply text cleaning by converting to lowercase and removing stop words, punctuation, and whitespace tokens. 
Generate TF-IDF matrix – Use scikit-learn's TfidfVectorizer to create a TF-IDF representation of the cleaned documents. 
Display TF-IDF features and values – Show the vocabulary (feature names) and IDF values for each term. 
Display TF-IDF matrix – Show the TF-IDF matrix as a numerical array where rows represent documents and columns represent words. 


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
Preceded by the header: === Original Text Sample (First 300 chars) === 
Followed by a blank line 


Cleaned Text Sample 

Displays the first 50 cleaned tokens 
Preceded by the header: === Cleaned Text Sample === 
Followed by a blank line 


TF-IDF Features 

Displays all vocabulary words 
Preceded by the header: === TF-IDF Features === 
Followed by a blank line 


IDF Values 

Displays each word and its IDF value 
Preceded by the header: === IDF Values === 
Each line format: word : idf_value 
Followed by a blank line 


TF-IDF Matrix 

Displays the TF-IDF matrix as a DataFrame rounded to 4 decimal places 
Preceded by the header: === TF-IDF Matrix === 


Refer to the sample output for exact formatting specifications. 

Code constraints :
File Constraints 

File must be a valid text file with .txt extension 
File must exist in the same directory as the Python script (using sys.path[0]) 
File encoding must be UTF-8 compatible 
If the file is not found, the program prints: 
Error: File '{filename}' not found. and exits with status code 1 


Library Requirements 

The program uses spaCy library for text processing 
Requires the en_core_web_sm language model to be installed 
If the spaCy model is not found, the program prints installation instructions and exits 
The program uses scikit-learn's TfidfVectorizer for TF-IDF generation 
Uses spaCy's built-in stop words list for filtering


Processing Constraints 

The program suppresses warnings using warnings.simplefilter(action='ignore') 
TensorFlow warnings are suppressed via environment variable TF_CPP_MIN_LOG_LEVEL = '3' 
Text preprocessing includes: 
Converting to lowercase 
Removing stop words using spaCy's is_stop 
Removing punctuation tokens 
Removing whitespace tokens 
Documents are stored in a list for vectorization 


Vectorization Constraints 

TfidfVectorizer is used without any custom parameters (uses default settings) 
Vocabulary is built from all cleaned documents 
IDF values are extracted using vectorizer.idf_ 
Feature names are extracted using vectorizer.get_feature_names() 


Output Constraints 

The original text preview displays exactly the first 300 characters using slicing content[:300] 
The cleaned text preview displays exactly the first 50 cleaned tokens 
TF-IDF matrix is displayed using pd.DataFrame rounded to 4 decimal places 
All section headers use === for emphasis 
Blank lines separate all major output sections 
All print statements match the exact format shown in the solution code 
Sample test cases :
Input 1 :
Sample.txt
Output 1 :
Enter text file name: 
=== Original Text Sample (First 300 chars) ===
News Article 1

Claxton hunting first major medal

British hurdler Sarah Claxton is confident she can win her first major medal at next month's European Indoor Championships in Madrid.

The 25-year-old has already smashed the British record over 60m hurdles twice this season, setting a new mark of 7

=== Cleaned Text Sample ===
news article claxton hunting major medal british hurdler sarah claxton confident win major medal month european indoor championships madrid year old smashed british record m hurdles twice season setting new mark seconds win aaas title confident said claxton race comes long training think chance medal claxton won national m hurdles

=== TF-IDF Features ===
['aaas', 'agio', 'announced', 'april', 'article', 'athlete', 'athletics', 'attentions', 'australia', 'automatic', 'base', 'birmingham', 'boost', 'born', 'british', 'britton', 'bronze', 'bupa', 'byrne', 'campaign', 'championships', 'chance', 'claxton', 'cobh', 'colchester', 'comes', 'confident', 'contested', 'country', 'course', 'cross', 'currentily', 'dividends', 'domestic', 'dublin', 'equal', 'etienne', 'european', 'event', 'explain', 'fastest', 'favourite', 'fifth', 'fionnualla', 'focused', 'form', 'france', 'grand', 'great', 'hinted', 'hunting', 'hurdler', 'hurdles', 'included', 'indicated', 'indoor', 'indoors', 'international', 'ireland', 'irina', 'jolene', 'jump', 'leap', 'left', 'like', 'likely', 'line', 'london', 'long', 'madrid', 'major', 'marathon', 'march', 'maria', 'mark', 'mccambridge', 'medal', 'month', 'moving', 'national', 'nationals', 'new', 'news', 'official', 'officially', 'old', 'owns', 'participate', 'participation', 'past', 'pays', 'place', 'preparing', 'present', 'previous', 'prix', 'provincial', 'race', 'record', 'regime', 'run', 'runner', 'russian', 'said', 'santry', 'sarah', 'saturday', 'scotland', 'season', 'seasons', 'seconds', 'selected', 'selections', 'setting', 'shevchenko', 'sixth', 'smashed', 'sonia', 'spot', 'st', 'stage', 'struggled', 'success', 'team', 'teams', 'think', 'time', 'title', 'trailing', 'training', 'translate', 'twice', 'week', 'win', 'won', 'world', 'worlds', 'year', 'years']

=== IDF Values ===
aaas                 : 1.0000
agio                 : 1.0000
announced            : 1.0000
april                : 1.0000
article              : 1.0000
athlete              : 1.0000
athletics            : 1.0000
attentions           : 1.0000
australia            : 1.0000
automatic            : 1.0000
base                 : 1.0000
birmingham           : 1.0000
boost                : 1.0000
born                 : 1.0000
british              : 1.0000
britton              : 1.0000
bronze               : 1.0000
bupa                 : 1.0000
byrne                : 1.0000
campaign             : 1.0000
championships        : 1.0000
chance               : 1.0000
claxton              : 1.0000
cobh                 : 1.0000
colchester           : 1.0000
comes                : 1.0000
confident            : 1.0000
contested            : 1.0000
country              : 1.0000
course               : 1.0000
cross                : 1.0000
currentily           : 1.0000
dividends            : 1.0000
domestic             : 1.0000
dublin               : 1.0000
equal                : 1.0000
etienne              : 1.0000
european             : 1.0000
event                : 1.0000
explain              : 1.0000
fastest              : 1.0000
favourite            : 1.0000
fifth                : 1.0000
fionnualla           : 1.0000
focused              : 1.0000
form                 : 1.0000
france               : 1.0000
grand                : 1.0000
great                : 1.0000
hinted               : 1.0000
hunting              : 1.0000
hurdler              : 1.0000
hurdles              : 1.0000
included             : 1.0000
indicated            : 1.0000
indoor               : 1.0000
indoors              : 1.0000
international        : 1.0000
ireland              : 1.0000
irina                : 1.0000
jolene               : 1.0000
jump                 : 1.0000
leap                 : 1.0000
left                 : 1.0000
like                 : 1.0000
likely               : 1.0000
line                 : 1.0000
london               : 1.0000
long                 : 1.0000
madrid               : 1.0000
major                : 1.0000
marathon             : 1.0000
march                : 1.0000
maria                : 1.0000
mark                 : 1.0000
mccambridge          : 1.0000
medal                : 1.0000
month                : 1.0000
moving               : 1.0000
national             : 1.0000
nationals            : 1.0000
new                  : 1.0000
news                 : 1.0000
official             : 1.0000
officially           : 1.0000
old                  : 1.0000
owns                 : 1.0000
participate          : 1.0000
participation        : 1.0000
past                 : 1.0000
pays                 : 1.0000
place                : 1.0000
preparing            : 1.0000
present              : 1.0000
previous             : 1.0000
prix                 : 1.0000
provincial           : 1.0000
race                 : 1.0000
record               : 1.0000
regime               : 1.0000
run                  : 1.0000
runner               : 1.0000
russian              : 1.0000
said                 : 1.0000
santry               : 1.0000
sarah                : 1.0000
saturday             : 1.0000
scotland             : 1.0000
season               : 1.0000
seasons              : 1.0000
seconds              : 1.0000
selected             : 1.0000
selections           : 1.0000
setting              : 1.0000
shevchenko           : 1.0000
sixth                : 1.0000
smashed              : 1.0000
sonia                : 1.0000
spot                 : 1.0000
st                   : 1.0000
stage                : 1.0000
struggled            : 1.0000
success              : 1.0000
team                 : 1.0000
teams                : 1.0000
think                : 1.0000
time                 : 1.0000
title                : 1.0000
trailing             : 1.0000
training             : 1.0000
translate            : 1.0000
twice                : 1.0000
week                 : 1.0000
win                  : 1.0000
won                  : 1.0000
world                : 1.0000
worlds               : 1.0000
year                 : 1.0000
years                : 1.0000

=== TF-IDF Matrix ===
     aaas    agio  announced   april  ...   world  worlds    year   years
0  0.0545  0.0545     0.0545  0.1089  ...  0.1089  0.0545  0.2179  0.1089

[1 rows x 139 columns]