from app.main import is_isogram
import pytest


@pytest.mark.parametrize(

    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("M", True)])
def test_normal_types(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
