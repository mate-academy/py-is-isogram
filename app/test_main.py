from app.main import is_isogram
import pytest


@pytest.mark.parametrize("word, expected_result", [
    ("hello", False),
    ("world", True),
    ("python", True),
    ("IsOgrAm", False),
    ("", True),
    ("aa", False),
    ("12345", True),
])
def test_is_isogram(word: str, expected_result: str) -> str:
    assert is_isogram(word) == expected_result


if __name__ == "__main__":
    pytest.main()
