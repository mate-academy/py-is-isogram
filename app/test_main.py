from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_same_letters_same_case() -> None:
    assert is_isogram("wood") is False


def test_same_letters_different_case() -> None:
    assert is_isogram("Adam") is False


def test_no_repeated_letters_same_case() -> None:
    assert is_isogram("mate") is True


def test_no_repeated_letters_different_case() -> None:
    assert is_isogram("Mate") is True
