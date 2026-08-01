from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_is_isogram_with_different_values(
        word: str,
        expected_result: bool
) -> None:
    assert is_isogram(word) == expected_result


def test_is_isogram_expected_error() -> None:
    with pytest.raises(AttributeError):
        assert is_isogram(123)
