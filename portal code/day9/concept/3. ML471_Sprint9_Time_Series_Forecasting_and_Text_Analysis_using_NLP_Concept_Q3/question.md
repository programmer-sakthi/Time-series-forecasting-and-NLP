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
Removes URLs (http/https patterns) using regex pattern r'http\S+|@\w+' 
Removes all non-alphabetic characters (numbers, punctuation) using regex pattern r'[^a-z\s]' 
Removes English stopwords (common words like 'a', 'the', 'is', 'was', etc.) 
Removes extra whitespace and trims the text 
Input: Raw text string 
Output: Cleaned text string 
Handles: Converts non-string inputs to string using str() 


Function 2: split_labels(label_string) 

Purpose: Converts comma-separated emotion labels into a list 
Operations performed:  
Checks for NaN or empty string values 
Splits string by comma delimiter using .split(',') 
Strips whitespace from each individual label using .strip() 
Returns list of clean emotion labels 
Input: Comma-separated string (e.g., "joy,sadness,anger") 
Output: List of emotion labels (e.g., ['joy', 'sadness', 'anger']) 
Handles: Returns empty list [] for NaN or empty string inputs 


Function 3: split_data(df, test_ratio=0.2, random_state=42) 

Purpose: Splits dataset into training and testing sets 
Operations performed:  
Uses pandas .sample() method with specified test ratio 
Maintains random state for reproducibility 
Resets indices for both train and test sets 
Input: DataFrame, test_ratio (default 0.2), random_state (default 42) 
Output: Two DataFrames (train, test) with reset indices 


File 2: main.py (or solution.py) 

This is the main execution file that orchestrates the entire NLP pipeline: 



Import Requirements: 

pandas for data manipulation 
os, sys for file path handling 
warnings for suppressing warning messages 
sklearn.pipeline.Pipeline for creating ML pipelines 
sklearn.feature_extraction.text.TfidfVectorizer for feature extraction 
sklearn.preprocessing.LabelEncoder for single-label encoding 
sklearn.preprocessing.MultiLabelBinarizer for multi-label encoding 
sklearn.linear_model.LogisticRegression for binary and multi-label classification 
sklearn.naive_bayes.MultinomialNB for multi-class classification 
sklearn.multiclass.OneVsRestClassifier for multi-label classification strategy 
sklearn.metrics for evaluation (accuracy_score, classification_report, confusion_matrix, f1_score) 
nlp_utils module (clean_text, split_labels, split_data functions) 


Main Processing Pipeline: 



File Input & Loading  

Prompts user for filename with extension: "Enter dataset filename (CSV or Excel): " 
Supports CSV (.csv) and Excel (.xlsx, .xls) formats 
Uses os.path.join(sys.path[0], filename) to construct file path 
Loads CSV using pd.read_csv(file_path) 
Loads Excel using pd.read_excel(file_path, engine="openpyxl") 
Prints error "Only CSV or Excel files supported" and exits if unsupported format 
Data Exploration  

Displays heading: === Dataset Preview === 
Shows first 5 rows of dataset using df.head() 
Displays all columns: text, sentiment, binary_sentiment, emotion_labels 
Data Splitting  

Splits dataset using split_data(df) function 
Creates train (80%) and test (20%) sets 
Uses random_state=42 for reproducibility 
Text Cleaning  

Applies clean_text() function to 'text' column for both train and test sets 
Creates new 'clean_text' column with processed text: train["clean_text"] = train["text"].apply(clean_text) 
Example transformation:  
Original: "Sooo SAD I will miss you here in San Diego!!!" 
Cleaned: "sooo sad miss san diego" 
Binary Classification Pipeline  

Section heading: ===== Binary Classification ===== 

Pipeline components:  

TfidfVectorizer with max_features=2000 
LogisticRegression with max_iter=1000 
Training: Fits on train["clean_text"] and train["binary_sentiment"] 

Prediction: Generates predictions on test["clean_text"] 

Output:  

Prints first 10 predictions: "Binary Predictions:" followed by array 
Prints blank line 
Prints "Binary Accuracy:" with accuracy score 
Prints blank line and "Binary Classification Report:\n" with classification report 
Prints "Binary Confusion Matrix:\n" with confusion matrix 
Multi-Class Classification Pipeline  

Section heading: ===== Multi-Class Classification ===== 

Encoding: Uses LabelEncoder to convert sentiment labels to integers  

Creates sentiment_encoded column in both train and test sets 
train["sentiment_encoded"] = le.fit_transform(train["sentiment"]) 
test["sentiment_encoded"] = le.transform(test["sentiment"]) 
Pipeline components:  

TfidfVectorizer with max_features=2000 
MultinomialNB classifier 
Training: Fits on train["clean_text"] and train["sentiment_encoded"] 

Prediction: Generates encoded predictions on test set 

Output:  

Prints first 10 encoded predictions: "Multi-Class Predictions:" followed by array 
Prints blank line 
Prints "Multi-Class Accuracy:" with accuracy score 
Prints blank line and "Multi-Class Classification Report:\n" with classification report 
Prints "Multi-Class Confusion Matrix:\n" with confusion matrix 
Multi-Label Classification Pipeline  

Section heading: ===== Multi-Label Classification ===== 

Preprocessing:  

Applies split_labels() to convert comma-separated strings to lists 
Creates 'emotion_list' column: train["emotion_list"] = train["emotion_labels"].apply(split_labels) 
Encoding: Uses MultiLabelBinarizer to create binary matrix  

Y_train = mlb.fit_transform(train["emotion_list"]) 
Y_test_mlabel = mlb.transform(test["emotion_list"]) 
Each column represents one unique emotion class 
Value of 1 indicates presence, 0 indicates absence 
Pipeline components:  

TfidfVectorizer with max_features=2000 
OneVsRestClassifier wrapping LogisticRegression with max_iter=1000 
Training: Fits on train["clean_text"] and binarized emotion matrix Y_train 

Prediction: Generates binary predictions for each emotion class 

Output:  

Prints "Multi-Label Predictions (first 5 rows):\n" followed by first 5 rows of prediction matrix 
Prints "Classes:" followed by mlb.classes_ array showing unique emotion labels 
Prints blank line 
Prints "Multi-Label Micro F1 Score:" with micro-averaged F1 score 
Prints "Multi-Label Macro F1 Score:" with macro-averaged F1 score 
Prints blank line and "Per-Label F1 Scores:" 
For each emotion class, prints: "{emotion}: {score:.4f}" 


Cross-Model Summary  

Section heading: ========== SUMMARY ========== 

Prints final comparison of all three classification approaches:  
"Binary Accuracy:" with score 
"Multi-Class Accuracy:" with score 
"Multi-Label Micro F1:" with score 
"Multi-Label Macro F1:" with score 
Input format :
CSV File Input: 

The program prompts the user to enter the name of the dataset file 
Input must include the file extension (.csv, .xlsx, or .xls) 
File must be located in the same directory as the script 
Output format :
The program generates the following outputs in sequence: 



1. Dataset Preview 

Prints the heading: === Dataset Preview === 
Displays the first 5 rows of the DataFrame using .head() 
Shows in tabular format with column names and row indices 
Displays all columns: text, sentiment, binary_sentiment, emotion_labels
 

2. Binary Classification Results 

Prints blank line followed by: ===== Binary Classification ===== 
Prints "Binary Predictions:" followed by first 10 predictions as array 
Prints blank line 
Prints "Binary Accuracy:" followed by accuracy score 
Prints blank line 
Prints "Binary Classification Report:\n" followed by detailed metrics (precision, recall, f1-score, support) for each class 
Prints "Binary Confusion Matrix:\n" followed by 2x2 matrix showing true vs predicted classifications 


3. Multi-Class Classification Results 

Prints blank line followed by: ===== Multi-Class Classification ===== 
Prints "Multi-Class Predictions:" followed by first 10 encoded predictions as array 
Prints blank line 
Prints "Multi-Class Accuracy:" followed by accuracy score 
Prints blank line 
Prints "Multi-Class Classification Report:\n" followed by detailed metrics for each sentiment class 
Prints "Multi-Class Confusion Matrix:\n" followed by NxN matrix where N is number of sentiment classes 


4. Multi-Label Classification Results 

Prints blank line followed by: ===== Multi-Label Classification ===== 
Prints "Multi-Label Predictions (first 5 rows):\n" followed by binary matrix (5 rows × number of emotion classes) 
Prints "Classes:" followed by array of emotion class names from mlb.classes_ 
Prints blank line 
Prints "Multi-Label Micro F1 Score:" followed by micro-averaged F1 score 
Prints "Multi-Label Macro F1 Score:" followed by macro-averaged F1 score 
Prints blank line 
Prints "Per-Label F1 Scores:" 
For each emotion class, prints on new line: "{emotion_name}: {f1_score:.4f}" 


5. Summary 

Prints blank line followed by: ========== SUMMARY ========== 
Prints "Binary Accuracy:" followed by binary classification accuracy 
Prints "Multi-Class Accuracy:" followed by multi-class classification accuracy 
Prints "Multi-Label Micro F1:" followed by micro F1 score 
Prints "Multi-Label Macro F1:" followed by macro F1 score 
Code constraints :
File and Data Constraints 



CSV Constraints: 

File must be CSV (.csv), Excel (.xlsx), or older Excel (.xls) format 
File must exist in the same directory as the Python script 
File must contain the text column for text processing (mandatory) 
File must contain binary_sentiment, sentiment, and emotion_labels columns for respective classification tasks 
File must contain at least 1 row of data (excluding header) 
If file format is unsupported, program prints "Only CSV or Excel files supported" and exits using sys.exit(1) 


Column Data Type Constraints: 

text: Must be text/string values containing content to analyze (mandatory) 
sentiment: Text/string values representing sentiment categories (negative, positive, neutral) 
binary_sentiment: Text/string values for binary classification (negative, positive) 
emotion_labels: Text/string values with comma-separated emotion tags (e.g., "love,sadness", "anger") 


Text Processing Constraints 

Text Cleaning (clean_text function in nlp_utils.py):

Converts all text to lowercase using .lower() 
Removes URLs and @ mentions using regex pattern r'http\S+|@\w+' 
Removes all non-alphabetic characters using regex pattern r'[^a-z\s]' 
Removes English stopwords from predefined ENGLISH_STOPWORDS set 
Removes extra whitespace by splitting and rejoining with single spaces 
Converts non-string inputs to string using str(text) 
Returns cleaned text string with only lowercase alphabetic characters and single spaces 


Multi-label Processing (split_labels function in nlp_utils.py): 

Handles comma-separated emotion labels 
Checks for NaN values using pd.isna(label_string) or empty strings 
Splits string by comma delimiter using .split(',') 
Strips whitespace from each label using .strip() 
Returns list of individual emotion labels 
Returns empty list [] for NaN or empty string inputs 
Preserves individual emotion tags as list elements for multi-label encoding 


Feature Extraction Constraints 

TF-IDF Vectorization: 

Maximum features: 2000 (max_features=2000) 
Uses TfidfVectorizer from sklearn.feature_extraction.text 
Applied within Pipeline for each classification task 
Fitted on training data's cleaned text 
Transforms both training and test data 
Converts text to numerical feature vectors 
Output: Sparse matrix representation of text features 
Each feature represents TF-IDF score (term importance) in the corpus 


Encoding Constraints 

Single-label Encoding (Sentiment): 

Uses LabelEncoder from sklearn.preprocessing 
Applied to 'sentiment' column for multi-class classification 
Transforms categorical sentiment values to integers (0, 1, 2, ...) 
Creates new column: sentiment_encoded in both train and test DataFrames 
Fitted on training data: le.fit_transform(train["sentiment"]) 
Transforms test data: le.transform(test["sentiment"]) 
Each unique sentiment category gets a unique integer label 


Multi-label Encoding (Emotion Labels): 

Uses MultiLabelBinarizer from sklearn.preprocessing 
Applied to 'emotion_labels' column after splitting into lists 
First converts comma-separated strings to lists using split_labels() function 
Creates new column: emotion_list with list of individual emotions 
Transforms emotion lists to binary matrix representation using .fit_transform() 
Each column in the matrix represents one unique emotion class 
Value of 1 indicates presence of that emotion, 0 indicates absence 
Enables handling multiple emotions per text sample simultaneously 
Output shape: (number_of_samples, number_of_unique_emotions) 
Fitted on training data: mlb.fit_transform(train["emotion_list"]) 
Transforms test data: mlb.transform(test["emotion_list"]) 


Model and Pipeline Constraints 

Binary Classification: 

Uses Pipeline with TfidfVectorizer (max_features=2000) and LogisticRegression (max_iter=1000) 
Target column: binary_sentiment 
Evaluation metrics: Accuracy, Classification Report, Confusion Matrix 


Multi-Class Classification: 

Uses Pipeline with TfidfVectorizer (max_features=2000) and MultinomialNB 
Target column: sentiment_encoded (encoded version of sentiment) 
Evaluation metrics: Accuracy, Classification Report, Confusion Matrix 


Multi-Label Classification: 

Uses Pipeline with TfidfVectorizer (max_features=2000) and OneVsRestClassifier(LogisticRegression(max_iter=1000)) 
Target: Binary matrix from MultiLabelBinarizer 
Evaluation metrics: Micro F1 Score, Macro F1 Score, Per-Label F1 Scores 
Uses average="micro" and average="macro" for aggregate metrics 
Uses average=None for per-label metrics 
Uses zero_division=0 to handle cases with no predictions for a class 


Program Processing Constraints 

Error Handling: 

If file format is unsupported, prints: "Only CSV or Excel files supported" and exits using sys.exit(1) 
Warnings are suppressed using warnings.simplefilter("ignore") 


General Processing: 

All processing steps are performed sequentially with clear section headings 
Uses .apply() method to apply functions to DataFrame columns 
All outputs include descriptive headers with ===== formatting for major sections 
Train-test split performed before any preprocessing or encoding 
Text cleaning applied identically to both train and test sets 
Encoders fitted only on training data, then applied to test data 


Module Structure: 

Main processing logic in main.py/solution.py with if __name__ == "__main__": main() entry point 
Reusable utility functions in separate nlp_utils.py module 
Clear separation of concerns between ML pipeline and text utilities 
Stopwords defined as module-level constant in nlp_utils.py
Sample test cases :
Input 1 :
Sample.csv
Output 1 :
Enter dataset filename (CSV or Excel): 
=== Dataset Preview ===
                                                text  ...                  emotion_labels
0      Sooo SAD I will miss you here in San Diego!!!  ...                    love,sadness
1                          my boss is bullying me...  ...                           anger
2                     what interview! leave me alone  ...         anger,confusion,disgust
3   Sons of ****, why couldn`t they put them on t...  ...  anticipation,boredom,confusion
4  2am feedings for the baby are fun when he is a...  ...                  excitement,joy

[5 rows x 4 columns]

===== Binary Classification =====
Binary Predictions: ['negative' 'negative' 'negative' 'negative']

Binary Accuracy: 0.5

Binary Classification Report:
               precision    recall  f1-score   support

    negative       0.50      1.00      0.67         2
    positive       0.00      0.00      0.00         2

    accuracy                           0.50         4
   macro avg       0.25      0.50      0.33         4
weighted avg       0.25      0.50      0.33         4

Binary Confusion Matrix:
 [[2 0]
 [2 0]]

===== Multi-Class Classification =====
Multi-Class Predictions: [0 0 0 0]

Multi-Class Accuracy: 0.25

Multi-Class Classification Report:
               precision    recall  f1-score   support

           0       0.25      1.00      0.40         1
           1       0.00      0.00      0.00         1
           2       0.00      0.00      0.00         2

    accuracy                           0.25         4
   macro avg       0.08      0.33      0.13         4
weighted avg       0.06      0.25      0.10         4

Multi-Class Confusion Matrix:
 [[1 0 0]
 [1 0 0]
 [2 0 0]]

===== Multi-Label Classification =====
Multi-Label Predictions (first 5 rows):
 [[0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 0]]
Classes: ['anger' 'anticipation' 'boredom' 'confusion' 'disgust' 'excitement'
 'fear' 'joy' 'love' 'sadness' 'surprise']

Multi-Label Micro F1 Score: 0.0
Multi-Label Macro F1 Score: 0.0

Per-Label F1 Scores:
anger: 0.0000
anticipation: 0.0000
boredom: 0.0000
confusion: 0.0000
disgust: 0.0000
excitement: 0.0000
fear: 0.0000
joy: 0.0000
love: 0.0000
sadness: 0.0000
surprise: 0.0000

========== SUMMARY ==========
Binary Accuracy: 0.5
Multi-Class Accuracy: 0.25
Multi-Label Micro F1: 0.0
Multi-Label Macro F1: 0.0