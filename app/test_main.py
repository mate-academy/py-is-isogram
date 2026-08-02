import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word_isogram,expected_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Product", True),
        ("CORN", True),
        ("", True),
        ("Adam", False)
    ],
    ids=[
        "isogram in lower case should return True",
        "not isogram should return False",
        "isogram with first upper char should return True",
        "isogram in upper case should return True",
        "empty string should return True",
        "word with same letter in lower/upper cases should return False"
    ]
)
def test_equivalence_classes(
        word_isogram: str,
        expected_result: bool
) -> None:
    assert is_isogram(word_isogram) == expected_result
