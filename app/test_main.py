import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "testing_word,boolean_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("ILOVEU", True)
    ]
)
def test_return_correct_result(
    testing_word: str,
    boolean_result: bool
) -> None:
    assert is_isogram(testing_word) == boolean_result
