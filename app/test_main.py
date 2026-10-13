import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("look", False),
        ("playground", True),
        ("Adam", False),
        ("", True),
    ],
)
def test_should_return_correct_result_for_word(
    word: str,
    expected: bool,
) -> None:
    assert is_isogram(word) is expected
