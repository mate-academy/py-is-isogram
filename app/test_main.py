import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("Adam", False),
        ("", True),
        ("look", False)
    ],
    ids=[
        "Should return True",
        "Should return False",
        "If word is empty, should return True",
        "Should return False"
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result


@pytest.mark.parametrize(
    "word",
    [
        ["Play"],
        {"Play"},
        {"Play": 1},
        ("play", "look")
    ]
)
def test_raise_error_correctly(word: str) -> None:
    with pytest.raises(AttributeError):
        is_isogram(word), (
            "Should return TypeError, if function receives not string"
        )
