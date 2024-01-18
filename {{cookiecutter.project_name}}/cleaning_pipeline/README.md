# Text Cleaning Pipeline

This package provides scripts for text cleaning with two main flows:

## Base Cleaning:

- Remove HTML tags
- Remove URLs
- Remove non-ASCII symbols
- Remove extra space characters (e.g., when there are several spaces in a row)
- Remove spaces at the beginning and end of the text
- Check for long tokens (detect missed spaces due to parsing tools or similar issues)

## Lexical Cleaning:

- Standardize text (transform to lowercase)
- Remove punctuation
- Remove stopwords (e.g., 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', etc.)
- Stemming (reduce inflected words to their word stem, e.g., "programming," "programmer," and "programs" to "program")
- Lemmatization (reduce inflected words to their root form based on intended meaning)

Lexical cleaning is typically necessary for algorithms like TF-IDF.
