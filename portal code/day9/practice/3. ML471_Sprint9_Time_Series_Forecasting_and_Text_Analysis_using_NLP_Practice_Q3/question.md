Multi File Programming Question
Problem Statement 



Organizations need to analyze customer reviews to understand sentiment and emotional responses toward their products or services. Traditional sentiment analysis provides only positive/negative classifications, but real-world reviews contain complex, nuanced emotions. 



This project addresses the need for: 



Comprehensive text preprocessing – Clean and normalize raw review text by removing noise, URLs, mentions, punctuation, and stopwords to prepare data for feature extraction. 
Feature extraction – Convert cleaned text into numerical representations using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization to capture term importance across the review corpus. 
Multi-dimensional sentiment analysis – Support both binary sentiment classification and multi-label emotion detection to capture the full emotional spectrum in reviews. 


This solution implements an end-to-end NLP pipeline for analyzing customer reviews through three complementary classification approaches: 



1. Text Preprocessing (nlp_utils.py) 

Cleaning Function (clean_text): 

Converts text to lowercase 
Removes URLs, mentions, punctuation, and numbers 
Eliminates English stopwords using a built-in set 
Returns normalized, tokenized text suitable for ML models 
Label Processing (split_labels): 

Converts comma-separated emotion labels into structured lists 
Handles missing or empty values gracefully 
Data Splitting (split_data): 

Randomly splits dataset into training (80%) and testing (20%) sets 
Maintains reproducibility with fixed random state 


2. Feature Engineering (Solution file.txt) 

TF-IDF Vectorization: 

Converts cleaned text into 3000-dimensional numerical features 
Captures term importance relative to the entire corpus 
Creates sparse matrix representations for efficient ML processing 


3. Multi-Level Classification System 

The system performs three parallel classification tasks: 

Binary Sentiment Classification: 

Uses Logistic Regression 
Classifies reviews as positive (1) or negative (0) 
Reports Accuracy, Precision, Recall, and F1 Score 
Multi-Class Sentiment Analysis: 

Uses Multinomial Naive Bayes 
Classifies into multiple sentiment categories (encoded numerically) 
Provides confusion matrix and detailed classification report 
Multi-Label Emotion Detection: 

Uses One-vs-Rest classifier with Logistic Regression 
Detects multiple emotions per review (e.g., "happy,excited,satisfied") 
Reports Micro F1 (emphasizes frequent labels) and Macro F1 (treats all labels equally) 
Provides per-emotion F1 scores for detailed analysis 
 

CSV File Structure



﻿



Sample Data



review,binary_sentiment,emotion_labels,sentiment

"One of the other reviewers has mentioned that after watching just 1 Oz episode you'll be hooked. They are right, as this is exactly what happened with me.<br /><br />The first thing that struck me about Oz was its brutality and unflinching scenes of violence, which set in right from the word GO. Trust me, this is not a show for the faint hearted or timid. This show pulls no punches with regards to drugs, sex or violence. Its is hardcore, in the classic use of the word.<br /><br />It is called OZ as that is the nickname given to the Oswald Maximum Security State Penitentary. It focuses mainly on Emerald City, an experimental section of the prison where all the cells have glass fronts and face inwards, so privacy is not high on the agenda. Em City is home to many..Aryans, Muslims, gangstas, Latinos, Christians, Italians, Irish and more....so scuffles, death stares, dodgy dealings and shady agreements are never far away.<br /><br />I would say the main appeal of the show is due to the fact that it goes where other shows wouldn't dare. Forget pretty pictures painted for mainstream audiences, forget charm, forget romance...OZ doesn't mess around. The first episode I ever saw struck me as so nasty it was surreal, I couldn't say I was ready for it, but as I watched more, I developed a taste for Oz, and got accustomed to the high levels of graphic violence. Not just violence, but injustice (crooked guards who'll be sold out for a nickel, inmates who'll kill on order and get away with it, well mannered, middle class inmates being turned into prison bitches due to their lack of street skills or prison experience) Watching Oz, you may become comfortable with what is uncomfortable viewing....thats if you can get in touch with your darker",1,"anger,fear,disgust","negative"

Input format :
CSV File Input: 

The program prompts the user to enter the name of the dataset file containing review data. 
Input must include the file extension .csv. 
Output format :
The program generates outputs in the following exact sequence: 



1. Data Preview (First 5 Rows) 

Prints: === First 5 Rows === 
Displays the first 5 rows using .head() method 
Shows all 4 columns: review, binary_sentiment, emotion_labels, sentiment 
Provides immediate visibility into raw data structure and content 
Uses tabular format with column names and row indices for readability 


2. Dataset Statistics 

Number of samples: X 
Reports total dataset size (X = total rows) 
Essential for understanding dataset scale and split calculations 


3. Data Type Information 

Prints: === Data Types === 
Lists all column names with corresponding pandas data types 
Shows types like object (text), int64 (numeric), etc. 
Ends with dtype: object as standard pandas output 
Crucial for understanding what preprocessing each column requires 


4. Train/Test Split Details 

Train: X, Test: Y 
Reports training and testing set sizes 
Uses default 80/20 split ratio (configurable) 
Shows actual counts for model training validation 


5. Text Cleaning Demonstration 

Prints: === Sample Cleaned Text === 
Shows side-by-side comparison of original vs cleaned text 
Displays first 5 samples with two columns: review and cleaned_text 
Demonstrates the complete text cleaning transformation: 
Lowercasing 
URL/mention removal 
Punctuation and number removal 
Stopword elimination 
Whitespace normalization 


6. Feature Engineering Statistics 

Prints: === TF-IDF Shapes === 
Train: (X, Y) 
Test: (A, B) 
Reports TF-IDF matrix dimensions for both training and test sets 
X/A = number of samples in each set 
Y/B = 3000 (max_features parameter) 
Shows sparse matrix dimensions for memory/performance awareness 


7. Sentiment Encoding Information (Conditional) 

Prints: === Sentiment Mapping === 
{'negative': 0, 'neutral': 1, 'positive': 2} 
Only displays if sentiment column exists in dataset 
Shows LabelEncoder transformation mapping 
Documents how categorical sentiment labels are converted to numerical values 
Essential for interpreting model predictions 


8. Multi-label Class Information (Conditional) 

Prints: === Multi-label Classes === 
['anger' 'disgust' 'fear' 'joy' 'sadness' 'surprise'] 
Multi-label shape (train): (X, Y) 
Only displays if emotion_labels column exists 
Shows unique emotion classes detected by MultiLabelBinarizer 
Reports training set shape: X = samples, Y = unique emotion classes 
Documents the multi-label encoding structure 


Refer to the sample output for exact formatting specifications. 

 

Code constraints :
CSV Constraints 

File must be a comma-separated CSV (.csv) 
File must exist in the same directory as the Python script 
File must contain the review column for text processing 
File must contain at least 1 row of data (excluding header) 
Supported file formats: CSV 


Column Data Type Constraints 

review: Must be text/string values containing review content 
binary_sentiment: Integer values (0 or 1) for binary classification 
emotion_labels: Text/string values with comma-separated emotion tags 
sentiment: Text/string values representing sentiment categories 


Text Processing Constraints 

Text Cleaning (clean_text function): 

Converts all text to lowercase for consistency 
Removes URLs using regex pattern http\S+ 
Removes mentions (e.g., @username) using regex pattern @\w+ 
Removes all punctuation, numbers, and special characters using pattern [^a-z\s] 
Filters out English stopwords (190+ common words like 'a', 'the', 'is', 'and', etc.) 
Returns space-separated cleaned tokens 


Multi-label Processing (split_labels function): 

Handles comma-separated emotion labels 
Splits string by comma delimiter 
Strips whitespace from each label 
Returns empty list for NaN or empty values 
Preserves individual emotion tags for multi-label encoding 


Train/Test Split (split_data function): 

Default test ratio: 20% (test_ratio=0.2) 
Default random state: 42 for reproducibility 
Uses random sampling with df.sample() 
Returns reset-indexed DataFrames for both train and test sets 


Feature Extraction Constraints 

TF-IDF Vectorization: 

Maximum features: 3000 (max_features=3000) 
Fitted on training data only to prevent data leakage 
Transforms both train and test sets using fitted vectorizer 
Saves vectorizer as tfidf.pkl in script directory for future use 
Output: Sparse matrix representation of text features 


Encoding Constraints 

Single-label Encoding (Sentiment): 

Uses LabelEncoder from sklearn for sentiment column 
Transforms categorical sentiment values to integers 
Fitted on training data, applied to both train and test 
Creates new column: sentiment_encoded 
Displays class-to-integer mapping dictionary 


Multi-label Encoding (Emotion Labels): 

Uses MultiLabelBinarizer from sklearn for emotion_labels column 
First converts comma-separated strings to lists using split_labels 
Creates new column: emotion_list with list of individual emotions 
Transforms emotion lists to binary matrix representation 
Each column represents one unique emotion class 
Value of 1 indicates presence of that emotion, 0 indicates absence 
Fitted on training data, applied to both train and test 


Program Processing Constraints 

If file is not found, prints error message: "Error loading file: {error_details}" and exits 
If review column is not found, prints: "Column 'review' not found — cannot clean text." and exits 
Warnings are suppressed using warnings.simplefilter("ignore") 
TF-IDF vectorizer is saved using pickle for deployment/inference 
All processing steps are performed sequentially with clear section headings 
Sample test cases :
Input 1 :
Sample.csv
Output 1 :

============= BINARY MODEL =============
Accuracy : 0.5
Precision: 0.5
Recall   : 1.0
F1 Score : 0.6666666666666666

============= MULTI-LABEL MODEL =============
Micro F1 : 0.3
Macro F1 : 0.16666666666666666

Per-Label F1 Scores:
anger: 0.0000
anticipation: 0.0000
boredom: 0.0000
confusion: 0.0000
disgust: 0.6667
excitement: 0.6667
fear: 0.0000
joy: 0.6667
love: 0.0000
sadness: 0.0000
surprise: 0.0000
trust: 0.0000

Metric Interpretation:
Accuracy  : Overall correctness
Precision : Correct positive predictions
Recall    : Actual positives captured
F1 Score  : Balance of precision and recall
Micro F1  : Emphasizes frequent labels
Macro F1  : Treats all labels equally