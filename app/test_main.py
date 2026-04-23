from app.main import is_isogram


def test_no_repeating_letters() -> None:
    assert is_isogram("nightmare") == True


def test_repeating_letters() -> None:
    assert is_isogram("boss") == False


def test_no_letters() -> None:
    assert is_isogram("") == True


def test_consecutive_word() -> None:
    assert is_isogram("SOS") == False


def test_lower_and_upper_case() -> None:
    assert is_isogram("preSs") == False
