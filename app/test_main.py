from app.main import is_isogram


def test_should_return_true_when_word_is_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_when_word_with_lower_letters_and_is_not_isogram() -> None:
    assert is_isogram("look") is False


def test__when_one_letter_is_lower_and_another_is_upper() -> None:
    assert is_isogram("Adam") is False


def test_with_empty_word() -> None:
    assert is_isogram("") is True
