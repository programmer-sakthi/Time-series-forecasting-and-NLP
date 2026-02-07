
import sys
import os
import warnings
from collections import Counter

warnings.simplefilter(action='ignore')

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

try:
    import spacy
except ImportError:
    print("SpaCy library not found. Please install it using: pip install spacy")
    sys.exit(1)

def load_text_file(file_name):
    script_dir = sys.path[0]
    file_path = os.path.join(script_dir, file_name)

    if not os.path.exists(file_path):
        print(f"Error: File '{file_name}' not found.")
        sys.exit(1)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except Exception as e:
        print(f"Error reading file '{file_name}': {e}")
        sys.exit(1)

def load_ner_model():
    
    try:
        nlp = spacy.load("en_core_web_sm")
        return nlp
    except OSError:
        print("SpaCy model 'en_core_web_sm' not found. Install it using:")
        print("python -m spacy download en_core_web_sm")
        sys.exit(1)

def process_text_for_entities(nlp_model, text_content):
    
    doc = nlp_model(text_content)
    extracted_entities = []
    entity_counts = Counter()
    
    target_entity_types = ["PERSON", "GPE", "DATE"]

    for ent in doc.ents:
        if ent.label_ in target_entity_types:
            extracted_entities.append((ent.text, ent.label_))
            entity_counts[ent.label_] += 1
            
    return extracted_entities, entity_counts

def display_results(text_content, extracted_entities, entity_counts):
    
    print("=== Original Text Sample (First 300 chars) ===")
    print(text_content[:300])
    print()

    print("=== Named Entities (PERSON, GPE, DATE) ===")
    for entity_text, entity_type in extracted_entities:
        print(f"{entity_text} ({entity_type})")
    print()
    print("=== Entity Frequency ===")
    for entity_type in ["PERSON", "DATE", "GPE"]:
        print(f"{entity_type}: {entity_counts[entity_type]}")

if __name__ == "__main__":
    file_name = input("Enter text file name: ")
    text_content = load_text_file(file_name)
    nlp = load_ner_model()

    extracted_entities, entity_counts = process_text_for_entities(nlp, text_content)

    display_results(text_content, extracted_entities, entity_counts)
