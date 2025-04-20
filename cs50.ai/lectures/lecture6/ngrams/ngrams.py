from collections import Counter

import math
import nltk
import os
import sys

def main():
    """Calc top term freq for a corpus of docs"""

    if len(sys.argv) != 3:
        sys.exit("usage: python ngrams.py n corpus")
    print("Loading Data ...")

    n = int(sys.argv[1])
    corpus = load_data(sys.argv[2])


    ngrams = Counter(nltk.ngrams(corpus, n))

    for ngram, freq in ngrams.most_common(10):
        print(f"{freq}: {ngram}")


def load_data(directory):
    contents = []

    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename)) as f:
            contents.extend([
                word.lower() for word in nltk.word_tokenize(f.read())
                if any(c.isalpha() for c in word)
            ])

if __name__ == "__main__":
    main()