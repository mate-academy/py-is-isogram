import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
)
def test_is_isogram_cases(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected


def test_is_isogram_should_raise_for_invalid_type() -> None:
    with pytest.raises(TypeError):
        is_isogram(2)
