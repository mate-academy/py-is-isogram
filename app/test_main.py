import pytest
from typing import Type
from app.main import is_isogram


@pytest.mark.parametrize(
    "words,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_should_return_correct_data(
        words: str,
        result: bool
) -> None:
    assert is_isogram(words) == result


@pytest.mark.parametrize(
    "words,expected_error",
    [
        (42, AttributeError),
        ([23, "45"], AttributeError),
        ({"word": ""}, AttributeError),
        ({4, 5}, AttributeError)
    ]
)
def test_raising_errors(
        words: str,
        expected_error: Type[BaseException]
) -> None:
    with pytest.raises(expected_error):
        is_isogram(words)
