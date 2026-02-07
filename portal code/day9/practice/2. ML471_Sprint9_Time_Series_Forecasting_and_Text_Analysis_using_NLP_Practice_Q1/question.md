Multi File Programming Question
Problem Statement 



Organizations need to analyze customer reviews to understand sentiment and emotional responses toward their products or services. Traditional sentiment analysis provides only positive/negative classifications, but real-world reviews contain complex, nuanced emotions. This project addresses the need for: 



Comprehensive text preprocessing – Clean and normalize raw review text by removing noise, URLs, mentions, punctuation, and stopwords to prepare data for feature extraction. 
Feature extraction – Convert cleaned text into numerical representations using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization to capture term importance across the review corpus. 
Multi-dimensional sentiment analysis – Support both binary sentiment classification and multi-label emotion detection to capture the full emotional spectrum in reviews. 


This preprocessing and encoding pipeline ensures that review data is transformed into a format suitable for training sophisticated machine learning models capable of understanding both overall sentiment and specific emotional nuances. 



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
The program generates the following outputs in sequence: 



1. First 5 Rows of Data: 

Prints the heading: === First 5 Rows === 
Displays the first 5 rows of the DataFrame using .head() 
Shows in tabular format with column names and row indices 
Displays all 4 columns: review, binary_sentiment, emotion_labels, sentiment 


2. Number of Samples: 

Prints a blank line 
Prints: "Number of samples: X" where X is the total number of rows in the dataset 


3. Data Types: 

Prints a blank line followed by: === Data Types === 
Lists all column names with their corresponding data types using .dtypes 
Shows data types (e.g., object, int64) 
Ends with dtype: object 


4. Train/Test Split Information: 

Prints a blank line 
Prints: "Train: X, Test: Y" where X is the number of training samples and Y is the number of test samples 
Default split ratio: 80% train, 20% test 


5. Sample Cleaned Text: 

Prints a blank line followed by: === Sample Cleaned Text === 
Displays comparison of original review text and cleaned text for first 5 samples 
Shows two columns: review and cleaned_text 
Demonstrates the text cleaning transformation 


6. TF-IDF Shapes: 

Prints a blank line followed by: === TF-IDF Shapes === 
Prints: "Train: (X, Y)" where X is number of train samples and Y is max_features (3000) 
Prints: "Test: (A, B)" where A is number of test samples and B is max_features (3000) 


7. Sentiment Mapping (if sentiment column exists): 

Prints a blank line followed by: === Sentiment Mapping === 
Displays dictionary mapping sentiment classes to encoded integer values 
Shows the LabelEncoder transformation: {'class1': 0, 'class2': 1, ...} 


8. Multi-label Classes (if emotion_labels column exists): 

Prints a blank line followed by: === Multi-label Classes === 
Shows array of unique emotion classes found using MultiLabelBinarizer 
Example: ['anger' 'disgust' 'fear' 'joy' 'sadness' 'surprise'] 
Prints: "Multi-label shape (train): (X, Y)" where X is number of train samples and Y is number of unique emotion classes 


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
Enter dataset filename (CSV or Excel): 
=== First 5 Rows ===
                                              review  ... sentiment
0  One of the other reviewers has mentioned that ...  ...  negative
1  A wonderful little production. <br /><br />The...  ...  positive
2  I thought this was a wonderful way to spend ti...  ...  positive
3  Basically there's a family where a little boy ...  ...  negative
4  Petter Mattei's "Love in the Time of Money" is...  ...  positive

[5 rows x 4 columns]

Number of samples: 10

=== Data Types ===
review              object
binary_sentiment    object
emotion_labels      object
sentiment           object
dtype: object

Train: 8, Test: 2

=== Sample Cleaned Text ===
                                              review                                       cleaned_text
0  Encouraged by the positive comments about this...  encouraged positive comments film looking forw...
1  A wonderful little production. <br /><br />The...  wonderful little production br br filming tech...
2  Probably my all-time favorite movie, a story o...  probably alltime favorite movie story selfless...
3  One of the other reviewers has mentioned that ...  one reviewers mentioned watching just oz episo...
4  This show was an amazing, fresh & innovative i...  show amazing fresh innovative idea s first air...

=== TF-IDF Shapes ===
Train: (8, 515) Test: (2, 515)

=== Sentiment Mapping ===
{'negative': 0, 'positive': 1}

=== Multi-label Classes ===
['anger' 'anticipation' 'boredom' 'confusion' 'disgust' 'excitement'
 'fear' 'joy' 'love' 'sadness' 'surprise' 'trust']
Multi-label shape (train): (8, 12)