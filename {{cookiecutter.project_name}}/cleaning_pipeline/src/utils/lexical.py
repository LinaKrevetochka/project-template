import re

import spacy
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))
nlp = spacy.load('en_core_web_sm')


def standartization(text: str) -> str:
    return text.lower()


def remove_punctuation(text: str) -> str:
    return re.sub(r'[^\w\s]', '', text)


def tokenize_text(text: str) -> list[str]:
    return word_tokenize(text)


def remove_stopwords(tokens: list[str]) -> list[str]:
    return [token for token in tokens if token not in stop_words]


def stemming(tokens: list[str]) -> list[str]:
    """Stemming is the process of reducing the tokens to their root forms.

    For example, the words 'running', 'runs', and 'run' can be stemmed to the root form 'run'.
    Stemming can help group together words that have similar meanings but different forms.

    Returns:
        stemmed tokens.
    """
    return [stemmer.stem(token) for token in tokens]


def lemmatization(tokens: list[str]) -> list[str]:
    """Lemmatization produces valid words that are the base forms of the tokens.

    For example, the word 'better' can be lemmatized to the base form 'good'.
    Lemmatization can also take into account the part-of-speech of the tokens, which can affect their meanings.
    For example, the word 'saw' can be lemmatized to either 'see' or 'saw' depending on whether it is a verb or a noun.

    Returns:
        lemmas of tokens.
    """
    text = ' '.join(tokens)
    doc = nlp(text)
    return [token.lemma_ for token in doc]
