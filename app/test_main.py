import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "string_word,expected_answer",
    [
        pytest.param("playgrounds", True,
                     id="\'playgrounds\' is isogram"),
        pytest.param("look", False,
                     id="\'look\' is not isogram (duplicated letters)"),
        pytest.param("Adam", False,
                     id="\'Adam\' is not isogram (case-insensitive behavior)"),
        pytest.param("", True,
                     id="the empty string is an isogram")
    ]
)
def test_is_isogram(string_word: str,
                    expected_answer: list) -> None:
    assert expected_answer == is_isogram(string_word)
