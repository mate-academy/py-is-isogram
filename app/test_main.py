from app.main import is_isogram


def test_check_empty_str() -> None:
    assert is_isogram("") is True


def test_check_1_space() -> None:
    assert is_isogram(" ") is True


def test_should_return_false_if_spaces() -> None:
    assert is_isogram("    ") is False


def test_check_when_number_is_string() -> None:
    assert is_isogram("12345") is True


def test_should_return_false_if_numbers_repeat() -> None:
    assert is_isogram("12233") is False


def test_check_isogram_word() -> None:
    assert is_isogram("playgrounds") is True


def test_check_big_letters() -> None:
    assert is_isogram("ABCD") is True


def test_check_non_isogram_word_with_big_letter() -> None:
    assert is_isogram("Adam") is False


def test_should_return_false_string_has_non_consecutive_letters() -> None:
    assert is_isogram("asdfghjkla") is False


def test_should_return_false_string_has_consecutive_letters() -> None:
    assert is_isogram("aaabcd") is False
