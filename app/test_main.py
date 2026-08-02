import pytest

from app.main import is_isogram


def test_should_return_bool() -> None:
    goals = is_isogram("f")
    assert isinstance(goals, bool)


@pytest.mark.parametrize(
    "word, result, test_id",
    [
        ("playgrounds", True,
         "playgrounds should return True"),
        ("look", False,
         "look should return False"),
        ("Adam", False,
         "Function should be case-insensitive"
         "(M and m are considered the same letter)"),
        ("", True,
         "The empty string is an isogram")
    ],
)
def test_errors_for_type_values(
        word: str,
        result: bool,
        test_id: str
) -> None:
    assert is_isogram(word) == result
