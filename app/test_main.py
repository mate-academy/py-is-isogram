import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result", [
        ("", True),
        ("playgrounds", True),
        ("sHoulD", True),
        ("bool", False),
        ("tests", False),
        ("Inside", False),
        ("abc45de", True),
        ("by iSograM", True)
    ]
)
def test_is_isogram_words(word: str, result: bool) -> None:
    assert is_isogram(word) == result
