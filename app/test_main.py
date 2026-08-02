from app.main import is_isogram


def test_word_is_empty_string() -> None:
    assert is_isogram("") is True


def test_correct_lower_case_word() -> None:
    assert is_isogram("playgrounds") is True


def test_correct_upper_case_word() -> None:
    assert is_isogram("Playgrounds") is True


def test_incorrect_lower_case_word() -> None:
    assert is_isogram("look") is False


def test_incorrect_upper_case_word() -> None:
    assert is_isogram("Adam") is False
