from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_empty_string_with_space() -> None:
    assert is_isogram(" ") is True


def test_one_letter() -> None:
    assert is_isogram("s") is True


def test_two_same_letters_in_different_case() -> None:
    assert is_isogram("Aa") is False


def test_big_true_words() -> None:
    assert is_isogram("Dermatoglyphics") is True


def test_words_with_same_letters() -> None:
    assert is_isogram("pacific") is False
