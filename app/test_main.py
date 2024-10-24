import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param(
            "",
            True,
            id="should return True if empty string"
        ),
        pytest.param(
            "return",
            False,
            id="should return False if word have repeating letters"
        ),
        pytest.param(
            "look",
            False,
            id="return False if repeating letters"
        ),
        pytest.param(
            "read",
            True,
            id="should True if no repeating letters"
        ),
    ]
)
def test_modify_is_isogram_correctly(word: str, result: bool) -> None:
    assert is_isogram(word) == result


def test_isogram_is_case_insensitive() -> None:
    assert is_isogram("MeSsI") == is_isogram("meSSI")
