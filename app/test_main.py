from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_single_word_is_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_word_with_repeating_letters() -> None:
    assert is_isogram("look") is False


def test_case_insensitivity() -> None:
    assert is_isogram("Adam") is False


def test_mixed_case_isogram() -> None:
    assert is_isogram("Dermatoglyphics") is True
