Multi File Programming Question
Problem Statement 



Organizations need to analyze customer feedback to understand sentiment and emotional responses toward their products or services. Traditional sentiment analysis provides only positive/negative classifications, but real-world text data contains complex, nuanced emotions.



This project addresses the need for: 



Comprehensive text preprocessing – Clean and normalize raw text by removing noise, URLs, numbers, punctuation, and extra whitespace to prepare data for feature extraction. 



Feature extraction – Convert cleaned text into numerical representations using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization to capture term importance across the text corpus. 



Multi-dimensional sentiment analysis – Support both single-label sentiment classification and multi-label emotion detection to capture the full emotional spectrum in text data. 



This preprocessing and encoding pipeline ensures that text data is transformed into a format suitable for training sophisticated machine learning models capable of understanding both overall sentiment and specific emotional nuances. 



CSV File Structure





Sample Data

text,sentiment,binary_sentiment,emotion_labels

"Sooo SAD I will miss you here in San Diego!!!",negative,negative,"love,sadness"

"my boss is bullying me...",negative,negative,anger



Required Files 

The solution requires two Python files to be created: 



File 1: nlp_utils.py 

This utility module contains reusable text preprocessing functions: 

Function 1: clean_text(text) 

Purpose: Cleans and normalizes input text for NLP processing 
Operations performed:  
Converts text to lowercase 
Removes URLs (http/https/www links) 
Removes all numeric characters 
Removes all punctuation marks 
Removes extra whitespace and trims the text 
Input: Raw text string 
Output: Cleaned text string 
Handles non-string inputs by returning empty string 


Function 2: split_labels(label_text) 

Purpose: Converts comma-separated emotion labels into a list 
Operations performed:  
Splits string by comma delimiter 
Strips whitespace from each individual label 
Filters out empty strings 
Input: Comma-separated string (e.g., "joy,sadness,anger") 
Output: List of emotion labels (e.g., ['joy', 'sadness', 'anger']) 
Handles non-string inputs by returning empty list 


File 2: main.py (or solution.py) 

This is the main execution file that orchestrates the entire NLP pipeline: 

Import Requirements: 

pandas for data manipulation 
numpy for numerical operations 
sklearn.feature_extraction.text.TfidfVectorizer for feature extraction 
sklearn.preprocessing.LabelEncoder for single-label encoding 
sklearn.preprocessing.MultiLabelBinarizer for multi-label encoding 
nlp_utils module (clean_text, split_labels functions) 
os, sys for file path handling 
warnings for suppressing warning messages 


Main Processing Pipeline: 

File Input & Loading  

Prompts user for filename with extension 
Supports CSV (.csv) and Excel (.xlsx, .xls) formats 
Loads data into pandas DataFrame 
Data Exploration  

Displays first 5 rows of dataset 
Shows total number of samples 
Displays data types of all columns 
Shows missing value counts for each column 
Text Cleaning  

Applies clean_text() function to 'text' column 
Creates new 'clean_text' column with processed text 
Displays comparison of original vs cleaned text 
Feature Extraction (TF-IDF)  

Initializes TfidfVectorizer with max_features=2000 
Fits and transforms cleaned text data 
Outputs shape of TF-IDF matrix 
Sentiment Encoding (if sentiment column exists)  

Uses LabelEncoder to convert categorical sentiment to integers 
Creates 'sentiment_encoded' column 
Displays mapping of sentiment classes to encoded values 
Multi-label Emotion Encoding (if emotion_labels column exists)  

Applies split_labels() to convert strings to lists 
Creates 'emotion_list' column 
Uses MultiLabelBinarizer to create binary matrix 
Displays unique emotion classes and encoding shape 
Input format :
CSV File Input: 

The program prompts the user to enter the name of the dataset file 
Input must include the file extension (.csv, .xlsx, or .xls) 
File must be located in the same directory as the script 
Output format :
The program generates the following outputs in sequence: 



1. First 5 Rows of Data: 

Prints the heading: === First 5 Rows === 
Displays the first 5 rows of the DataFrame using .head() 
Shows in tabular format with column names and row indices 
Displays all columns: text, sentiment, binary_sentiment, emotion_labels 


2. Number of Samples: 

Prints a blank line 
Prints: "Number of samples: X" where X is the total number of rows in the dataset 


3. Data Types: 

Prints a blank line followed by: === Data Types === 
Lists all column names with their corresponding data types using .dtypes 
Shows data types (e.g., object, int64) 
Ends with dtype: object 


4. Missing Values: 

Prints a blank line followed by: === Missing Values === 
Displays count of missing (null) values for each column using .isnull().sum() 
Shows column names with their corresponding null counts 


5. Sample Cleaned Text: 

Prints a blank line followed by: === Sample Cleaned Text === 
Displays comparison of original text and cleaned text for first 5 samples 
Shows two columns: text and clean_text 
Demonstrates the text cleaning transformation applied by clean_text() function 


6. TF-IDF Shape: 

Prints a blank line 
Prints: "TF-IDF Shape: (X, Y)" where X is number of samples and Y is max_features (2000) 
Shows dimensions of the sparse matrix created by TfidfVectorizer 


7. Sentiment Mapping (if sentiment column exists): 

Prints a blank line 
Prints: "Sentiment Classes:" followed by dictionary 
Displays mapping of sentiment classes to encoded integer values 
Shows the LabelEncoder transformation: {'negative': 0, 'positive': 1, ...} 


8. Multi-label Classes (if emotion_labels column exists): 

Prints a blank line 
Prints: "Emotion Classes:" followed by array of classes 
Shows array of unique emotion classes found using MultiLabelBinarizer 
Example: ['anger' 'joy' 'love' 'sadness'] 
Prints: "Emotion Encoding Shape: (X, Y)" where X is number of samples and Y is number of unique emotion classes 


Code constraints :
File and Data Constraints 

CSV Constraints: 

File must be CSV (.csv), Excel (.xlsx), or older Excel (.xls) format 
File must exist in the same directory as the Python script 
File must contain the text column for text processing (mandatory) 
File must contain at least 1 row of data (excluding header) 
If file format is unsupported, program prints "Unsupported file format" and exits 
If file cannot be loaded, program handles the error gracefully 


Column Data Type Constraints: 

text: Must be text/string values containing content to analyze (mandatory) 
sentiment: Text/string values representing sentiment categories (optional) 
binary_sentiment: Text/string or numeric values for binary classification (optional) 
emotion_labels: Text/string values with comma-separated emotion tags (optional) 


Text Processing Constraints 

Text Cleaning (clean_text function in nlp_utils.py): 

Converts all text to lowercase for consistency 
Removes URLs using regex pattern r'http\S+|www\S+' 
Removes all numbers using regex pattern r'\d+' 
Removes all punctuation using string.punctuation translation 
Removes extra whitespace using regex pattern r'\s+' and applies .strip() 
Returns cleaned text string 
Handles non-string inputs by returning empty string "" 
Preserves only lowercase alphabetic characters and single spaces 


Multi-label Processing (split_labels function in nlp_utils.py): 

Handles comma-separated emotion labels 
Splits string by comma delimiter using .split(',') 
Strips whitespace from each label using .strip() 
Filters out empty strings using list comprehension 
Returns empty list [] for non-string values 
Preserves individual emotion tags as list elements for multi-label encoding 


Feature Extraction Constraints 

TF-IDF Vectorization: 

Maximum features: 2000 (max_features=2000) 
Uses TfidfVectorizer from sklearn.feature_extraction.text 
Fitted on all cleaned text data using .fit_transform() 
Converts text to numerical feature vectors 
Output: Sparse matrix representation of text features 
Shape: (number_of_samples, 2000) 
Each feature represents importance of a term in the corpus 


Encoding Constraints 

Single-label Encoding (Sentiment): 

Uses LabelEncoder from sklearn.preprocessing 
Applied only if 'sentiment' column exists in dataset 
Transforms categorical sentiment values to integers (0, 1, 2, ...) 
Creates new column: sentiment_encoded 
Displays class-to-integer mapping dictionary using dict(zip(le.classes_, le.transform(le.classes_))) 
Each unique sentiment category gets a unique integer label 


Multi-label Encoding (Emotion Labels): 

Uses MultiLabelBinarizer from sklearn.preprocessing 
Applied only if 'emotion_labels' column exists in dataset 
First converts comma-separated strings to lists using split_labels() function 
Creates new column: emotion_list with list of individual emotions 
Transforms emotion lists to binary matrix representation using .fit_transform() 
Each column in the matrix represents one unique emotion class 
Value of 1 indicates presence of that emotion, 0 indicates absence 
Enables handling multiple emotions per text sample 
Output shape: (number_of_samples, number_of_unique_emotions) 


Program Processing Constraints 

Error Handling: 

If file format is unsupported, prints: "Unsupported file format" and exits using return 
If text column is not found, prints: "Column 'text' not found" and exits using return 
Uses isinstance() checks in utility functions to validate input types 


General Processing: 

Warnings are suppressed using warnings.simplefilter(action='ignore') 
All processing steps are performed sequentially with clear section headings 
Uses .apply() method to apply functions to DataFrame columns 
Conditional processing based on column existence (sentiment, emotion_labels) 
All outputs include descriptive headers with === formatting for clarity 


Module Structure: 

Main processing logic in main.py/solution.py 
Reusable utility functions in separate nlp_utils.py module 
Clear separation of concerns between data processing and text utilities 
Functions are well-documented with docstrings explaining purpose and behavior 
Sample test cases :
Input 1 :
Sample.csv
Output 1 :
=== First 5 Rows ===
                                                text  ...                  emotion_labels
0      Sooo SAD I will miss you here in San Diego!!!  ...                    love,sadness
1                          my boss is bullying me...  ...                           anger
2                     what interview! leave me alone  ...         anger,confusion,disgust
3   Sons of ****, why couldn`t they put them on t...  ...  anticipation,boredom,confusion
4  2am feedings for the baby are fun when he is a...  ...                  excitement,joy

[5 rows x 4 columns]

Number of samples: 21

=== Data Types ===
text                object
sentiment           object
binary_sentiment    object
emotion_labels      object
dtype: object

=== Missing Values ===
text                0
sentiment           0
binary_sentiment    0
emotion_labels      0
dtype: int64

=== Sample Cleaned Text ===
                                                text                                         clean_text
0      Sooo SAD I will miss you here in San Diego!!!         sooo sad i will miss you here in san diego
1                          my boss is bullying me...                             my boss is bullying me
2                     what interview! leave me alone                      what interview leave me alone
3   Sons of ****, why couldn`t they put them on t...  sons of why couldnt they put them on the relea...
4  2am feedings for the baby are fun when he is a...  am feedings for the baby are fun when he is al...

TF-IDF Shape: (21, 181)

Sentiment Classes: {'negative': 0, 'neutral': 1, 'positive': 2}

Emotion Classes: ['anger' 'anticipation' 'boredom' 'confusion' 'disgust' 'excitement'
 'fear' 'joy' 'love' 'sadness' 'surprise']
Emotion Encoding Shape: (21, 11)