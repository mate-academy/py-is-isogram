from app.main import is_isogram


def test_empty_parameter() -> None:
    assert (is_isogram("") == True)


def test_one_letter_parameter() -> None:
    assert (is_isogram("e") == True)


def test_one_word_parameter_no_same_letters() -> None:
    assert (is_isogram("practise") == True)


def test_one_word_with_same_upper_and_lower_letter() -> None:
    assert (is_isogram("Grog") == False)


def test_one_word_equal_to_bool() -> None:
    assert (is_isogram("False") == True)


def test_one_big_sentence() -> None:
    assert (is_isogram("hat takes a string word, "
                       "that contains only letters, "
                       "and checks whether this word "
                       "is an isogram.") == False)
