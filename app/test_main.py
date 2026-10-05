from app.main import is_isogram


def test_is_isogram_returns_true_for_isogram() -> None:
    assert is_isogram("isogram") is True


def test_is_isogram_returns_false_for_non_isogram() -> None:
    assert is_isogram("hello") is False


def test_is_isogram_returns_true_for_empty_string() -> None:
    assert is_isogram("") is True


def test_is_isogram_lowercase_and_uppercase() -> None:
    assert is_isogram("Dermatoglyphics") is True
    assert is_isogram("aba") is False
    assert is_isogram("moOse") is False
