import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,bool_expected_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ]
)
def test_is_isogram(word: str, bool_expected_result: bool) -> None:
    assert is_isogram(word) == bool_expected_result
