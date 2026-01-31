# Problem Description

## Identifying High-Frequency Common Words in Customer Review Text

In text analytics, common words such as articles, prepositions, and punctuation often occur frequently but provide little analytical value. Identifying these high-frequency tokens helps analysts decide which words should be ignored (e.g., as stopwords) so that meaningful insights can be extracted from customer reviews.

In this task, you are given an input document containing unstructured text. Using Natural Language Processing (NLP) techniques, you must analyze token frequencies and determine how often specific commonly occurring words and symbols appear.

## Objectives :

Identify the frequency counts of the following words/symbols in the input document:
the
at
has
. (period)
From the above list, determine which token has the highest frequency count.

## Input format :

CSV File Input:

The program prompts the user to enter the name of the txt file containing the needed data.
Input must include the file extension .txt

## Output format :

The program should print output in the following order:

Frequency count of each target word/symbol (the, at, has, .)
The word/symbol with the highest frequency and its count

Exact counts depend on the content of the input document.

Refer to the sample output for exact formatting specifications.

## Code constraints :

Tokenization must be done using spaCy
Frequency comparison is case-sensitive
Symbols and punctuation must be treated as valid tokens
No stopword removal should be applied before counting

## Sample test cases :

### Input 1 :

Sample.txt

### Output 1 :

Frequency of 'the': 2 <br/>
Frequency of 'at': 3 <br/>
Frequency of 'has': 3 <br/>
Frequency of '.': 2 <br/>
Highest frequency among targets: at → 3
