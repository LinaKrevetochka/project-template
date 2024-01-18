import re
import string

from spacy.lang.tokenizer_exceptions import URL_PATTERN

MAX_TOKEN_LEN = 30

spacy_url_regex = re.compile(URL_PATTERN)
url_regex = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

html_tags_regex = re.compile('<[^<>]*>')


def remove_url(text: str) -> str:
    text = spacy_url_regex.sub(' ', text)
    return url_regex.sub(' ', text)


def strip_spaces(text: str) -> str:
    return text.strip()


def shrink_space_characters(text: str) -> str:
    return re.sub(r'\s\s+', ' ', text)


def remove_html_tags(text: str) -> str:
    return html_tags_regex.sub(' ', text)


def is_text_contains_long_tokens(text: str) -> bool:
    """Can be changed to remove long tokens from text.

    In the current version, the main idea is to check if the text contains long tokens
    and remove the entire text if it does.

    Returns:
        True if text contais long tokens, False otherwise.
    """
    tokens = re.findall(rf'[^{string.punctuation}\s]+', text)
    return any(len(token) > MAX_TOKEN_LEN for token in tokens)


def remove_non_ascii_symbols(text: str) -> str:
    return re.sub(r'[^\x00-\x7f]', ' ', text)
