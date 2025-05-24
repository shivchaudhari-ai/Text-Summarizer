import nltk
import re
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def summarize(text, max_sentences=3):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalnum() and word not in stop_words]

    freq = Counter(words)

    sentences = sent_tokenize(text)
    sentence_scores = {}

    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in freq:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + freq[word]

    summarized = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:max_sentences]
    return " ".join(summarized)

if __name__ == "__main__":
    with open("sample.txt", "r", encoding="utf-8") as file:
        content = file.read()

    result = summarize(content)
    print("\n--- Summary ---\n")
    print(result)
