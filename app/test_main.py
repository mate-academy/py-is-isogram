from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_isogram_word() -> None:
    assert is_isogram("playgrounds") is True


def test_non_isogram_word() -> None:
    assert is_isogram("look") is False


def test_case_insensitivity() -> None:
    assert is_isogram("Adam") is False


def test_long_isogram() -> None:
    assert is_isogram("Dermatoglyphics") is True


def test_single_character() -> None:
    assert is_isogram("a") is True


def test_repeated_letters() -> None:
    assert is_isogram("banana") is False
