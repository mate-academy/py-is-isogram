from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_isogram_word() -> None:
    assert is_isogram("playgrounds") is True


def test_non_isogram_word() -> None:
    assert is_isogram("look") is False


def test_case_insensitivity() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("madam") is False
    assert is_isogram("MaDam") is False
