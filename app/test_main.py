import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("Playground", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_is_isogram(
        word: str,
        expected: bool
) -> None:
    result = is_isogram(word)
    assert result == expected
