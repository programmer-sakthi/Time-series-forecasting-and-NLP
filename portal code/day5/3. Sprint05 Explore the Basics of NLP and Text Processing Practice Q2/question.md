# Problem Description

## Identifying Frequently Used Words in a Sports News Article

When analyzing historical sports articles, identifying frequently occurring words helps uncover dominant themes and recurring references. Word frequency analysis is a fundamental NLP technique used in text summarization, topic modeling, and information retrieval.

In this problem, you are given a sports news article as input text. Using spaCy, you must tokenize the text, compute word frequencies, determine the most common tokens, and find the occurrence count of specific keywords.

## Objectives :

Extract the frequency count of all tokens in the document.
Identify the top 10 most common words/symbols/characters.
Determine the frequency of the words “Claxton” and “medal” in the input document.

## Input format :

CSV File Input:

The program prompts the user to enter the name of the txt file containing the needed data.
Input must include the file extension .txt

## Output format :

The program should print output in the following order:

Top 10 most common tokens with their frequencies
Frequency count of the word Claxton
Frequency count of the word medal

Exact frequency values depend on the input document.

Refer to the sample output for exact formatting specifications.

## Code constraints :

Tokenization must be done using spaCy
The text is unstructured and may include punctuation and special characters
Token comparison is case-sensitive
All symbols and punctuation are treated as valid tokens

## Sample test cases :

### Input 1 :

Sample.txt

### Output 1 :

```text
Top 10 most common tokens
in : 9
the : 8
. : 7
O'Sullivan : 5
- : 5
, : 5
: 3
Ireland : 3
on : 3
and : 3
Frequency of 'Claxton': 0
Frequency of 'medal': 0
```
