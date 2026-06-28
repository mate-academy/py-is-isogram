from app.main import is_isogram
import pytest


@pytest.mark.parametrize("word, expected_result", [
    ("playgrounds", True),
    ("", True),
    (" ", True),
    ("look", False),
    ("Adam", False),
    ("Aa", False),
    ("ADAM", False),


])
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result


def test_is_isogram_with_diff_types() -> None:
    with pytest.raises(AttributeError):
        assert is_isogram(12) is False

    with pytest.raises(AssertionError):
        assert is_isogram(".,/!@#$%^&*(") is False
