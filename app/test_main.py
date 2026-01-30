import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("background", True),
        ("a", True),
        ("", True),
        ("look", False),
        ("subdermatoglyphic", True),
        ("subdermatoglyphics", False),
        ("six-year-old", False),
        ("Adam", False),
        ("WeiRder", False),
        ("WEIRD", True)
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert (
        is_isogram(word) == result
    ), f"Failed: word: {word}"
