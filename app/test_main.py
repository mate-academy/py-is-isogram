from app.main import is_isogram


def test_checking_all_letters_low() -> None:
    result_of_func = is_isogram("playgrounds")
    assert result_of_func is True


def test_word_contains_same_letters() -> None:
    result_of_func = is_isogram("look")
    assert result_of_func is False


def test_word_with_big_letter_and_same_letters() -> None:
    result_of_func = is_isogram("Adam")
    assert result_of_func is False


def test_empty_string() -> None:
    result_of_func = is_isogram("")
    assert result_of_func is True
