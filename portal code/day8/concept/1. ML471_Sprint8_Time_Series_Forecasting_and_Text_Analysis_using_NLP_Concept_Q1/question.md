Multi File Programming Question
Problem Overview 



A data science team is building a text preprocessing pipeline for a business news analysis system. The raw text contains various forms of words and noise (stop words, punctuation) that can affect the performance of text mining algorithms. To prepare the data for tasks like classification and clustering, the team needs to implement a Bag-of-Words (BoW) model that converts text into numerical features. 



The team needs to preprocess the text by removing noise, extracting meaningful tokens, and generating a BoW representation to analyze word frequency patterns across multiple business news articles. 



Objectives 



As part of this text preprocessing and feature extraction task, the team needs to: 



Process a sample sentence – Demonstrate text cleaning on a simple sentence ("LOL LOL slay slay slay queen.") to show the preprocessing pipeline in action. 
Load spaCy model – Initialize the spaCy English model (en_core_web_sm) for text processing with error handling. 
Preprocess sentence – Apply text cleaning by converting to lowercase and removing stop words, punctuation, and whitespace tokens from the sample sentence. 
Generate sentence BoW – Create a Bag-of-Words representation using CountVectorizer showing word frequencies for the cleaned sentence. 
Load business news file – Import the business news text file (Sample.txt) containing articles about media companies, financial markets, and airline industry. 
Preprocess documents – Clean all documents by applying lowercase conversion, stop word removal, and punctuation filtering using spaCy. 
Generate document BoW matrix – Use scikit-learn's CountVectorizer to create a comprehensive BoW representation of all cleaned documents. 
Display word frequencies – List all words and their total frequencies across all business news documents. 


This analysis will help the team transform unstructured business news into structured data suitable for machine learning models. 



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
Task 8.1.2: Processes sample sentence and generates BoW 
Task 8.1.3: Processes business news file and generates BoW 
Input format :
Text File Input: 

The program prompts the user with: "Enter sports news text file name: " 
Input must include the file extension .txt 
File should be located in the same directory as the Python script 
File must be UTF-8 encoded 


Output format :
The program generates the following outputs in sequence: 



Task 8.1.2 – Sentence BoW Output 



1. Cleaned Sentence 

Header: "Cleaned Sentence:" 
Displays the preprocessed sentence with tokens separated by spaces 
Shows only alphabetic tokens with stop words removed 
Example: "lol lol slay slay slay queen" 
Followed by a blank line 


2. BoW Word Frequencies (Sentence) 

Header: "BoW Word Frequencies (Sentence):" 
Shows each unique word with its frequency count 
Format: "word : count" 
Example: 
lol : 2
slay : 3
queen : 1


Task 8.1.3 – Business News File BoW Output 



3. BoW Word Frequencies (Business Data) 

Header: "BoW Word Frequencies (Business Data):" 
Shows all words from the business news file with their total frequencies across all documents 
Each line format: "word : frequency" 
Words appear in vocabulary order (alphabetically as stored in CountVectorizer) 
Frequencies are summed across all documents in the file 
Example: 
profit : 15
sales : 8
quarter : 6




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
scikit-learn: Required for CountVectorizer 
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

CountVectorizer() is instantiated without any custom parameters (uses all defaults) 
Default parameters mean:  
No additional stop word filtering (already done in preprocessing) 
Unigram features only (single words) 
Case sensitivity doesn't matter (text already lowercased) 
Vocabulary is automatically built from all cleaned documents during fit_transform() 
BoW matrix is generated as a sparse matrix for memory efficiency 
Word frequencies are calculated by summing across all documents using bow.sum(axis=0) 
Matrix dimension: rows = number of documents, columns = vocabulary size 


Output Constraints 

Cleaned Sentence: Displays space-joined tokens after preprocessing 
Sentence BoW: Each word shows its count from the BoW matrix using bow[0, index] 
Business Data BoW: Total counts across all documents are converted to integers using int() 
Words are displayed in the order they appear in vectorizer.vocabulary_.items() 
All section headers use descriptive text without special formatting characters 
Blank lines (print() with no arguments) separate major output sections 
No additional formatting like bold, colors, or special characters 
Frequency values are displayed as integers, not floats 


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
Cleaned Sentence:
lol lol slay slay slay queen

BoW Word Frequencies (Sentence):
lol : 2
slay : 3
queen : 1

BoW Word Frequencies (Business Data):
news : 3
article : 3
ad : 1
sales : 5
boost : 2
time : 5
warner : 4
profit : 6
quarterly : 2
profits : 8
media : 1
giant : 1
timewarner : 7
jumped : 1
months : 6
december : 2
year : 11
earlier : 4
firm : 1
biggest : 1
investors : 1
google : 2
benefited : 1
high : 4
speed : 2
internet : 4
connections : 1
higher : 3
advert : 1
said : 12
fourth : 3
quarter : 6
rose : 4
buoyed : 1
gains : 2
offset : 2
dip : 1
bros : 1
users : 1
aol : 7
friday : 3
owns : 1
search : 1
engine : 1
business : 1
mixed : 1
fortunes : 1
lost : 1
subscribers : 2
lower : 2
preceding : 1
quarters : 1
company : 2
underlying : 1
exceptional : 1
items : 1
stronger : 1
advertising : 2
revenues : 5
hopes : 1
increase : 1
offering : 1
online : 1
service : 1
free : 1
customers : 2
try : 1
sign : 1
existing : 1
broadband : 1
restate : 2
results : 6
following : 1
probe : 1
securities : 1
exchange : 1
commission : 1
sec : 2
close : 2
concluding : 1
slightly : 2
better : 4
analysts : 1
expectations : 1
film : 2
division : 1
saw : 1
slump : 1
helped : 1
box : 1
office : 1
flops : 1
alexander : 1
catwoman : 1
sharp : 2
contrast : 1
final : 1
lord : 1
rings : 1
trilogy : 1
boosted : 1
posted : 1
performance : 2
grew : 1
financial : 1
strong : 2
meeting : 3
exceeding : 1
objectives : 1
greatly : 1
enhancing : 1
flexibility : 1
chairman : 4
chief : 2
executive : 2
richard : 1
parsons : 1
projecting : 1
operating : 2
earnings : 1
growth : 1
expects : 2
revenue : 6
wider : 1
margins : 2
accounts : 2
efforts : 1
resolve : 1
inquiry : 1
market : 3
regulators : 1
offered : 1
pay : 1
settle : 1
charges : 1
deal : 2
review : 1
unable : 1
estimate : 1
needed : 1
set : 4
aside : 1
legal : 1
reserves : 1
previously : 3
intends : 1
adjust : 1
way : 3
german : 1
music : 1
publisher : 1
bertelsmann : 1
purchase : 1
stake : 3
europe : 2
reported : 2
book : 1
sale : 1
loss : 1
value : 1
dollar : 6
greenspan : 3
speech : 2
hit : 3
highest : 1
level : 1
euro : 2
federal : 3
reserve : 3
head : 2
trade : 1
deficit : 6
stabilise : 1
alan : 1
highlighted : 1
government : 1
willingness : 1
curb : 1
spending : 1
rising : 1
household : 1
savings : 1
factors : 1
help : 3
reduce : 1
late : 1
trading : 1
new : 2
york : 2
reached : 1
thursday : 1
concerns : 2
greenback : 1
recent : 4
mr : 2
london : 1
ahead : 2
finance : 1
ministers : 1
sent : 1
tumbled : 1
worse : 1
expected : 2
jobs : 2
data : 1
think : 1
taking : 2
sanguine : 1
view : 2
current : 3
account : 3
taken : 2
robert : 1
sinche : 1
currency : 3
strategy : 1
bank : 1
america : 1
longer : 1
term : 1
laying : 1
conditions : 1
improve : 1
worries : 1
china : 2
remain : 2
remains : 2
pegged : 1
falls : 2
chinese : 3
export : 1
prices : 4
highly : 1
competitive : 1
calls : 1
shift : 1
beijing : 1
policy : 2
fallen : 1
deaf : 1
ears : 1
despite : 1
comments : 1
major : 2
newspaper : 1
ripe : 1
loosening : 1
peg : 1
thought : 1
unlikely : 1
produce : 1
meaningful : 1
movement : 1
meantime : 1
decision : 1
february : 1
interest : 1
rates : 2
point : 2
sixth : 1
opened : 1
differential : 1
european : 1
half : 2
window : 1
believe : 2
assets : 2
looking : 2
attractive : 1
prop : 1
partly : 1
result : 1
big : 1
budget : 2
deficits : 1
yawning : 1
gap : 1
need : 1
funded : 1
buying : 1
bonds : 1
foreign : 1
firms : 1
governments : 1
white : 1
house : 1
announce : 1
monday : 1
commentators : 1
trillion : 1
dollars : 1
fuel : 8
ba : 11
british : 1
airways : 1
blamed : 1
drop : 1
reporting : 1
airline : 1
pre : 1
tax : 1
compared : 1
rod : 1
eddington : 2
respectable : 1
costs : 3
expectation : 1
rise : 3
increased : 2
price : 1
aviation : 3
introduced : 1
surcharge : 3
passengers : 1
october : 1
long : 1
haul : 2
flights : 1
short : 2
raised : 1
leg : 1
analyst : 2
mike : 1
powell : 1
dresdner : 1
kleinwort : 1
wasserstein : 1
says : 1
estimated : 1
annual : 1
additional : 1
predicted : 1
extra : 1
turnover : 1
benefiting : 1
cargo : 2
march : 2
warned : 1
yields : 1
average : 1
passenger : 2
decline : 1
continues : 1
face : 1
competition : 1
low : 1
cost : 3
carriers : 1
forecast : 2
total : 1
outlook : 1
previous : 1
guidance : 1
improvement : 1
anticipated : 1
martin : 1
broughton : 1
numbers : 1
january : 1
nick : 1
van : 1
den : 1
brul : 1
bnp : 1
paribas : 1
described : 1
latest : 1
pretty : 1
modest : 1
good : 1
shows : 1
impact : 2
surcharges : 1
positive : 1
development : 1
september : 1
attacks : 1
united : 1
states : 1
cut : 1
cutting : 1
drive : 1
focus : 1
reducing : 1
controllable : 1
debt : 1
whilst : 1
continuing : 1
invest : 1
products : 1
example : 1
delivery : 1
airbus : 1
aircraft : 1
month : 1
start : 1
improvements : 1
club : 1
world : 1
flat : 1
beds : 1
shares : 1
closed : 1
pence : 2