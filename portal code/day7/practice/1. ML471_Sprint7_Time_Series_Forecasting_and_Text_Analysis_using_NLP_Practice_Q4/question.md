Problem Overview 



A natural language processing (NLP) research team is developing an entity recognition and information extraction pipeline for sports news content analysis. When processing news articles about athletics and competitions, it's crucial to identify key entities such as athletes and sports events to extract meaningful insights about competitions and achievements. The team needs a system that can automatically identify specific athlete names and sporting events mentioned in the text using rule-based pattern matching with spaCy's PhraseMatcher. 



The team needs to understand how to effectively use spaCy's PhraseMatcher capabilities to extract structured information from unstructured sports news articles through predefined pattern lists. 



Objectives 



As part of this information extraction analysis, the team needs to: 



Load and preview the text file – Import the text file containing news articles and display the first 300 characters to verify successful data loading and understand the content structure. 
Process with spaCy – Load the spaCy language model and create a Doc object for linguistic processing, enabling automated extraction of structured information. 
Extract athlete names using rule-based matching – Use PhraseMatcher to identify and display mentions of specific athletes (Sarah Claxton, Sonia O'Sullivan, Irina Shevchenko) throughout the articles. 
Extract sports events using rule-based matching – Use PhraseMatcher to identify and extract specific competition names (European Indoor Championships, World Cross Country Championships, London marathon, Bupa Great Ireland Run) mentioned in the articles. 


This analysis will guide the team in building an automated sports news monitoring system that can track specific athletes and competitions using predefined pattern lists. 



Sample Data 



The input file contains unstructured news articles separated by delimiters. Each article includes: 



Article title/heading 
Article body with multiple paragraphs 
Separator lines (dashes) between articles 


News Article 1 



Claxton hunting first major medal 



British hurdler Sarah Claxton is confident she can win her first major medal at next month's European Indoor Championships in Madrid. 



The 25-year-old has already smashed the British record over 60m hurdles twice this season, setting a new mark of 7.96 seconds to win the AAAs title. "I am quite

Input format :
Text File Input:

The program prompts the user with: "Enter text file name: "
Input must include the file extension .txt
File should be located in the same directory as the Python script
File must be UTF-8 encoded
Output format :
The program generates the following outputs in sequence: 



1. Original Text Sample 

Displays the first 300 characters of the loaded text content 
Preceded by the header: "=== Original Text Sample (First 300 chars) ===" 
Provides a preview of the raw text before processing 
Followed by a blank line separator 


2. Matched Athlete Names 

Displays a section header: "=== Matched Athlete Names ===" 
Shows all instances where the predefined athlete names are found in the text 
Each matching athlete name is displayed with a bullet point (-) 
Format: "- {athlete name}" 
Matches are found using PhraseMatcher with patterns for: Sarah Claxton, Sonia O'Sullivan, Irina Shevchenko 
If no matching athletes found, displays: "No athlete names found." 
Followed by a blank line separator 


3. Matched Sports Events 

Displays a section header: "=== Matched Sports Events ===" 
Shows all instances where the predefined sports events are found in the text 
Each matching event is displayed with a bullet point (-) 
Format: "- {event name}" 
Matches are found using PhraseMatcher with patterns for: European Indoor Championships, World Cross Country Championships, London marathon, Bupa Great Ireland Run 
If no events found, displays: "No sports events found." 


Refer to the sample output for exact formatting specifications. 

Code constraints :
File Constraints 

File must be a valid text file with .txt extension 
File must exist in the same directory as the Python script (using sys.path[0]) 
File encoding must be UTF-8 compatible 
If the file is not found, the program prints: "Error: File '{filename}' not found." and exits with status code 1 


Library Requirements 

The program uses spaCy library for NLP processing and PhraseMatcher 
Requires the en_core_web_sm language model to be installed 
If the spaCy model is not found, the program prints:  
"SpaCy model 'en_core_web_sm' not found." 
"Install it using: python -m spacy download en_core_web_sm" 
Then exits with status code 1 


Processing Constraints 

The program suppresses warnings using warnings.simplefilter(action='ignore') 
TensorFlow warnings are suppressed via environment variable TF_CPP_MIN_LOG_LEVEL = '3' (hides INFO/WARNING messages) 
File reading uses UTF-8 encoding explicitly 
PhraseMatcher is used for rule-based entity matching with predefined patterns 


Pattern Matching Constraints 

Athlete name patterns are created using nlp.make_doc() for: "Sarah Claxton", "Sonia O'Sullivan", "Irina Shevchenko" 
Sports event patterns are created using nlp.make_doc() for: "European Indoor Championships", "World Cross Country Championships", "London marathon", "Bupa Great Ireland Run" 
PhraseMatcher performs exact phrase matching (case-sensitive by default) 
Matches are retrieved as tuples containing (match_id, start_token, end_token) 
Matched text spans are extracted using doc[start:end] 


Output Constraints 

The original text preview displays exactly the first 300 characters using slicing content[:300] 
All section headers use === for emphasis 
Matching names and events are displayed with "- " prefix 
Each match is displayed using span.text to show the matched phrase 
Blank lines (print()) separate all major output sections 
All print statements must match the exact format shown in the sample output, including spacing, line breaks, and formatting characters 
Sample test cases :
Input 1 :
Sample.txt
Output 1 :
Enter text file name: 
=== Original Text Sample (First 300 chars) ===
News Article 1

Claxton hunting first major medal

British hurdler Sarah Claxton is confident she can win her first major medal at next month's European Indoor Championships in Madrid.

The 25-year-old has already smashed the British record over 60m hurdles twice this season, setting a new mark of 7

=== Matched Athlete Names ===
- Sarah Claxton
- Irina Shevchenko
- Sonia O'Sullivan

=== Matched Sports Events ===
- European Indoor Championships
- World Cross Country Championships
- London marathon
- Bupa Great Ireland Run