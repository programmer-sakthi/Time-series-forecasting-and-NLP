Problem Statement

Organizations need to analyze customer reviews to understand sentiment and emotional responses toward their products or services. Traditional sentiment analysis provides only positive/negative classifications, but real-world reviews contain complex, nuanced emotions.

This project addresses the need for:

Comprehensive text preprocessing – Clean and normalize raw review text by removing noise, URLs, mentions, punctuation, and stopwords to prepare data for feature extraction.
FastText data preparation – Convert cleaned text into FastText-compatible formats for binary, multi-class, and multi-label classification tasks.
Multi-dimensional sentiment analysis – Support binary sentiment classification, multi-class sentiment categorization, and multi-label emotion detection to capture the full emotional spectrum in reviews.

Solution Overview

This solution implements an end-to-end NLP pipeline for preparing customer review data for FastText model training through three complementary classification approaches:

1. Data Loading and Preprocessing

Dataset Loading:

Reads CSV file containing review data from the script directory
Validates file existence before processing
Handles missing values through dropna() operation
Train/Test Split:

Randomly splits dataset into training (80%) and testing (20%) sets
Uses fixed random state (42) for reproducibility
Drops test indices from original dataframe to ensure no overlap

2. FastText Format Generation

The system prepares three parallel training datasets in FastText format:

Binary Sentiment Classification:

Converts binary_sentiment values to FastText labels using **label** prefix
Combines labels with cleaned text: **label**<sentiment> <clean_text>
Saves to train_fasttext_bn.txt for binary classification training
Example format: **label**negative sooo sad miss san diego
Multi-Class Sentiment Analysis:

Converts sentiment categories to FastText labels using **label** prefix
Combines labels with cleaned text: **label**<sentiment_category> <clean_text>
Saves to train_fasttext_mc.txt for multi-class training
Example format: **label**negative bos bullying
Multi-Label Emotion Detection:

Processes comma-separated emotion labels
Converts each emotion to individual FastText labels with **label** prefix
Combines multiple labels with cleaned text: **label**<emotion1> **label**<emotion2> ... <clean_text>
Saves to train_fasttext_ml.txt for multi-label training
Example format: **label**love **label**sadness sooo sad miss san diego

3. Label Processing Functions

convert_multilabels Function:

Splits comma-separated emotion labels into individual emotions
Strips whitespace from each emotion tag
Adds **label** prefix to each emotion
Joins all labels with spaces for FastText format
Handles multiple emotions per review (e.g., "anger,confusion,disgust" → "**label**anger **label**confusion **label**disgust")

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

1. FastText Binary Training Data

Prints: ===== FASTTEXT BINARY TRAIN DATA =====
Displays the formatted binary classification data
Shows each training sample with **label**<binary_sentiment> <clean_text> format
Provides visibility into binary sentiment labeling structure

2. FastText Multi-Class Training Data

Prints: ===== FASTTEXT MULTI-CLASS TRAIN DATA =====
Displays the formatted multi-class classification data
Shows each training sample with **label**<sentiment> <clean_text> format
Demonstrates sentiment category labeling transformation

3. FastText Multi-Label Training Data

Prints: ===== FASTTEXT MULTI-LABEL TRAIN DATA =====
Displays the formatted multi-label classification data
Shows each training sample with **label**<emotion1> **label**<emotion2> ... <clean_text> format
Illustrates how multiple emotion labels are combined

4. Success Confirmation

Prints: fastText training files generated successfully
Confirms all three training files have been created

5. Installation Note

Prints: Separator line and installation reminder
Notes that fasttext module is not available in the current environment
Provides installation instruction: pip install fasttext

File Outputs

The program creates three training files:

train_fasttext_bn.txt – Binary sentiment classification training data
train_fasttext_mc.txt – Multi-class sentiment classification training data
train_fasttext_ml.txt – Multi-label emotion detection training data
Code constraints :
CSV Constraints

File must be named Sample.csv
File must be a comma-separated CSV (.csv)
File must exist in the same directory as the Python script
File must contain the clean_text, binary_sentiment, sentiment, and emotion_labels columns
File must contain at least 1 row of data (excluding header)

Column Data Type Constraints

clean_text: String values containing preprocessed review content
binary_sentiment: String/categorical values for binary classification
sentiment: String/categorical values representing sentiment categories
emotion_labels: String values with comma-separated emotion tags

Data Processing Constraints

Missing Value Handling:

All rows with any missing values are removed using dropna()
Ensures clean data for FastText format generation

Train/Test Split:

Default train ratio: 80% (frac=0.8)
Default test ratio: 20% (remaining data)
Random state: 42 for reproducibility
Uses random sampling with df.sample()

Label Formatting:

All FastText labels must start with **label** prefix
Binary labels use binary_sentiment values directly
Multi-class labels use sentiment category values
Multi-label format requires space-separated labels before text

File Writing:

Files are written without headers (header=False)
Files are written without row indices (index=False)
All files use UTF-8 encoding by default
Files overwrite existing files with same names

Program Processing Constraints

If Sample.csv file is not found, prints: "Dataset file not found." and exits
Warnings are suppressed using warnings.simplefilter("ignore")
All processing steps execute sequentially
FastText module installation reminder is displayed at the end
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

============================================================
NOTE: fasttext module is not available
Install it with: pip install fasttext
