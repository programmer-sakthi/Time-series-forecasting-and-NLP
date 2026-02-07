Problem Statement

Organizations need robust methods to evaluate and compare different sentiment analysis approaches. While traditional machine learning models provide baseline performance, newer technologies like fastText and GenAI offer alternative approaches. This project requires you to implement a comprehensive model comparison pipeline with the following components: 

Multi-model prediction framework – Implement three different prediction approaches (fastText, sklearn, and GenAI) to classify the same sentiment data and evaluate their relative performance. 
Utility functions module – Create reusable helper functions for text cleaning, data splitting, and preprocessing in a separate utility module (nlp_utils.py). 
Model alignment analysis – Compare predictions across models to identify where they agree or disagree, providing insights into model behavior and reliability. 
Confidence-based filtering – Analyze high-confidence predictions to understand when models are most certain and whether that confidence correlates with accuracy. 

This project requires you to write two separate Python files: nlp_utils.py containing helper functions and main.py (or Solution file.py) containing the main processing logic. 

CSV File Structure 

The input CSV file must contain the following columns: 

Sample Data 

review,binary_sentiment,emotion_labels,sentiment

"One of the other reviewers has mentioned that after watching just 1 Oz episode you'll be hooked. They are right, as this is exactly what happened with me.<br /><br />The first thing that struck me about Oz was its brutality and unflinching scenes of violence, which set in right from the word GO. Trust me, this is not a show for the faint hearted or timid...",1,"anger,fear,disgust","negative"

Code Structure Requirements 

You must create two separate Python files:

 

File 1: nlp_utils.py - Utility Functions Module 

This file must contain the following functions: 

clean_text(text) - Text cleaning function  

Input: Raw text string 
Output: Cleaned text string with stopwords removed 
Must convert to lowercase, remove URLs, mentions, special characters 
Must filter out English stopwords 
split_labels(label_string) - Multi-label splitting function  

Input: Comma-separated label string 
Output: List of individual labels 
Must handle NaN and empty values safely 
split_data(df, test_ratio=0.2, random_state=42) - Train/test split function  

Input: DataFrame, test_ratio, random_state 
Output: Tuple of (train_df, test_df) 
Must reset indexes after splitting 

File 2: main.py (Solution file.py) - Main Processing Script 

This file must: 

Import necessary libraries (pandas, os, sys, warnings, random) 
Import sklearn components (TfidfVectorizer, MultinomialNB, Pipeline) 
Import helper functions from nlp_utils.py 
Define a main() function containing all processing steps 
Include if name == "main": block to execute main() 
Input format :
CSV File Input: 

The program prompts the user to enter the name of the dataset file containing review data. 
Input must include the file extension .csv. 
Output format :
The program generates the following outputs in sequence: 

1. Multi-Class sklearn Sample Predictions 

Prints the heading: Multi-Class sklearn Sample Predictions: Displays the first 10 predictions from the sklearn pipeline as a list 

2. Multi-Class Accuracy Comparison 

Prints a formatted section: ============= MULTI-CLASS ACCURACY ============= Shows accuracy scores for all three models: 

fastText Accuracy: (rounded to 4 decimal places) 
sklearn Accuracy: (rounded to 4 decimal places) 
GenAI Accuracy: (rounded to 4 decimal places) 

3. Alignment Results 

Prints a formatted section: ============= ALIGNMENT RESULTS ============= Displays agreement percentages between model pairs: 

agree_ft_sk: Percentage where fastText and sklearn agree 
agree_ft_gen: Percentage where fastText and GenAI agree 
agree_sk_gen: Percentage where sklearn and GenAI agree 

4. High-Confidence fastText Predictions 

Prints: High-Confidence fastText Predictions: Shows 5 samples with confidence > 0.85 including: 

Original review text 
fastText prediction 
Confidence score 

5. Interpretation Analysis 

Prints a formatted section: ============= INTERPRETATION ============= 

Followed by three comparative analyses: 

a) Where fastText > sklearn? 

Shows 3 examples where fastText was correct but sklearn was wrong 
Displays: review, pred_ft, pred_sklearn 
b) Where sklearn > fastText? 

Shows 3 examples where sklearn was correct but fastText was wrong 
Displays: review, pred_sklearn, pred_ft 
c) Where GenAI > both? 

Shows 3 examples where GenAI was correct but both others were wrong 
Displays: review, pred_genai, pred_ft, pred_sklearn 
Code constraints :
CSV Constraints 

File must be a valid CSV (.csv) or Excel (.xlsx) file 
File must exist in the same directory as the Python scripts 
File must contain the review column for text processing 
File must contain sentiment_encoded column for classification 
File must contain at least 1 row of data (excluding header) 

Column Data Type Constraints 

review: Text/string values containing review content 
sentiment_encoded: Integer values representing sentiment classes 
clean_text: Text/string values (auto-generated if missing)

 

nlp_utils.py Implementation Constraints 

clean_text(text) function requirements: 

Must convert input to string using str(text) 
Convert all text to lowercase using .lower() 
Remove URLs using regex pattern r"http\S+" 
Remove mentions using pattern r"@\w+" 
Remove all non-alphabetic characters except spaces using r"[^a-z\s]" 
Filter out English stopwords from ENGLISH_STOPWORDS set 
Return cleaned string with words joined by spaces 

split_labels(label_string) function requirements: 

Must check for NaN values using pd.isna(label_string) 
Check for empty strings 
If NaN or empty, return empty list [] 
Split string by comma delimiter using .split(",") 
Strip whitespace from each label using .strip() 
Return list of individual labels 

split_data(df, test_ratio=0.2, random_state=42) function requirements: 

Use DataFrame.sample() with frac=1-test_ratio 
Use specified random_state for reproducibility 
Create test set using df.drop(train.index) 
Must reset indexes on both sets using .reset_index(drop=True) 
Return tuple: (train_df, test_df) 

main.py Implementation Constraints 

Step 1: File Path Configuration 

Accept filename from sys.argv[1] or default to "Sample.csv" 
Construct path using os.path.join(sys.path[0], filename) 
Check file existence using os.path.exists() 
Handle both CSV and Excel files appropriately 
Step 2: Train/Test Split 

Use split_data() function from nlp_utils 
Default test_ratio of 0.2 
Step 3: Text Cleaning 

Apply clean_text() to review column for both train and test 
Store result in clean_text column 
Step 3.1: Mock fastText Predictions 

Set random seed to 42 for reproducibility 
Extract unique labels from sentiment_encoded 
Create fasttext_predict_mock() function that randomly selects labels 
Apply to test set clean_text to create pred_ft column 
Step 3.2: sklearn Pipeline Predictions 

Create Pipeline with TfidfVectorizer(max_features=2000) and MultinomialNB() 
Fit on training clean_text and sentiment_encoded 
Predict on test clean_text to create pred_sklearn column 
Print first 10 predictions as list 
Step 3.3: Mock GenAI Predictions 

Extract unique labels from sentiment_encoded 
Create genai_predict_mock() function that randomly selects labels 
Apply to test set clean_text to create pred_genai column 
Step 3.4: Model Evaluation 

Calculate accuracy_score for all three models against y_true (test sentiment_encoded) 
Round all accuracies to 4 decimal places 
Print formatted accuracy comparison 
Step 3.5: Alignment Analysis 

Create boolean columns: agree_ft_sk, agree_ft_gen, agree_sk_gen 
Calculate mean of each agreement column 
Print alignment results 
Step 3.6: Confidence Analysis 

Generate mock confidence scores between 0.60 and 0.99 
Round to 3 decimal places 
Filter for confidence > 0.85 
Display first 5 high-confidence samples 
Step 3.7: Interpretation 

Filter and display 3 examples where fastText outperforms sklearn 
Filter and display 3 examples where sklearn outperforms fastText 
Filter and display 3 examples where GenAI outperforms both 
General Program Constraints 

Must suppress warnings using warnings.simplefilter("ignore") 
All file operations must use os.path.join(sys.path[0], filename) 
Print statements must match exact format with === delimiters 
Sample outputs must show specified number of rows using .head() 
Error handling must provide informative messages 
Random seed must be set to 42 for reproducible mock predictions 
Sample test cases :
Input 1 :
Sample.csv
Output 1 :

Multi-Class sklearn Sample Predictions:
[2, 2]

============= MULTI-CLASS ACCURACY =============
fastText Accuracy : 0.5
sklearn Accuracy : 0.5
GenAI Accuracy : 1.0

============= ALIGNMENT RESULTS =============
agree_ft_sk 1.0
agree_ft_gen 0.5
agree_sk_gen 0.5
dtype: float64

High-Confidence fastText Predictions:
review pred_ft ft_confidence
1 After seeing the 1996 remake, I thought it was... 2 0.887

============= INTERPRETATION =============

Where fastText > sklearn?
Empty DataFrame
Columns: [review, pred_ft, pred_sklearn]
Index: []

Where sklearn > fastText?
Empty DataFrame
Columns: [review, pred_sklearn, pred_ft]
Index: []

Where GenAI > both?
review ... pred_sklearn
0 I am a great fan of David Lynch and have every... ... 2

[1 rows x 4 columns]
