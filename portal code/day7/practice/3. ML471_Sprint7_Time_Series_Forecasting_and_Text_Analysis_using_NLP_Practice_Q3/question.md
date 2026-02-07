Multi File Programming Question
Problem Overview 



A natural language processing (NLP) research team is developing an entity recognition and information extraction pipeline for sports news content analysis. When processing news articles about athletics and competitions, it's crucial to identify key entities such as athletes (PERSON entities) and events (EVENT entities) to extract meaningful insights about competitions and achievements. The team needs a system that can automatically identify sentences where athletes are mentioned in the context of medals, as well as extract all competition and event names mentioned in the text. 



The team needs to understand how to effectively use spaCy's named entity recognition (NER) capabilities to extract structured information from unstructured sports news articles. 



Objectives 



As part of this information extraction analysis, the team needs to: 

Load and preview the text file – Import the text file containing news articles and display the first 300 characters to verify successful data loading and understand the content structure. 
Process with spaCy NER – Apply spaCy's named entity recognition to identify and classify entities in the text, enabling automated extraction of people, events, and other named entities. 
Extract medal-related sentences – Identify and display all sentences where a PERSON entity is mentioned alongside the word "medal" to track athlete achievements and aspirations. 
Extract competition names – Identify and extract all competition and event names mentioned in the articles by detecting EVENT entities and text patterns containing keywords like "Championship," "Run," or "Grand Prix." 
Remove duplicates – Generate a unique list of competitions to provide a clean summary of all events mentioned across multiple articles. 


This analysis will guide the team in building an automated sports news monitoring system that can track athlete achievements and upcoming competitions. 



Sample Data 



The input file contains unstructured news articles separated by delimiters. Each article includes: 



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


2. Sentences with PERSON followed by 'medal' 

Displays a section header: "=== Sentences with PERSON followed by 'medal' ===" 
Shows all sentences where a PERSON entity appears and the word "medal" is mentioned 
Each matching sentence is displayed with a bullet point (-) 
Format: "- {sentence text}" 
If no matching sentences found, displays: "No matching sentences found." 
Followed by a blank line separator 


3. Competitions Mentioned 

Displays a section header: "=== Competitions Mentioned ===" 
Shows a unique list of all competitions and events extracted from the text 
Each event is displayed with a bullet point (-) 
Format: "- {event name}" 
Events are extracted based on:  
Entities labeled as "EVENT" by spaCy 
Text containing keywords: "Championship", "Run", or "Grand Prix" 
Duplicates are automatically removed using set() 
If no events found, displays: "No events found." 


Refer to the sample output for exact formatting specifications. 

Code constraints :
File Constraints 

File must be a valid text file with .txt extension 
File must exist in the same directory as the Python script (using sys.path[0]) 
File encoding must be UTF-8 compatible 
If the file is not found, the program prints: "Error: File '{filename}' not found." and exits with status code 1 


Library Requirements 

The program uses spaCy library for NER and sentence segmentation 
Requires the en_core_web_sm language model to be installed 
If the spaCy model is not found, the program prints:  
"SpaCy model 'en_core_web_sm' not found. Install it using:" 
"python -m spacy download en_core_web_sm" 
Then exits with status code 1 


Processing Constraints 

The program suppresses warnings using warnings.simplefilter(action='ignore') 
TensorFlow warnings are suppressed via environment variable TF_CPP_MIN_LOG_LEVEL = '3' (hides INFO/WARNING messages) 
File reading uses UTF-8 encoding explicitly 
Entity recognition uses spaCy's built-in NER pipeline 
Sentence segmentation uses spaCy's sentence boundary detection 


Entity Extraction Constraints 

PERSON entity detection uses spaCy's entity label: ent.label_ == "PERSON" 
Medal context matching is case-insensitive: "medal" in sent.text.lower() 
Event extraction checks for EVENT entities: ent.label_ == "EVENT" 
Additional pattern matching for keywords: "Championship", "Run", "Grand Prix" 
Duplicate events are removed using set(unique_events) 


Output Constraints 

The original text preview displays exactly the first 300 characters using slicing content[:300] 
All section headers use === for emphasis 
Matching sentences are displayed with "- " prefix and .strip() applied 
Event names are displayed with "- " prefix 
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

=== Sentences with PERSON followed by 'medal' ===
- News Article 1

Claxton hunting first major medal

British hurdler Sarah Claxton is confident she can win her first major medal at next month's European Indoor Championships in Madrid.

=== Competitions Mentioned ===
- the Bupa Great Ireland Run
- World Cross Country Championships
- Birmingham Grand Prix
- European Indoor Championships