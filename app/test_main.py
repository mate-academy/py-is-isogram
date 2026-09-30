from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_isogram_is_case_insensitive() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("Aa") is False
    assert is_isogram("aA") is False
    assert is_isogram("A") is True


def test_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("look") is False
    assert is_isogram("aa") is False


def test_non_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("alphabet") is False
    assert is_isogram("aba") is False
    assert is_isogram("isograms") is False


def test_valid_isograms() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("backgrounds") is True
    assert is_isogram("subdermatoglyphic") is True
