# ----------------------------
# Suppress TensorFlow warnings
# ----------------------------
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import spacy
from collections import Counter


def main():
    # Load spaCy model safely
    try:
        nlp = spacy.load("en_core_web_sm")
    except Exception:
        return

    # Input text
    text = """
    News Article 2

    O'Sullivan could run in Worlds

    Sonia O'Sullivan has indicated that she would like to participate in next month's World Cross Country Championships in St Etienne.

    Athletics Ireland have hinted that the 35-year-old Cobh runner may be included in the official line-up for the event in France on 19-20 March. Provincial teams were selected after last Saturday's Nationals in Santry and will be officially announced this week. O'Sullivan is at present preparing for the London marathon on 17 April. The participation of O'Sullivan, currentily training at her base in Australia, would boost the Ireland team who won the bronze three years agio. The first three at Santry last Saturday, Jolene Byrne, Maria McCambridge and Fionnualla Britton, are automatic selections and will most likely form part of the long-course team. O'Sullivan will also take part in the Bupa Great Ireland Run on 9 April in Dublin.
    """

    # Process text
    doc = nlp(text)

    # ----------------------------
    # 3.1 Word frequency count
    # ----------------------------
    freq_counts = Counter()
    for token in doc:
        freq_counts[token.text] += 1

    # ----------------------------
    # 3.2 Top 10 most common tokens
    # ----------------------------
    print("Top 10 most common tokens:")
    for token, count in freq_counts.most_common(10):
        print(token, ":", count)

    # ----------------------------
    # 3.3 Frequency of specific words
    # ----------------------------
    print("Frequency of 'Claxton':", freq_counts["Claxton"])
    print("Frequency of 'medal':", freq_counts["medal"])


if __name__ == "__main__":
    main()
