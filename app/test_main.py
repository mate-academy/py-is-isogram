import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected", [
        pytest.param("", True, id="empty_str_is_isogram"),
        pytest.param("Adam", False, id="repeating_letter_ignore_case"),
        pytest.param("look", False, id="repeating_letters"),
        pytest.param("playgrounds", True, id="is_isogram")
    ]
)
def test_is_isogram(

        word: str,
        expected: bool

) -> None:

    assert is_isogram(word) == expected
