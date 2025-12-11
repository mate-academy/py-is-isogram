import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("a", True),
        ("", True)
    ]
)
def test_expected_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
