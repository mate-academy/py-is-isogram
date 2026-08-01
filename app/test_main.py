import pytest


from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True),
    ("  ", True)
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


def test_is_isogram_error_when_word_not_str() -> None:
    with pytest.raises(TypeError):
        is_isogram(11)
