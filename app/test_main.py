import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("playground", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ],
    ids=[
        "playgrounds is isogram",
        "look is not an isogram, it has repeating letters",
        "Adam is not an isogram, it has repeating letters",
        "'' is isogram"
    ]
)
def test_is_correct_for_different_cents_given(
        word: str,
        result: bool
) -> None:
    assert (
        is_isogram(word) == result
    ), f"'{word}' result should be equal to {result}"
