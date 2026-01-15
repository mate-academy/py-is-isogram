import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,bool_value",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_should_return_correct_boolean_value(
        word: str, bool_value: bool
) -> None:
    assert (is_isogram(word) is bool_value
            ), f"should return {bool_value} when 'word' is {word}"
