import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_result",
    [
        ("", True),
        ("wash", True),
        ("see", False),
        ("COMPUTER", True),
        ("SCISSORS", False),
        ("plEase", False)
    ]
)
def test_should_return_correct_result(
        word: str,
        expected_result: bool
) -> None:
    assert is_isogram(word) == expected_result


def test_should_raise_errors_correctly() -> None:
    with pytest.raises(AttributeError):
        is_isogram(12345)
