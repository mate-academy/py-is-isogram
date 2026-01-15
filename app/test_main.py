import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word",
    [
        "",
        "a",
        "subdermatoglyphic",
        "SubDermatoglyphic",
        "uncopyrightable",
        "Dermatoglyphics",
    ],
)
def test_detects_isograms(word: str) -> None:
    assert is_isogram(word)


@pytest.mark.parametrize(
    "word",
    [
        "look",
        "letter",
        "alphabet",
        "Adam",
        "Moon",
        "noon",
        "aa",
        "Aa",
        "Mississippi",
    ],
)
def test_detects_non_isograms(word: str) -> None:
    assert not is_isogram(word)
