from app.main import is_isogram


def test_isogram_simple_true() -> None:
    assert is_isogram("playgrounds") is True


def test_isogram_simple_false() -> None:
    assert is_isogram("look") is False


def test_isogram_case_insensitive_false() -> None:
    assert is_isogram("Adam") is False


def test_isogram_empty_string() -> None:
    assert is_isogram("") is True


def test_isogram_single_letter() -> None:
    assert is_isogram("a") is True


def test_isogram_mixed_case_true() -> None:
    assert is_isogram("Dermatoglyphics") is True


def test_isogram_repeated_letters_mixed_case() -> None:
    assert is_isogram("Aa") is False


def test_isogram_all_unique_short() -> None:
    assert is_isogram("abc") is True


def test_isogram_repeated_non_consecutive() -> None:
    assert is_isogram("aba") is False
