import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param("", True, id="empty sting"),
        pytest.param("AAA", False, id="consecutive letters"),
        pytest.param("playgrounds", True, id="lower string"),
        pytest.param("Adam", False, id="case sensitive test")
    ]
)
def test_is_isogram_input(word: str, expected: bool) -> bool:
    assert is_isogram(word) == expected


def test_raise_error_if_not_str() -> None:
    with pytest.raises(AttributeError):
        assert is_isogram(100)
