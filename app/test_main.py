import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("PlAygrOundS", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
    ids=[
        "test isogram lowercase",
        "test isogram with mixed case",
        "test not isogram lowercase",
        "test not isogram mixed case",
        "temp empty string"
    ]
)
def test_can_sum(word: str, result: list[int]) -> None:
    assert (is_isogram(word) == result),\
        f"Result of func for word={word} and should be equal to {result}"


def test_raise_typeerror_if_not_integer() -> None:
    with pytest.raises(AttributeError):
        is_isogram([12, 17, 55])
