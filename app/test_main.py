import pytest

from app import main


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param("", True, id="empty string is an isogram"),
        pytest.param("a", True, id="single letter is an isogram"),
        pytest.param("playgrounds", True, id="word without repeats"),
        pytest.param("Dermatoglyphics", True, id="long isogram with capital"),
        pytest.param("look", False, id="consecutive repeated letters"),
        pytest.param("letter", False, id="non-consecutive repeated letters"),
        pytest.param("aa", False, id="two identical letters"),
    ],
)
def test_is_isogram_basic_cases(word: str, expected: bool) -> None:
    assert main.is_isogram(word) is expected


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param("Adam", False, id="same letter in different case"),
        pytest.param("aA", False, id="lower and upper of same letter"),
        pytest.param("MOM", False, id="all uppercase with repeat"),
        pytest.param("PLAYGROUNDS", True, id="all uppercase isogram"),
        pytest.param("PlAyGrOuNdS", True, id="mixed case isogram"),
    ],
)
def test_is_isogram_is_case_insensitive(word: str, expected: bool) -> None:
    assert main.is_isogram(word) is expected
