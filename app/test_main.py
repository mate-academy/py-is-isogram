import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    ("word", "expected"),
    [
        ("playgrounds", True),
        ("table", True),
        ("wood", False),
        ("telephone", False),
        ("dermatoglyphics", True),
        ("polymer", True),
        ("", True),
        ("Alphabet", False)
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
