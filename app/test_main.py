from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,expected",
    [
        ("wow", False),
        ("wo", True),
        ("", True),
        ("playground", True),
        ("look", False),
        ("Adam", False)

    ]
)
def test_is_iso_should_return_correct_bool(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
