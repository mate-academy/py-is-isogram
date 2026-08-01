import pytest

from app.main import is_isogram


cases = [
    ("a", True),
    ("helo", True),
    ("asdghjl", True),
    ("ASDFGHJKL", True),
    ("main", True),
    ("ex", True),
    ("", True),
    ("playgrounds", True),
    ("Aa", False),
    ("aa", False),
    ("look", False),
    ("Adam", False),
    ("txt", False),
    ("test", False),
    ("TesT", False),
    ("readme", False),
    ("MAMA", False),
]


@pytest.mark.parametrize(
    "word,correct_result",
    cases,
    ids=[
        f"{word} {'is' if res else 'is not'} an isogram"
        for word, res in cases
    ]
)
def test_is_isogram_returns_correct_result(
        word: str,
        correct_result: bool
) -> None:
    assert is_isogram(word) == correct_result
