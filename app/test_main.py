from app.main import is_isogram


def test_isogram_true() -> None:
    assert is_isogram("playgrounds") is True


def test_isogram_false_consecutive() -> None:
    assert is_isogram("look") is False


def test_isogram_false_non_consecutive() -> None:
    assert is_isogram("Adam") is False


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_isogram_mixed_case() -> None:
    assert is_isogram("Dermatoglyphics") is True


def test_single_character_string() -> None:
    assert is_isogram("A") is True


def test_repeating_letters_different_cases() -> None:
    assert is_isogram("Alphabet") is False
