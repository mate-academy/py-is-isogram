from app.main import is_isogram
import pytest


@pytest.mark.parametrize("word, expected_boolean", [
    ("Forest", True),
    ("soUnd", True),
    ("", True),
    ("weather", False),
    ("apPle", False)
])
def test_is_isogram_function(
        word: str, expected_boolean: bool
) -> None:
    assert is_isogram(word) == expected_boolean
