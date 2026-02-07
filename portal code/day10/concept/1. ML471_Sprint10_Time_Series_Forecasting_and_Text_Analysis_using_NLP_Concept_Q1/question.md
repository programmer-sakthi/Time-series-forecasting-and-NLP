Problem Statement

Organizations need to analyze customer reviews to understand sentiment and emotional responses toward their products or services. Traditional sentiment analysis provides only positive/negative classifications, but real-world reviews contain complex, nuanced emotions.

This project addresses the need for:

Comprehensive text preprocessing – Clean and normalize raw review text by removing noise, URLs, mentions, punctuation, and stopwords to prepare data for feature extraction.
Feature extraction – Convert cleaned text into numerical representations using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization to capture term importance across the review corpus.
Multi-dimensional sentiment analysis – Support both binary sentiment classification and multi-label emotion detection to capture the full emotional spectrum in reviews.

This project requires you to write two separate Python files: nlp_utils.py containing helper functions and main.py (or Solution file.py) containing the main processing logic.

CSV File Structure

The input CSV file must contain the following columns:

Sample Data

text,sentiment,binary_sentiment,emotion_labels,clean_text,sentiment_encoded,emotion_list

Sooo SAD I will miss you here in San Diego!!!,negative,negative,"love,sadness",sooo sad miss san diego,0,"['love', 'sadness']"

my boss is bullying me...,negative,negative,anger,bos bullying,0,['anger']

what interview! leave me alone,negative,negative,"anger,confusion,disgust",interview leave alone,0,"['anger', 'confusion', 'disgust']"

Sons of \*\*\*\*, why couldn`t they put them on the releases we already bought,negative,negative,"anticipation,boredom,confusion",son couldnt put release already bought,0,"['anticipation', 'boredom', 'confusion']"

2am feedings for the baby are fun when he is all smiles and coos,positive,positive,"excitement,joy",feeding baby fun smile coo,2,"['excitement', 'joy']"

Solution Overview

This solution implements an end-to-end NLP pipeline for analyzing customer reviews through three complementary classification approaches:

FastText Format Generation (Solution file.txt)

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

Binary Classification Format:

Prepends **label** prefix to binary sentiment values
Combines formatted label with cleaned text
Saves to train_fasttext_bn.txt for FastText binary classification

Multi-Class Classification Format:

Prepends **label** prefix to sentiment categories
Combines formatted label with cleaned text
Saves to train_fasttext_mc.txt for FastText multi-class classification

Multi-Label Classification Format:

Converts comma-separated emotion labels to space-separated FastText format
Each emotion gets **label** prefix
Combines all emotion labels with cleaned text
Saves to train_fasttext_ml.txt for FastText multi-label classification
Input format :
CSV File Input:

The program prompts the user to enter the name of the dataset file containing review data.
Input must include the file extension .csv.
Output format :
The program generates the following outputs in sequence:

1. Multi-Class sklearn Sample Predictions

Prints the heading: Multi-Class sklearn Sample Predictions: Displays the first 10 predictions from the sklearn pipeline as a list

2. Multi-Class Accuracy Comparison

Prints a formatted section: "============= MULTI-CLASS ACCURACY ============= "
Shows accuracy scores for all three models:
fastText Accuracy: (rounded to 4 decimal places)
sklearn Accuracy: (rounded to 4 decimal places)
GenAI Accuracy: (rounded to 4 decimal places)

3. Alignment Results

Prints a formatted section: "============= ALIGNMENT RESULTS ============= "
Displays agreement percentages between model pairs:
agree_ft_sk: Percentage where fastText and sklearn agree
agree_ft_gen: Percentage where fastText and GenAI agree
agree_sk_gen: Percentage where sklearn and GenAI agree

4. High-Confidence fastText Predictions

Prints: High-Confidence fastText Predictions: Shows 5 samples with confidence > 0.85 including:
Original review text
fastText prediction
Confidence score

5. Interpretation Analysis

Prints a formatted section: " ============= INTERPRETATION ============= "
Followed by three comparative analyses:
a) Where fastText > sklearn?
Shows 3 examples where fastText was correct but sklearn was wrong
Displays: review, pred_ft, pred_sklearn
b) Where sklearn > fastText?
Shows 3 examples where sklearn was correct but fastText was wrong
Displays: review, pred_sklearn, pred_ft
c) Where GenAI > both?
Shows 3 examples where GenAI was correct but both others were wrong
Displays: review, pred_genai, pred_ft, pred_sklearn

Code constraints :
CSV Constraints

File must be a valid CSV (.csv) or Excel (.xlsx) file
File must exist in the same directory as the Python scripts
File must contain the review column for text processing
File must contain sentiment_encoded column for classification
File must contain at least 1 row of data (excluding header)

Column Data Type Constraints

review: Text/string values containing review content
sentiment_encoded: Integer values representing sentiment classes
clean_text: Text/string values (auto-generated if missing)

nlp_utils.py Implementation Constraints

clean_text(text) function requirements:

Must convert input to string using str(text)
Convert all text to lowercase using .lower()
Remove URLs using regex pattern r"http\S+"
Remove mentions using pattern r"@\w+"
Remove all non-alphabetic characters except spaces using r"[^a-z\s]"
Filter out English stopwords from ENGLISH_STOPWORDS set
Return cleaned string with words joined by spaces

split_labels(label_string) function requirements:

Must check for NaN values using pd.isna(label_string)
Check for empty strings
If NaN or empty, return empty list []
Split string by comma delimiter using .split(",")
Strip whitespace from each label using .strip()
Return list of individual labels

split_data(df, test_ratio=0.2, random_state=42) function requirements:

Use DataFrame.sample() with frac=1-test_ratio
Use specified random_state for reproducibility
Create test set using df.drop(train.index)
Must reset indexes on both sets using .reset_index(drop=True)
Return tuple: (train_df, test_df)

main.py Implementation Constraints

Step 1: File Path Configuration

Accept filename from sys.argv[1] or default to "Sample.csv"
Construct path using os.path.join(sys.path[0], filename)
Check file existence using os.path.exists()
Handle both CSV and Excel files appropriately
Step 2: Train/Test Split

Use split_data() function from nlp_utils
Default test_ratio of 0.2
Step 3: Text Cleaning

Apply clean_text() to review column for both train and test
Store result in clean_text column
Step 3.1: Mock fastText Predictions

Set random seed to 42 for reproducibility
Extract unique labels from sentiment_encoded
Create fasttext_predict_mock() function that randomly selects labels
Apply to test set clean_text to create pred_ft column
Step 3.2: sklearn Pipeline Predictions

Create Pipeline with TfidfVectorizer(max_features=2000) and MultinomialNB()
Fit on training clean_text and sentiment_encoded
Predict on test clean_text to create pred_sklearn column
Print first 10 predictions as list
Step 3.3: Mock GenAI Predictions

Extract unique labels from sentiment_encoded
Create genai_predict_mock() function that randomly selects labels
Apply to test set clean_text to create pred_genai column
Step 3.4: Model Evaluation

Calculate accuracy_score for all three models against y_true (test sentiment_encoded)
Round all accuracies to 4 decimal places
Print formatted accuracy comparison
Step 3.5: Alignment Analysis

Create boolean columns: agree_ft_sk, agree_ft_gen, agree_sk_gen
Calculate mean of each agreement column
Print alignment results
Step 3.6: Confidence Analysis

Generate mock confidence scores between 0.60 and 0.99
Round to 3 decimal places
Filter for confidence > 0.85
Display first 5 high-confidence samples
Step 3.7: Interpretation

Filter and display 3 examples where fastText outperforms sklearn
Filter and display 3 examples where sklearn outperforms fastText
Filter and display 3 examples where GenAI outperforms both

General Program Constraints

Must suppress warnings using warnings.simplefilter("ignore")
All file operations must use os.path.join(sys.path[0], filename)
Print statements must match exact format with === delimiters
Sample outputs must show specified number of rows using .head()
Error handling must provide informative messages
Random seed must be set to 42 for reproducible mock predictions
Sample test cases :
Input 1 :
Sample.csv
Output 1 :

===== FASTTEXT BINARY TRAIN DATA =====
0 **label**negative sooo sad miss san diego
1 **label**negative bos bullying
5 **label**negative soooo high
14 **label**negative gotta restart computer thoug...
13 **label**positive playing ghost online really ...
11 **label**negative ive sick past day thus hair ...
8 **label**positive really really like song love...
9 **label**negative sharpie running dangerously ...
2 **label**negative interview leave alone
15 **label**positive free fillin app ipod fun im ...
4 **label**positive feeding baby fun smile coo
7 **label**negative much love hopeful reckon cha...
10 **label**negative want go music tonight lost v...
Name: ft_format_binary, dtype: object

===== FASTTEXT MULTI-CLASS TRAIN DATA =====
0 **label**negative sooo sad miss san diego
1 **label**negative bos bullying
5 **label**neutral soooo high
14 **label**neutral gotta restart computer though...
13 **label**positive playing ghost online really ...
11 **label**negative ive sick past day thus hair ...
8 **label**positive really really like song love...
9 **label**negative sharpie running dangerously ...
2 **label**negative interview leave alone
15 **label**positive free fillin app ipod fun im ...
4 **label**positive feeding baby fun smile coo
7 **label**neutral much love hopeful reckon chan...
10 **label**negative want go music tonight lost v...
Name: ft_format_multiclass, dtype: object

===== FASTTEXT MULTI-LABEL TRAIN DATA =====
0 **label**love **label**sadness sooo sad miss s...
1 **label**anger bos bullying
5 **label**excitement soooo high
14 **label**boredom gotta restart computer though...
13 **label**disgust **label**surprise playing gho...
11 **label**disgust ive sick past day thus hair l...
8 **label**joy **label**love **label**surprise r...
9 **label**fear sharpie running dangerously low ink
2 **label**anger **label**confusion **label**dis...
15 **label**excitement **label**joy free fillin a...
4 **label**excitement **label**joy feeding baby ...
7 **label**anticipation **label**joy **label**lo...
10 **label**confusion **label**sadness want go mu...
Name: ft_format_multilabel, dtype: object

fastText training files generated successfully
