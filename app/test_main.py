from app.main import is_isogram


def test_check_empty_string() -> None:
    assert is_isogram("") is True


def test_not_empty_true_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_check_same_letters_in_word() -> None:
    assert is_isogram("look") is False


def test_check_same_small_and_big_letter() -> None:
    assert is_isogram("Adam") is False
