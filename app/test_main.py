import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("look", False),
        ("oclock", False),
        ("unlock", True),
        ("promO", False)
    ]
)
def test_func_should_return_correct_result(
        word: str,
        expected: bool
) -> None:
    assert is_isogram(word) == expected


def test_should_raise_coorrect_error_when_incorrect_input() -> None:
    with pytest.raises(AttributeError):
        is_isogram(3)
