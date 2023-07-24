import pytest
from app.main import is_isogram


def test_an_array() -> bool:
    assert type(is_isogram("wer")) == bool


def test_empty_array() -> bool:
    assert is_isogram("") is True


def test_different_cases_array() -> bool:
    assert is_isogram("Vv") is False


def test_different_cases_array1() -> bool:
    assert is_isogram("343") is False


@pytest.mark.parametrize(
    "word, expected",
    [
        ("fgh", True),
        ("ddff", False),
        ("fgds", True),
        ("ghhyyy", False),

    ],
    ids=[
        "test_word_fgh",
        "test_word_ddff",
        "test_word_fgds",
        "test_word_ghhyyy",

    ]
)
def test_main_get(word: str, expected: bool) -> bool:
    result = is_isogram(word)
    assert result == expected
