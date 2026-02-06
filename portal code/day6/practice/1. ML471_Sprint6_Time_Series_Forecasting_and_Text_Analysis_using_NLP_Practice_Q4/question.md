# Problem Statement

A news organization wants to analyze text content from their article database to extract meaningful insights and prepare the data for natural language processing tasks. The editorial team needs to process raw text documents by removing common stop words, performing lemmatization, and creating cleaned versions suitable for text mining and content analysis.

As the first step in this text processing pipeline, the team needs to:

Load and read text file – Prompt the user to enter a text filename, then import the file containing news articles and display its content for verification.
Process text with spaCy NLP – Load the spaCy English language model (en_core_web_sm) and process the entire document to enable linguistic analysis including tokenization, lemmatization, and part-of-speech tagging.
Initialize stop words collection – Load the default spaCy English stop words set to filter out common words that don't contribute significant meaning to the analysis.
Customize stop word list – Add domain-specific stop words (officially, announced, present, run) that are common but not meaningful in sports news context, while removing certain words (hence, every, he) that may carry important contextual information.
Filter and lemmatize tokens – Extract tokens from the document by converting them to lowercase lemmatized forms, excluding stop words, punctuation marks, and whitespace characters to create a clean token list.
Display filtered results – Show the first 20 filtered tokens to verify the preprocessing quality and provide a preview of the cleaned data structure.
Generate cleaned text – Reconstruct the processed text by joining all filtered tokens with spaces and display the first 200 characters as a sample of the final cleaned output.

This text preprocessing pipeline forms the foundation for downstream NLP tasks such as topic modeling, sentiment analysis, keyword extraction, and document classification.

The input file contains unstructured news articles separated by delimiters. Each article includes:

Article title/heading
Article body with multiple paragraphs
Separator lines (dashes) between articles

## Sample Data

News Article 1

Claxton hunting first major medal

British hurdler Sarah Claxton is confident she can win her first major medal at next month's European Indoor Championships in Madrid.

The 25-year-old has already smashed the British record over 60m hurdles twice this season, setting a new mark of 7.96 seconds to win the AAAs title.

...

## Input format :

### CSV File Input:

The program prompts the user to enter the name of the text file containing news articles.
Input must include the file extension .txt.
File should be located in the same directory as the Python script.
Output format :
The program generates the following outputs in sequence:

Filtered Tokens (First 20):

Displays a Python list showing the first 20 lemmatized tokens after stop word removal.
Format: ['token1', 'token2', 'token3', ...]
Followed by a blank line.

Cleaned Text Sample:

Prints the first 200 characters of the reconstructed text.
Tokens are joined with single spaces.
Shows processed, lemma-form text suitable for analysis.

Refer to the sample output for exact formatting specifications.

## Code constraints :

### Text File Constraints

File must be a valid UTF-8 encoded text file with .txt extension.
File must exist in the same directory as the Python script.
File can contain multiple paragraphs and sections separated by line breaks.
Special formatting like --- separators is acceptable and will be filtered during processing.

### Processing Constraints

The program uses spaCy (en_core_web_sm model) for NLP processing.
If the file is not found, the program prints "Error: File not found" and exits with status code 1.
Stop words are sourced from spacy.lang.en.stop_words.STOP_WORDS.
Custom stop words added: {"officially", "announced", "present", "run"}
Stop words removed from filter: {"hence", "every", "he"}
Token filtering excludes: stop words (case-insensitive), punctuation marks, and whitespace characters.
All tokens are converted to lowercase lemma forms for normalization.
The filtered tokens list displays exactly the first 20 tokens.
The cleaned text sample displays exactly the first 200 characters of the joined token string.

## Sample test cases :

### Input 1 :

Sample.txt

### Output 1 :

Enter text file name: Filtered Tokens (First 20):
['news', 'article', '1', 'claxton', 'hunt', 'major', 'medal', 'british', 'hurdler', 'sarah', 'claxton', 'confident', 'win', 'major', 'medal', 'month', 'european', 'indoor', 'championships', 'madrid']

Cleaned Text Sample:
news article 1 claxton hunt major medal british hurdler sarah claxton confident win major medal month european indoor championships madrid 25 year old smash british record 60 m hurdle twice season set
