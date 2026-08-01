import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_get_human_age(word: str, result: bool) -> None:
    assert (
        is_isogram(word) == result
    ), f"{word} is calculated badly."
