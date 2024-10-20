from app.main import is_isogram
import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("isogram", True),
        ("Python", True),
        ("banana", False),
        ("Dermatoglyphics", True),
    ]
)
def test_is_isogram(word, expected_result):
    assert is_isogram(word) == expected_result
