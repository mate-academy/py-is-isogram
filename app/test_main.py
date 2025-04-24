from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word_test, result",
    [
        ("hide", True),
        ("", True),
        ("mOndAy", True),
        ("lOok", False),
        ("territory", False),
        ("amazing", False)
    ]
)
def test_is_isogram(word_test: str, result: bool) -> None:
    assert is_isogram(word_test) == result
