from app.main import is_isogram


def test_main_empty_line() -> None:
    assert is_isogram("") is True


def test_consecutive_letters_not_an_isogram() -> None:
    assert is_isogram("zxcvasdfZ") is False
