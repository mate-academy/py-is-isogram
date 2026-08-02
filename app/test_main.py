import pytest

from app.main import is_isogram


test_cases = [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True)
]


@pytest.mark.parametrize("word, excpected_result", test_cases)
def test_is_isogram(word: str,
                    excpected_result: bool
                    ) -> None:
    assert is_isogram(word) == excpected_result
