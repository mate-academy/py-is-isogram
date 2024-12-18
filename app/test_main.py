import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("", True),
        ("playground", True),
        ("look", False),
        ("TyPpe", False),
        ("batman", False)
    ],
    ids=[
        "returns True if word is an empty string",
        "returns True if word is isogram",
        "returns False if word has repeating letters",
        "function should be case-sensitive",
        "returns False if word has non consecutive repeating letters"
    ]
)
def test_if_func_returns_correct_result(
        word: str,
        expected_result: bool
) -> None:
    assert is_isogram(word) == expected_result
