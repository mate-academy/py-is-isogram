import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "word, extended", [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_is_program(word: str, extended: bool) -> None:
    assert is_isogram(word) == extended
