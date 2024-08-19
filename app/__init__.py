from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word_test, expected", [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ])
def test_is_isogram(word_test: str,
                    expected: bool) -> None:
    assert is_isogram(word_test) == expected
