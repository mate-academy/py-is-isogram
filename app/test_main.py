import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result", [
        ("playgrounds", True),
        ("Listen", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_should_return_is_isogram(word, expected_result):
    assert is_isogram(word) == expected_result
