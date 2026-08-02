from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_all_unique_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_repeated_letters() -> None:
    assert is_isogram("look") is False


def test_case_insensitive_check() -> None:
    assert is_isogram("Adam") is False


def test_mixed_case_unique() -> None:
    assert is_isogram("SubDermaToglyphic") is True


def test_single_letter() -> None:
    assert is_isogram("A") is True


def test_two_same_letters_different_case() -> None:
    assert is_isogram("Aa") is False


def test_long_non_isogram() -> None:
    assert is_isogram("Mississippi") is False
