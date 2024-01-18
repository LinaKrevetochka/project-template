from cleaning_pipeline.src.utils.lexical import (
    lemmatization,
    remove_punctuation,
    remove_stopwords,
    standartization,
    stemming,
    tokenize_text,
)


def apply_lexical_cleaning(text: str) -> str:
    text = standartization(text)
    text = remove_punctuation(text)
    tokens = tokenize_text(text)
    tokens = remove_stopwords(tokens)
    tokens = stemming(tokens)
    tokens = lemmatization(tokens)
    return ' '.join(tokens)
