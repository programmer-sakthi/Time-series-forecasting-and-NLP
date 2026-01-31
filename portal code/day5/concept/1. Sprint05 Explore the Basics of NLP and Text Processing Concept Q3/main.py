# ----------------------------
# Suppress TensorFlow warnings
# ----------------------------
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import spacy
from collections import Counter


def main():
    # Load spaCy English model safely
    try:
        nlp = spacy.load("en_core_web_sm")
    except Exception:
        return

    # Sample input text (customer reviews / article content)
    text = """
    Sonia O'Sullivan has indicated that she would like to participate at the event.
    The runner has trained at her base and has shown improvement at the nationals.
    """

    # Process text
    doc = nlp(text)

    # ----------------------------
    # Token frequency extraction
    # ----------------------------
    freq_counts = Counter()
    for token in doc:
        freq_counts[token.text] += 1

    # ----------------------------
    # 4.1 Frequency of target tokens
    # ----------------------------
    targets = ["the", "at", "has", "."]
    for t in targets:
        print(f"Frequency of '{t}':", freq_counts[t])

    # ----------------------------
    # 4.2 Highest frequency token
    # ----------------------------
    highest = max(targets, key=lambda x: freq_counts[x])
    print("Highest frequency among targets:", highest, "→", freq_counts[highest])


if __name__ == "__main__":
    main()
