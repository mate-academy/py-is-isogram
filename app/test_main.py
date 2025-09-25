import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("isogram", True),
        ("Alphabet", False),  # A повторюється
        ("Dermatoglyphics", True),
        ("moOse", False),  # o повторюється (регістр не важливий)
        ("Python", True),
        ("Letter", False),
    ]
)
def test_is_isogram_cases(word: str, expected: bool) -> None:
    result = is_isogram(word)
    assert result == expected
    assert isinstance(result, bool)