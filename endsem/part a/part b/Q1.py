import os
import sys
import warnings

# Suppress TensorFlow and other warnings
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
warnings.simplefilter(action="ignore")


def main():
    try:
        import spacy
    except ImportError:
        print("spaCy is not installed.")
        return

    filename = input("Enter filename: ")
    file_path = os.path.join(sys.path[0], filename)

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        print("spaCy model 'en_core_web_sm' is not installed.")
        return

    # Customize stop words
    stop_words = nlp.Defaults.stop_words

    add_words = {"officially", "announced", "present", "run"}
    for word in add_words:
        stop_words.add(word)
        nlp.vocab[word].is_stop = True

    remove_words = {"hence", "every", "he"}
    for word in remove_words:
        if word in stop_words:
            stop_words.remove(word)
        nlp.vocab[word].is_stop = False

    doc = nlp(text)

    filtered_tokens = [
        token.lemma_.lower()
        for token in doc
        if not token.is_stop
        and not token.is_punct
        and not token.is_space
        and token.is_alpha
    ]

    print("Filtered Tokens (First 20):")
    print(filtered_tokens[:20])
    print()

    print("Cleaned Text Sample:")
    cleaned_text = " ".join(filtered_tokens)
    print(cleaned_text[:200])


if __name__ == "__main__":
    main()
