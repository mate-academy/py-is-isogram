import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "input_word,expected_resume",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("iSogRam", True),
        ("function", False),
        ("string", True)
    ],
)
def test_should_return_equal_resume(
    input_word: int,
    expected_resume: bool
) -> None:
    assert is_isogram(input_word) == expected_resume
