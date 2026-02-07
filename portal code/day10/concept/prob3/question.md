Problem Statement

Organizations need to analyze customer reviews to understand sentiment and emotional responses toward their products or services. Traditional sentiment analysis provides only positive/negative classifications, but real-world reviews contain complex, nuanced emotions.

This project addresses the need for:

Comprehensive model comparison – Evaluate multiple machine learning approaches (fastText, sklearn Naive Bayes, and GenAI) on the same sentiment classification task to understand their relative strengths and weaknesses.

Multi-class sentiment classification – Categorize reviews into distinct sentiment classes to capture nuanced emotional states beyond simple positive/negative labels.

Model alignment analysis – Assess agreement between different models to identify where models converge and diverge in their predictions, revealing potential areas for ensemble methods or model improvement.

Solution Overview

This solution implements an end-to-end sentiment analysis pipeline that compares three different classification approaches on customer review data through comprehensive accuracy measurement and alignment analysis:

1. Data Loading and Preprocessing

Dataset Loading:

Prompts user for CSV filename input
Reads CSV file containing review data from the script directory
Validates file existence before processing
Displays first 5 rows for data verification

Data Cleaning:

Creates separate train and test dataframes (both initially full copies)
Fills missing values in clean_text column with empty strings
Removes rows with empty or whitespace-only text
Converts all text to lowercase for consistency

Label Encoding:

Creates label mapping from unique sentiment values to numeric indices
Encodes sentiment labels in both train and test datasets
Generates y_true array from test set for evaluation (after cleaning)

2. Multi-Model Prediction Pipeline

Mock fastText Predictor:

Simulates fastText predictions using random selection
Uses fixed random seed (42) for reproducibility
Randomly selects sentiment labels from available classes
Stores predictions in pred_ft column
sklearn Naive Bayes Classifier:

Creates pipeline with TfidfVectorizer (max 2000 features) and MultinomialNB
Trains on clean_text and sentiment_encoded from training data
Generates predictions on test set
Stores predictions in pred_sklearn column

Mock GenAI Predictor:

Simulates GenAI predictions using random selection
Uses fixed random seed (42) for reproducibility
Randomly selects sentiment labels from available classes
Stores predictions in pred_genai column

3. Model Evaluation and Alignment Analysis

Accuracy Calculation:

Computes accuracy scores for all three models against y_true
Maps categorical predictions back to encoded labels for comparison
Displays rounded accuracy values (4 decimal places)

Alignment Comparison:

Creates boolean columns for pairwise model agreement:  
agree_ft_sk: fastText vs sklearn agreement
agree_ft_gen: fastText vs GenAI agreement
agree_sk_gen: sklearn vs GenAI agreement
Calculates mean agreement rates across all test samples
Displays alignment results as percentages

Prediction Inspection:

Generates sample fastText raw predictions with confidence scores
Displays first 5 samples with clean_text and prediction tuples

Comparative Analysis:

Identifies cases where fastText outperforms sklearn (agrees with GenAI but sklearn doesn't)
Identifies cases where sklearn outperforms fastText (agrees with GenAI but fastText doesn't)
Identifies cases where GenAI correctly predicts when both other models fail
Displays top 3 examples for each scenario

CSV File Structure

The input CSV file must contain the following columns:

Sample Data

text,sentiment,binary_sentiment,emotion_labels,clean_text,sentiment_encoded,emotion_list

Sooo SAD I will miss you here in San Diego!!!,negative,negative,"love,sadness",sooo sad miss san diego,0,"['love', 'sadness']"

my boss is bullying me...,negative,negative,anger,bos bullying,0,['anger']

what interview! leave me alone,negative,negative,"anger,confusion,disgust",interview leave alone,0,"['anger', 'confusion', 'disgust']"

Sons of \*\*\*\*, why couldn`t they put them on the releases we already bought,negative,negative,"anticipation,boredom,confusion",son couldnt put release already bought,0,"['anticipation', 'boredom', 'confusion']"

2am feedings for the baby are fun when he is all smiles and coos,positive,positive,"excitement,joy",feeding baby fun smile coo,2,"['excitement', 'joy']"

Input format :
CSV File Input:

The program prompts the user to enter the name of the dataset file containing review data.
Input must include the file extension .csv.
Output format :
The program generates outputs in the following exact sequence:

1. Data Preview

Prints: First 5 rows from the file:
Displays the first 5 rows of the loaded dataset
Provides immediate verification of data structure and content

2. Model Accuracy Results

Prints: fastText Accuracy: followed by rounded accuracy score
Prints: sklearn Accuracy: followed by rounded accuracy score
Prints: GenAI Accuracy: followed by rounded accuracy score
All accuracy values rounded to 4 decimal places

3. Alignment Results

Prints: Alignment Results:
Displays mean agreement rates for each model pair:  
agree_ft_sk: Proportion of predictions where fastText and sklearn agree
agree_ft_gen: Proportion of predictions where fastText and GenAI agree
agree_sk_gen: Proportion of predictions where sklearn and GenAI agree

4. Sample Predictions

Prints: Sample fastText raw predictions:
Displays first 5 rows with clean_text and raw prediction tuples
Shows predicted label and confidence score pairs

5. Comparative Analysis Sections

Where fastText > sklearn:

Prints: Where fastText > sklearn?
Displays top 3 cases where fastText agrees with GenAI but sklearn doesn't
Where sklearn > fastText:

Prints: Where sklearn > fastText?
Displays top 3 cases where sklearn agrees with GenAI but fastText doesn't
Where GenAI > both:

Prints: Where GenAI > both?
Displays top 3 cases where GenAI predicts correctly but both fastText and sklearn fail
Code constraints :
CSV Constraints

File must exist in the same directory as the Python script
File must be a comma-separated CSV (.csv)
File must contain the required columns: clean_text, sentiment, sentiment_encoded
File must contain at least 1 row of data (excluding header)

Column Data Type Constraints

clean_text: String values containing preprocessed review content
sentiment: String/categorical values representing sentiment categories
sentiment_encoded: Numeric encoding corresponding to sentiment labels
emotion_labels: String values with comma-separated emotion tags (optional for this script)

Data Processing Constraints

Missing Value Handling:

Missing values in clean_text are filled with empty strings
Rows with empty or whitespace-only text are removed after filling
Ensures clean data for all model predictions

Label Encoding:

Creates dynamic label mapping from unique sentiment values
Maps sentiment categories to sequential integer indices
Maintains consistent encoding across train and test sets

Random Seed:

Fixed random seed (42) for mock predictions
Ensures reproducible results across multiple runs
Applies to both fastText and GenAI mock predictors

Model Training Constraints

TfidfVectorizer limited to maximum 2000 features
MultinomialNB uses default parameters
Pipeline trains on full training dataset without validation split
No hyperparameter tuning or cross-validation performed

Program Processing Constraints

Warnings are suppressed using warnings.simplefilter(action='ignore')
File not found errors trigger error message and program exit
All processing steps execute sequentially
Predictions stored in dataframe columns for easy comparison and analysis
Sample test cases :
Input 1 :
Sample.csv
Output 1 :
First 5 rows from the file:
text ... emotion_list
0 Sooo SAD I will miss you here in San Diego!!! ... ['love', 'sadness']
1 my boss is bullying me... ... ['anger']
2 what interview! leave me alone ... ['anger', 'confusion', 'disgust']
3 Sons of \*\*\*\*, why couldn`t they put them on t... ... ['anticipation', 'boredom', 'confusion']
4 2am feedings for the baby are fun when he is a... ... ['excitement', 'joy']

[5 rows x 7 columns]

fastText Accuracy: 0.4375
sklearn Accuracy: 1.0
GenAI Accuracy: 0.4375

Alignment Results:
agree_ft_sk 0.4375
agree_ft_gen 1.0000
agree_sk_gen 0.4375
dtype: float64

Sample fastText raw predictions:
clean_text ft_pred_raw
0 sooo sad miss san diego (negative, 0.029797219438070344)
1 bos bullying (negative, 0.2326608933907396)
2 interview leave alone (neutral, 0.026535969683863625)
3 son couldnt put release already bought (negative, 0.7160196129224035)
4 feeding baby fun smile coo (neutral, 0.5449414806032167)

Where fastText > sklearn?
text ... ft_pred_raw
0 Sooo SAD I will miss you here in San Diego!!! ... (negative, 0.029797219438070344)
3 Sons of \*\*\*\*, why couldn`t they put them on t... ... (negative, 0.7160196129224035)
5 Soooo high ... (negative, 0.4492090462838536)

[3 rows x 14 columns]

Where sklearn > fastText?
Empty DataFrame
Columns: [text, sentiment, binary_sentiment, emotion_labels, clean_text, sentiment_encoded, emotion_list, pred_ft, pred_sklearn, pred_genai, agree_ft_sk, agree_ft_gen, agree_sk_gen, ft_pred_raw]
Index: []

Where GenAI > both?
Empty DataFrame
Columns: [text, sentiment, binary_sentiment, emotion_labels, clean_text, sentiment_encoded, emotion_list, pred_ft, pred_sklearn, pred_genai, agree_ft_sk, agree_ft_gen, agree_sk_gen, ft_pred_raw]
Index: []
