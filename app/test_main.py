import pytest
import app.main


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("playgrounds", True),
        ("book", False),
        ("Adam", False),
        ("HeLp", True),
        ("isogram", True),
        ("Alphaber", False),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert app.main.is_isogram(word) == expected
