from app.main import is_isogram

import pytest


@pytest.mark.parametrize("word, expected_result", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True)])
def test_should_return_bool(word: str,
                            expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
