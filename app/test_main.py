from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("  ", False)
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result


@pytest.mark.parametrize(
    "word, expected_error",
    [
        (12, TypeError),
        ([12], TypeError),
        (12.546, TypeError)
    ]
)
def test_is_isogram_for_error(
        word: str,
        expected_error: Exception
) -> None:
    with pytest.raises(Exception):
        is_isogram(word)
