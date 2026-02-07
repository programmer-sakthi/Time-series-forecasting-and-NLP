Problem Statement

Organizations need to analyze customer reviews to understand sentiment and emotional responses toward their products or services. Traditional sentiment analysis provides only positive/negative classifications, but real-world reviews contain complex, nuanced emotions. This project requires you to implement a complete preprocessing pipeline with the following components:

Comprehensive text preprocessing – Implement text cleaning functions to normalize raw review text by removing noise, special characters, punctuation, and extra whitespace to prepare data for analysis.
Utility functions module – Create reusable helper functions for text cleaning, label splitting, and data splitting in a separate utility module (nlp_utils.py).
Data preparation for machine learning – Transform cleaned text into fastText-compatible format for efficient training of sentiment and emotion classification models.
Multi-dimensional sentiment analysis – Support binary sentiment classification, multi-class sentiment detection, and multi-label emotion recognition to capture the full emotional spectrum in reviews.

This project requires you to write two separate Python files: nlp_utils.py containing helper functions and main.py containing the main processing logic.

CSV File Structure

The input CSV file must contain the following columns:

Sample Data

review,binary_sentiment,emotion_labels,sentiment

"One of the other reviewers has mentioned that after watching just 1 Oz episode you'll be hooked. They are right, as this is exactly what happened with me.<br /><br />The first thing that struck me about Oz was its brutality and unflinching scenes of violence, which set in right from the word GO. Trust me, this is not a show for the faint hearted or timid...",1,"anger,fear,disgust","negative"

Code Structure Requirements

You must create two separate Python files:

File 1: nlp_utils.py - Utility Functions Module

This file must contain the following functions:

clean_text(text) - Text cleaning function

Input: Raw text string
Output: Cleaned text string
Must handle non-string inputs safely
split_labels(label_str) - Multi-label splitting function

Input: Comma-separated label string
Output: List of individual labels
Must handle NaN values safely
split_data(df, test_size=0.2, random_state=42) - Train/test split function

Input: DataFrame, test_size ratio, random_state
Output: Tuple of (train_df, test_df)
Must reset indexes after splitting

File 2: main.py - Main Processing Script

This file must:

Import necessary libraries (pandas, os, sys, warnings)
Import helper functions from nlp_utils.py
Define a main() function containing all processing steps
Include if **name** == "**main**": block to execute main()

Input format :
CSV File Input:

The program prompts the user to enter the name of the dataset file containing review data.
Input must include the file extension .csv.
Output format :
The program generates the following outputs in sequence:

1. Training Data Sample

Prints the heading: === Training Data Sample ===
Displays the first 5 rows of the training DataFrame using .head()
Shows in tabular format with column names and row indices
Displays all available columns including review, binary_sentiment, emotion_labels, sentiment

2. Test Data Sample

Prints a blank line followed by: === Test Data Sample ===
Displays the first 5 rows of the test DataFrame
Shows the same tabular format as training data

3. Binary FastText Format Sample (if binary_sentiment column exists)

Prints a blank line followed by: === Binary FastText Sample ===
Displays the first 5 formatted training examples for binary classification
Format: **label**<binary_sentiment> <cleaned_text>
Example: **label**1 one of the other reviewers has mentioned that after watching just 1 oz episode...

4. Multi-Class FastText Format Sample (if sentiment column exists)

Prints a blank line followed by: === Multi-Class FastText Sample ===
Displays the first 5 formatted training examples for multi-class sentiment
Format: **label**<sentiment> <cleaned_text>
Example: **label**negative one of the other reviewers has mentioned that after watching just 1 oz episode...

5. Multi-Label FastText Format Sample (if emotion_labels column exists)

Prints a blank line followed by: === Multi-Label FastText Sample ===
Displays the first 5 formatted training examples for multi-label emotion detection
Format: **label**<emotion1> **label**<emotion2> ... <cleaned_text>
Example: **label**anger **label**fear **label**disgust one of the other reviewers has mentioned...

6. File Generation

Three fastText-ready training files are created in the script directory:  
train_fasttext_bn.txt – Binary sentiment classification data
train_fasttext_mc.txt – Multi-class sentiment classification data
train_fasttext_ml.txt – Multi-label emotion detection data

Code constraints :
CSV Constraints

File must be a comma-separated CSV (.csv)
File must exist in the same directory as the Python scripts
File must contain the review column for text processing
File must contain at least 1 row of data (excluding header)
Supported file formats: CSV only

Column Data Type Constraints

review: Text/string values containing review content
binary_sentiment: Integer values (0 or 1) for binary classification
emotion_labels: Text/string values with comma-separated emotion tags
sentiment: Text/string values representing sentiment categories (e.g., "negative", "positive", "neutral")

nlp_utils.py Implementation Constraints

clean_text(text) function requirements:

Must check if input is a string using isinstance(text, str)
If not a string, return empty string ""
Convert all text to lowercase using .lower()
Remove all punctuation and special characters using regex pattern r"[^a-z0-9\s]"
Collapse multiple spaces into single spaces using re.sub(r"\s+", " ")
Strip leading and trailing whitespace using .strip()
Return cleaned string

split_labels(label_str) function requirements:

Must check for NaN values using pd.isna(label_str)
If NaN or missing, return empty list []
Split string by comma delimiter using .split(",")
Strip whitespace from each label using .strip()
Return list of individual emotion tags

split_data(df, test_size=0.2, random_state=42) function requirements:

Must use train_test_split from sklearn.model_selection
Default parameters: test_size=0.2, random_state=42
Must reset indexes on both train and test sets using .reset_index(drop=True)
Return tuple: (train_df, test_df)

main.py Implementation Constraints

Step 1: File Path Configuration

Hardcode filenames: train_file = "Sample.csv" and test_file = "Sample.csv"
Construct paths using os.path.join(sys.path[0], filename)

Step 2: Data Loading

Use try-except block to handle file loading errors
Load CSV files using pd.read_csv()
On error, print: f"Error loading files: {e}" and exit with sys.exit(1)
Drop all NaN rows using .dropna() on both train and test DataFrames

Step 3: Text Cleaning

Check if clean_text column already exists
If not, check for review column
If review exists, apply clean_text() function to create clean_text column
If review column not found, print error message and exit

Step 4: Binary FastText Formatting (conditional)

Only execute if binary_sentiment column exists
Create ft_label_binary column: '**label**' + binary_sentiment.astype(str)
Create ft_format_binary column: ft_label_binary + " " + clean_text
Print sample using .head().tolist() joined with newlines
Save to train_fasttext_bn.txt using .to_csv() with index=False, header=False

Step 5: Multi-Class FastText Formatting (conditional)

Only execute if sentiment column exists
Create ft_label_multiclass column for both train and test: '**label**' + sentiment.astype(str)
Create ft_format_multiclass column: ft_label_multiclass + " " + clean_text
Print sample from training data
Save to train_fasttext_mc.txt

Step 6: Multi-Label FastText Formatting (conditional)

Only execute if emotion_labels column exists
Define inner function convert_labels(row) that:  
Calls split_labels(row['emotion_labels']) to get list of emotions
Adds '**label**' prefix to each emotion
Joins all labels with spaces
Apply convert_labels() to create ft_label_multi column
Create ft_format_multi column: ft_label_multi + " " + clean_text
Print sample
Save to train_fasttext_ml.txt

General Program Constraints

Must suppress warnings using warnings.simplefilter("ignore")
All file operations must use os.path.join(sys.path[0], filename) for path construction
Print statements must match exact format with === delimiters
Sample outputs must show first 5 rows using .head()
All saved files must exclude headers and index columns
Column existence checks must be performed before processing
Error handling must provide informative messages and exit gracefully

FastText Format Constraints

Binary Classification:

Label prefix: **label** followed by binary_sentiment value (0 or 1)
Format structure: <label> <cleaned_text>
One label per sample
Multi-Class Classification:

Label prefix: **label** followed by sentiment category string
Format structure: <label> <cleaned_text>
One label per sample
Multi-Label Classification:

Label prefix: **label** for each emotion
Format structure: <label1> <label2> ... <labelN> <cleaned_text>
Multiple labels per sample separated by spaces
Each emotion gets its own **label** prefix
Sample test cases :
Input 1 :
Sample.csv
Output 1 :

=== Training Data Sample ===
review ... emotion_list
0 Stories about the possibility of a post-apocal... ... ['anger', 'anticipation', 'boredom', 'confusio...
1 I liked this movie I remember there was one ve... ... ['excitement', 'joy']
2 First off I want to say most of the people who... ... ['anger', 'anticipation', 'boredom', 'confusio...
3 I am a great fan of David Lynch and have every... ... ['anger', 'confusion', 'disgust', 'excitement'...
4 End Game started well, the least said about th... ... ['anger', 'anticipation', 'boredom', 'confusio...

[5 rows x 7 columns]

=== Test Data Sample ===
review ... emotion_list
0 Stories about the possibility of a post-apocal... ... ['anger', 'anticipation', 'boredom', 'confusio...
1 I liked this movie I remember there was one ve... ... ['excitement', 'joy']
2 First off I want to say most of the people who... ... ['anger', 'anticipation', 'boredom', 'confusio...
3 I am a great fan of David Lynch and have every... ... ['anger', 'confusion', 'disgust', 'excitement'...
4 End Game started well, the least said about th... ... ['anger', 'anticipation', 'boredom', 'confusio...

[5 rows x 7 columns]

=== Binary FastText Sample ===
**label**positive story possibility postapocalyptic future around age since creation sciencefiction genre per se fact today society responsible may become future near tomorrow abuse refusal see right eye center story whether good badbr br terry gilliam course natural kind film give movie decadent feel throughout showing society run ragged excess bringing forth sense imminent tragedy despite moment comedy world world twelve monkey transpires place mad run wild city collapsing filth neglect everything reek foreboding despite luminosity opening sequence madness loom every corner dark movie best linear despite plot twist hold examination one get better repeated viewingsbr br tragic event deadly virus unleashed onto humanity thus led extermination life planet known lead scientist future try make amends change humanity fate earth employing renegade citizen scum earth guinea pig go back time among one james cole underplayed great effect bruce willis cole could person dont know anything way doesnt matter since little one many expendable volunteer hint character sneak later get closer fulfilling mission know man dream dream may reality may already scene event br br constant sense deja vu keep popping throughout movie taken mental ward mistake meet jeffrey goines spastically played brad pitt oscarnominated frantically spews forth talk doom destruction later cole belief seen goines recurring dream man pushing boy aside escaping doesnt know later meet psychologist kathryn railly madeleine stowe one first reaction he insane shes seen becomes running notion throughout participation story passiveresistant active even slightly crazy believer something terrible coming way especially meet six year later seen cole time cole continues talking dream keep also play part blonde woman running aisle screaming help shot rung particular redheaded man ponytail jeffrey goines apparently escaped pushing little boy innocent bystander question arise event happened going happen really part better yet everyone smallest player part greater plot trick fabric time time one huge conveyor belt showing repetition fragment event slide br br question formulated masterful sequence includes key scene alfred hitchcock masterpiece vertigo madeleine elsterjudy barton mourns brief existence took notice say cole railly watch seat movie theatre hiding snippet dialog vertigo form foil dialog railly cole later cole awakens apparently dozed theatre go looking railly come facetoface disguise looking almost exactly like eva maria saint north northwest swelling bernard herrmann score play emergence judy barton dressed madeleine elster fascinating sequence improbable occurrence name actor film madeleine stowe play kathryn railly don blond wig grey trenchcoat call judy simmons helping insane man named james cole james stewart play detective try help insane madeleine elster later reappear twice first brunette judy barton later madeleine action reenaction play replay
**label**positive liked movie remember one well done scene movie riff randell played pj sol lying bed smoking pot begin visualize ramones room sing song want around cool stuffbr br fun energetic quirky cool yes ill admit ending wayway top far fetched doesnt matter fun fun movie sex pot rock n rocll foreverbr br read cheap trick band originally star know true
**label**positive first want say people give poor review dont like kind comedy movie great open mind arent afraid laugh stupid thingsbr br movie shot like tv show lot short clip compiled one long movie scene dont even dialog someone come something unexpected funny negative felt like wasted money popcorn icee way could eat drink anything movie constantly laughing honestly nervous drinking icee seeing something caused laugh shoot everywherebr br dont mind male nudity enjoy jackass movie jackass tv show viva la bam sake go see moviebr br dont like first movie tv show dont see see dont post bad review hardcore christian see bash doesnt seem right
**label**negative great fan david lynch everything he made dvd except hotel room hour twin peak movie found immediately grabbed andandwhat bunch crudely drawn black white cartoon loud foul mouthed unfunny maybe dont know whats good maybe bunch crap foisted public name david lynch make buck let make clear didnt care foul language part keep adjusting sound neighbor might highly disappointing release may well left deluxe box set curiosity highly recommend dont spend money
**label**negative end game started well least said end better seemed like thing happening keep plot going example reporter first inquisitive intelligent person half way something really stupid totally character given reason apart next scene wouldnt make sense without whole story could told minute would made average tv political drama brilliant cuba gooding jr watchable however james wood admirable job consideringbr br end game honestly one worst film ive ever seenand thats saying something ive seen gigli

=== Multi-Class FastText Sample ===
**label**positive story possibility postapocalyptic future around age since creation sciencefiction genre per se fact today society responsible may become future near tomorrow abuse refusal see right eye center story whether good badbr br terry gilliam course natural kind film give movie decadent feel throughout showing society run ragged excess bringing forth sense imminent tragedy despite moment comedy world world twelve monkey transpires place mad run wild city collapsing filth neglect everything reek foreboding despite luminosity opening sequence madness loom every corner dark movie best linear despite plot twist hold examination one get better repeated viewingsbr br tragic event deadly virus unleashed onto humanity thus led extermination life planet known lead scientist future try make amends change humanity fate earth employing renegade citizen scum earth guinea pig go back time among one james cole underplayed great effect bruce willis cole could person dont know anything way doesnt matter since little one many expendable volunteer hint character sneak later get closer fulfilling mission know man dream dream may reality may already scene event br br constant sense deja vu keep popping throughout movie taken mental ward mistake meet jeffrey goines spastically played brad pitt oscarnominated frantically spews forth talk doom destruction later cole belief seen goines recurring dream man pushing boy aside escaping doesnt know later meet psychologist kathryn railly madeleine stowe one first reaction he insane shes seen becomes running notion throughout participation story passiveresistant active even slightly crazy believer something terrible coming way especially meet six year later seen cole time cole continues talking dream keep also play part blonde woman running aisle screaming help shot rung particular redheaded man ponytail jeffrey goines apparently escaped pushing little boy innocent bystander question arise event happened going happen really part better yet everyone smallest player part greater plot trick fabric time time one huge conveyor belt showing repetition fragment event slide br br question formulated masterful sequence includes key scene alfred hitchcock masterpiece vertigo madeleine elsterjudy barton mourns brief existence took notice say cole railly watch seat movie theatre hiding snippet dialog vertigo form foil dialog railly cole later cole awakens apparently dozed theatre go looking railly come facetoface disguise looking almost exactly like eva maria saint north northwest swelling bernard herrmann score play emergence judy barton dressed madeleine elster fascinating sequence improbable occurrence name actor film madeleine stowe play kathryn railly don blond wig grey trenchcoat call judy simmons helping insane man named james cole james stewart play detective try help insane madeleine elster later reappear twice first brunette judy barton later madeleine action reenaction play replay
**label**positive liked movie remember one well done scene movie riff randell played pj sol lying bed smoking pot begin visualize ramones room sing song want around cool stuffbr br fun energetic quirky cool yes ill admit ending wayway top far fetched doesnt matter fun fun movie sex pot rock n rocll foreverbr br read cheap trick band originally star know true
**label**negative first want say people give poor review dont like kind comedy movie great open mind arent afraid laugh stupid thingsbr br movie shot like tv show lot short clip compiled one long movie scene dont even dialog someone come some
