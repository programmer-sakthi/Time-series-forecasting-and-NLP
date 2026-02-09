import os
import sys
import warnings

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
warnings.simplefilter(action="ignore")


def main():
    try:
        import spacy
    except ImportError:
        print("spaCy is not installed.")
        return

    filename = input("Enter filename: ").strip()
    file_path = os.path.join(sys.path[0], filename)

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            text = "".join(lines)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        print("spaCy model 'en_core_web_sm' is not installed.")
        return

    # Print first 10 lines EXACTLY (no headings)
    for line in lines[:10]:
        print(line.rstrip())

    doc = nlp(text)

    tokens = [token.text for token in doc]

    # Print first 20 tokens as a single line
    print(" ".join(tokens[:20]))

    # Print total token count
    print(f"Total number of tokens: {len(tokens)}")


if __name__ == "__main__":
    main()
