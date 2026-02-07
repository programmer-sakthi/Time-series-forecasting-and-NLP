Multi File Programming Question
Problem Overview 



A natural language processing (NLP) research team is developing an information extraction pipeline for a content analysis system. When processing textual data from news articles, it's crucial to identify and extract key entities such as people, locations, and temporal references. Named Entity Recognition (NER) is a fundamental NLP technique that automatically identifies and classifies named entities in unstructured text, enabling applications like content categorization, knowledge graph construction, and automated summarization. 



The team needs to implement an entity extraction system that can identify persons, geographical locations, and dates from news article datasets, providing both detailed entity listings and frequency statistics for downstream analysis. 



Objectives 



As part of this entity extraction analysis, the team needs to: 



Load and preview the text file – Import the text file containing news articles and display the first 300 characters to verify successful data loading and understand the content structure. 
Load the NER model – Initialize spaCy's pre-trained language model (en_core_web_sm) which includes named entity recognition capabilities for processing English text. 
Apply Named Entity Recognition – Process the entire document using spaCy's NER pipeline to identify and extract entities of three specific types:  
PERSON: Names of individuals (e.g., athletes, public figures) 
GPE (Geopolitical Entity): Countries, cities, states, and other geographical locations 
DATE: Temporal expressions including specific dates, months, years, and relative time references 
Display extracted entities – Show each identified entity along with its classification type in the format: entity_text (ENTITY_TYPE), providing a comprehensive view of all persons, locations, and dates mentioned in the document. 
Generate frequency statistics – Calculate and display the count of entities for each type (PERSON, GPE, DATE), enabling the team to understand the distribution and prevalence of different entity types in the content. 


This analysis will help the team build robust information extraction pipelines for automated content processing, knowledge base construction, and semantic analysis of news articles. 



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


2. Named Entities List 

Displays a section header: "=== Named Entities (PERSON, GPE, DATE) ===" 
Shows each extracted entity with its type classification 
Format: entity_text (ENTITY_TYPE) 
Lists all entities of types PERSON, GPE, and DATE found in the document 
Each entity appears on a separate line 
Followed by a blank line separator 


3. Entity Frequency Statistics 

Displays a section header: "=== Entity Frequency ===" 
Shows the count of entities for each type 
Format: ENTITY_TYPE: count 
Displays frequency for PERSON, GPE, and DATE entity types 
Each type appears on a separate line 


Refer to the sample output for exact formatting specifications. 

Code constraints :
File Constraints 

File must be a valid text file with .txt extension 
File must exist in the same directory as the Python script (using sys.path[0]) 
File encoding must be UTF-8 compatible 
If the file is not found, the program prints: "Error: File '{filename}' not found." and exits with status code 1 


Library Requirements 

The program uses spaCy library for Named Entity Recognition 
Requires the en_core_web_sm language model to be installed 
If the spaCy model is not found, the program prints:  
"SpaCy model 'en_core_web_sm' not found. Install it using:" 
"python -m spacy download en_core_web_sm" 
Then exits with status code 1 
The program uses Python's Counter from the collections module for frequency counting 


Processing Constraints 

The program suppresses warnings using warnings.simplefilter(action='ignore') 
TensorFlow warnings are suppressed via environment variable TF_CPP_MIN_LOG_LEVEL = '3' (hides INFO/WARNING messages) 
File reading uses UTF-8 encoding explicitly 
NER processing is performed on the entire document content using spaCy's pipeline 


Entity Recognition Constraints 

Only three entity types are extracted: PERSON, GPE, and DATE 
Entity filtering is performed using conditional check: if ent.label_ in ["PERSON", "GPE", "DATE"] 
Entity text is accessed via the .text attribute 
Entity type is accessed via the .label_ attribute 
All matching entities are displayed in the order they appear in the document
 

Frequency Counting Constraints 

Frequency statistics track the count of entity types, not individual entity instances 
Counter is initialized as Counter() from the collections module 
Entity type counts are incremented using entity_counter[ent.label_] += 1 
Only the three target entity types (PERSON, GPE, DATE) are counted 


Output Constraints 

The original text preview displays exactly the first 300 characters using slicing content[:300] 
Entity output format must match: entity_text (ENTITY_TYPE) 
Frequency output format must match: ENTITY_TYPE: count 
Blank lines (print()) separate all major output sections 
All section headers use === for emphasis 
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

=== Named Entities (PERSON, GPE, DATE) ===
Sarah Claxton (PERSON)
next month's (DATE)
Madrid (GPE)
25-year-old (DATE)
this season (DATE)
the past three years (DATE)
Scotland (GPE)
this year (DATE)
last week's (DATE)
previous seasons (DATE)
25-year-old (DATE)
Colchester (GPE)
London (GPE)
next month's (DATE)
St Etienne (GPE)
Athletics Ireland (GPE)
35-year-old (DATE)
France (GPE)
19-20 March (DATE)
last Saturday's (DATE)
Santry (GPE)
this week (DATE)
O'Sullivan (PERSON)
London (GPE)
17 April (DATE)
O'Sullivan (PERSON)
Australia (GPE)
Ireland (GPE)
three years (DATE)
last Saturday (DATE)
Jolene Byrne (PERSON)
Maria McCambridge (PERSON)
Fionnualla Britton (PERSON)
O'Sullivan (PERSON)
9 April (DATE)
Dublin (GPE)

=== Entity Frequency ===
PERSON: 7
DATE: 17
GPE: 12