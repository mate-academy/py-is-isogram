import pytest

from app.main import is_isogram


def test_is_instance_is_isogram() -> None:
    assert isinstance(is_isogram("asd"), bool)


@pytest.mark.parametrize(
    "word,expected",
    [
        ("isogram", True),
        ("playgrounds", True),
        ("Adam", False),
        (" ", True),
        ("121", False),
        ("123", True),
        ("look", False)
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


def test_wrong_input_case() -> None:
    with pytest.raises(AttributeError):
        is_isogram(14)
