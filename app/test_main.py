from app.main import is_isogram


def test_is_isogram_str() -> None:
    word_lower = is_isogram(word="playgrounds")
    isinstance(word_lower, str)


def test_is_isogram() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("look") is False
    assert is_isogram("Adam") is False
    assert is_isogram("") is True
    assert is_isogram("Star") is True
    assert is_isogram("thumbscrew-japingly") is False
    assert is_isogram("moOse") is False
    assert is_isogram("aba") is False
