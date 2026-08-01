import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("playgrounds", True),
        ("Dermatoglyphics", True),
        ("look", False),
        ("Adam", False),
        ("moOse", False),
        ("Alphabet", False),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    from app.main import is_isogram
    assert is_isogram(word) == expected
