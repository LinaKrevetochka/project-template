from cleaning_pipeline.src.utils.base import (
    is_text_contains_long_tokens,
    remove_html_tags,
    remove_non_ascii_symbols,
    remove_url,
    shrink_space_characters,
    strip_spaces,
)


def apply_base_cleaning(text: str) -> str:
    text = remove_html_tags(text)
    text = remove_url(text)
    text = remove_non_ascii_symbols(text)
    text = shrink_space_characters(text)
    text = strip_spaces(text)
    return '' if is_text_contains_long_tokens(text) else text
