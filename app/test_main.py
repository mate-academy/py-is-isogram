import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("", True),
        ("playgrounds", True),
        ("Playgrounds", True),
        ("look", False),
        ("Adam", False)
    ],
    ids=[
        "empty string is isogram",
        "word that use lowercase and is isogram",
        "word that use uppercase and is isogram",
        "word that use lowercase and not isogram",
        "word that use uppercase and not isogram"
    ]
)
def test_check_word_if_its_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result


def test_program_must_be_case_insensitive() -> None:
    assert is_isogram("Ivan") == is_isogram("ivan")
