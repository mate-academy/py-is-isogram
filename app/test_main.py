import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds" is True),
        ("Playground" is True),
        ("look" is False),
        ("Adam" is False),
        ("" is True)
    ]
)
def is_isogram(
        word: str,
        expected: bool
) -> None:
    result = is_isogram(word)
    assert result == expected
