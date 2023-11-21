from app.main import is_isogram
import pytest


def test_should_raise_atributeerror() -> None:
    with pytest.raises(AttributeError):
        is_isogram(11)


@pytest.mark.parametrize(
    "word,expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("11", False)
    ]
)
def test_should_return_expected(
        word: str,
        expected: bool
) -> None:
    assert is_isogram(word) == expected
