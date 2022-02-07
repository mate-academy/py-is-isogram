import pytest
from app.main import is_isogram


def test_empty_string():
    assert is_isogram("")


@pytest.mark.parametrize(
    "word",
    [
        ("unCopyrIghtAbLe"),
        ("aMbiDextrOuslY"),
        ("plaYGrounDs")
    ]
)
def test_no_repeated_letters(word):
    assert is_isogram(word)


@pytest.mark.parametrize(
    "word",
    [
        ("loOk"),
        ("Adam"),
        ("DOcToRwHO")
    ]
)
def test_with_repeated_letters(word):
    assert not is_isogram(word)


def test_when_word_contains_symbols():
    assert not is_isogram('**8+%+9865)')
    assert is_isogram('*8%+965)')
