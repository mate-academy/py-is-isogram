import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("", True),
        ("look", False),
        ("Adam", False),
        ("playgrounds", True)
    ],
    ids=[
        "empty string is isogram",
        "consecutive repeting letters not isogram",
        "ensitive non consecutive repeating letters not isogram",
        "is isogram"
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
