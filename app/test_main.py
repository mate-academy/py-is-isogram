import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "initial_word,expected_bool",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ],
    ids=[
        "word is isogram",
        "word is not isogram",
        "contain same symbols in dif register",
        "word is empty"
    ]
)
def test_should_check_if_word_is_isogram(
        initial_word: str,
        expected_bool: bool
) -> None:
    assert (is_isogram(initial_word) == expected_bool), \
        "Should correctly check if word is isogram"
