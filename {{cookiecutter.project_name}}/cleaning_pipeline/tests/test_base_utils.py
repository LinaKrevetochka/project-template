from random import choice, randint
from string import ascii_letters, punctuation
from typing import Any, Callable

from hypothesis import given
from hypothesis import strategies as st

from cleaning_pipeline.src.utils.base import (
    MAX_TOKEN_LEN,
    is_text_contains_long_tokens,
    remove_html_tags,
    remove_non_ascii_symbols,
    remove_url,
    shrink_space_characters,
    strip_spaces,
)


@st.composite
def case_for_is_text_contains_long_tokens(draw: Callable[[Any], Any]) -> dict[str, str]:  # noqa: WPS210
    contains_long_tokens = draw(st.booleans())
    if contains_long_tokens:
        min_size = MAX_TOKEN_LEN + 1
        max_size = MAX_TOKEN_LEN + 20
    else:
        min_size = 1
        max_size = MAX_TOKEN_LEN

    base_tokens = draw(
        st.lists(elements=st.text(min_size=min_size, max_size=max_size, alphabet=ascii_letters), min_size=3),
    )
    base_text = base_tokens[0]
    for token in base_tokens[1:]:
        base_text = base_text + choice(f'{punctuation} \t\n\r\f\v') + token  # noqa: S311
    return {'input': base_text, 'expected_output': contains_long_tokens}


@given(test_case=case_for_is_text_contains_long_tokens())
def test_is_text_contains_long_tokens(test_case: dict[str, str]) -> None:
    assert is_text_contains_long_tokens(test_case['input']) == test_case['expected_output']


@st.composite
def case_for_remove_html_tags(draw: Callable[[Any], Any]) -> dict[str, str]:  # noqa: WPS210
    texts = draw(
        st.lists(
            elements=st.text(min_size=1, max_size=10, alphabet=f'{ascii_letters} '),
            min_size=3,
            max_size=3,
        ),
    )

    tag_name = draw(st.text(min_size=1, max_size=5, alphabet=f'{ascii_letters}!-'))
    open_tag = f'<{tag_name}>'
    close_tag = '</{tag_name}>'

    input_text = f'{texts[0]} {open_tag} {texts[1]} {close_tag} {texts[2]}'
    output_text = f'{texts[0]}   {texts[1]}   {texts[2]}'
    return {'input': input_text, 'expected_output': output_text}


@given(test_case=case_for_remove_html_tags())
def test_remove_html_tags(test_case: dict[str, str]) -> None:
    assert remove_html_tags(test_case['input']) == test_case['expected_output']


@st.composite
def case_for_strip_spaces(draw: Callable[[Any], Any]) -> dict[str, str]:
    text = draw(st.text(alphabet=ascii_letters, min_size=1, max_size=50))
    spaces = draw(st.lists(elements=st.text(min_size=1, max_size=10, alphabet=' \t\n\r\f\v'), min_size=2, max_size=2))
    input_text = spaces[0] + text + spaces[1]
    return {'input': input_text, 'expected_output': text}


@given(test_case=case_for_strip_spaces())
def test_strip_spaces(test_case: dict[str, str]) -> None:
    assert strip_spaces(test_case['input']) == test_case['expected_output']


@st.composite
def case_for_shrink_space_characters(draw: Callable[[Any], Any]) -> dict[str, str]:
    words = draw(
        st.lists(elements=st.text(min_size=5, max_size=10, alphabet=ascii_letters), min_size=2, max_size=5),
    )

    def generate_newlines_and_spaces() -> str:
        return draw(st.text(alphabet=' \t\n\r\f\v', min_size=2, max_size=5))

    input_text = ''.join(word + generate_newlines_and_spaces() for word in words[:-1])
    input_text = input_text + words[-1]
    output_text = ' '.join(words)
    return {'input': input_text, 'expected_output': output_text}


@given(test_case=case_for_shrink_space_characters())
def test_shrink_space_characters(test_case: dict[str, str]) -> None:
    assert shrink_space_characters(test_case['input']) == test_case['expected_output']


@st.composite
def case_for_remove_non_ascii_symbols(draw: Callable[[Any], Any]) -> dict[str, str]:
    words = draw(
        st.lists(elements=st.text(min_size=5, max_size=10, alphabet=ascii_letters), min_size=2, max_size=5),
    )

    def generate_non_ascii_symbol() -> str:
        return chr(randint(128, 255))

    input_text = ''.join(word + generate_non_ascii_symbol() for word in words[:-1])
    input_text = input_text + words[-1]
    output_text = ' '.join(words)
    return {'input': input_text, 'expected_output': output_text}


@given(test_case=case_for_remove_non_ascii_symbols())
def test_remove_non_ascii_symbols(test_case: dict[str, str]) -> None:
    assert remove_non_ascii_symbols(test_case['input']) == test_case['expected_output']


@st.composite
def case_for_remove_url(draw: Callable[[Any], Any]) -> dict[str, str]:
    host = draw(st.text(min_size=5, max_size=10, alphabet=ascii_letters))
    protocol = draw(st.sampled_from(['http://', 'https://']))

    texts = draw(st.lists(elements=st.text(min_size=0, max_size=20), min_size=2, max_size=2))
    input_text = ' '.join([texts[0], protocol + host, texts[1]])
    output_text = ' '.join([texts[0], ' ', texts[1]])
    return {'input': input_text, 'expected_output': output_text}


@given(test_case=case_for_remove_url())
def test_remove_url(test_case: dict[str, str]) -> None:
    assert remove_url(test_case['input']) == test_case['expected_output']
