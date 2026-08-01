from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert (is_isogram(word) == result), (
        "'is_isogram' function should return bool type"
    )


@pytest.mark.parametrize(
    "word",
    [
        (23),
        (38.05),
        ({17}),
        ([50]),
    ]
)
def test_rise_error_while_incorrect_arguments(word: any) -> None:
    with pytest.raises(AttributeError):
        is_isogram(word)
