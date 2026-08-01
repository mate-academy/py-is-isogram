import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, bool_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),

    ],
    ids=[
        "check for word that have not a repeating letters",
        "check for word that have two repeating letters",
        "check for word that have an upper letter and two repeating letters",
        "check when nothing",
    ]
)
def test_is_isogram_with_different_parameters(word: str,
                                              bool_result: bool) -> None:
    assert is_isogram(word) == bool_result
