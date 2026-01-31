# Problem Description

## Tokenization of Unstructured Sports News Articles Using spaCy

In Natural Language Processing (NLP), unstructured textual data such as news articles must be converted into structured components before meaningful analysis can be performed. One of the most important preprocessing steps is tokenization, which breaks down raw text into smaller units like words, punctuation marks, and symbols.

In this problem, you are given a text file containing multiple sports news articles written in free-form language. Your task is to read the content from the file, inspect a portion of the raw data, tokenize the complete text using spaCy, and analyze the total number of tokens produced.

## Objectives

Read the contents of the given text file containing sports news articles.
Display the first 10 lines of the extracted content.
Perform tokenization on the entire text using spaCy.
Display the first 20 tokens generated after tokenization.
Count and display the total number of tokens in the file.

## Input format :

CSV File Input:

The program prompts the user to enter the name of the txt file containing the needed data.
Input must include the file extension .txt

## Output format :

The program should print output in the following order:

First 10 lines from the input file
First 20 sample tokens obtained after tokenization
Total number of tokens in the complete file

Note: Exact token values and counts depend on spaCy’s tokenizer and are not hardcoded.

Refer to the sample output for exact formatting specifications.

Code constraints :
The input file is a plain text (.txt) file with unstructured content
Tokenization must be done using spaCy
English language model en_core_web_sm must be used
The solution must not manually split text using string methods
The program should handle missing spaCy models gracefully

## Sample test cases :

### Input 1 :

Sample.txt

### Output 1 :

News Article 1

Claxton hunting first major medal

British hurdler Sarah Claxton is confident she can win her first major medal at next month's European Indoor Championships in Madrid.

The 25-year-old has already smashed the British record over 60m hurdles twice this season, setting a new mark of 7.96 seconds to win the AAAs title. "I am quite confident," said Claxton. "But I take each race as it comes. "As long as I keep up my training but not do too much I think there is a chance of a medal." Claxton has won the national 60m hurdles title for the past three years but has struggled to translate her domestic success to the international stage. Now, the Scotland-born athlete owns the equal fifth-fastest time in the world this year. And at last week's Birmingham Grand Prix, Claxton left European medal favourite Russian Irina Shevchenko trailing in sixth spot.

For the first time, Claxton has only been preparing for a campaign over the hurdles - which could explain her leap in form. In previous seasons, the 25-year-old also contested the long jump but since moving from Colchester to London she has re-focused her attentions. Claxton will see if her new training regime pays dividends at the European Indoors which take place on 5-6 March.
News
Article
1

Claxton<br>
hunting<br>
first<br>
major<br>
medal

British<br>
hurdler<br>
Sarah<br>
Claxton<br>
is<br>
confident<br>
she<br>
can<br>
win<br>
her<br>
Total number of tokens: 261
