from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected", [
        pytest.param("playgrounds", True,
                     id="valid_isogram"),
        pytest.param("look", False,
                     id="repeated_letter"),
        pytest.param("Adam", False,
                     id="valid_isogram_case_insensitive"),
        pytest.param("", True,
                     id="empty_string")
    ]
)
def test_isogram_word(
        word: int, expected: bool
) -> None:
    assert is_isogram(word) == expected
