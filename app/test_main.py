from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_simple_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_repeated_letters() -> None:
    assert is_isogram("look") is False


def test_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_single_letter() -> None:
    assert is_isogram("a") is True


def test_unique_letters_word() -> None:
    assert is_isogram("lamp") is True


def test_non_consecutive_repeat() -> None:
    assert is_isogram("alphabet") is False


def test_uppercase_word() -> None:
    assert is_isogram("DOG") is True


def test_mixed_case_repeat() -> None:
    assert is_isogram("moOse") is False


def test_long_isogram() -> None:
    assert is_isogram("subdermatoglyphic") is True
