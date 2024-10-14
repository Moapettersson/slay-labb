import wordfreq
import sys
from wordfreq import *
import urllib.request


def main():
    # Defienera argument 3
    n = int(sys.argv[3])
    # Läs in stopwords
    with open(sys.argv[1], encoding="utf-8") as file:
        stopwords = set(file.read().split())
    # Läs in fil eller hemsida
    if "http://" in sys.argv[2] or "https://" in sys.argv[2]:
        response = urllib.request.urlopen(sys.argv[2])
        text = response.read().decode("utf8")
    else:
        with open(sys.argv[2], encoding="utf-8") as file:
            text = file.read()
    # Gör fil eller hemsida till en lång string i en lista
    textlst = []
    textlst.append(text)
    words = tokenize(textlst)
    # Kör countWords med korrekt värde i words och stopWords
    word_counts = countWords(words, stopwords)
    # Kör printTopMost
    printTopMost(word_counts, n)


if __name__ == "__main__":
    main()
