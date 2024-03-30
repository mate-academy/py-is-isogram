import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "initial_word, expected_result",
    [
        ("", True),
        ("Hello", False),
        ("HeLlo", False),
        ("HELLO", False),
        ("playgrounds", True),
        ("MAIN", True),
        ("Jakj", False)
    ]
)
def test_check_is_isogram(
        initial_word: str,
        expected_result: bool
) -> None:
    assert is_isogram(initial_word) == expected_result
