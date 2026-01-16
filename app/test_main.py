from app.main import is_isogram


def test_should_be_case_insensitive() -> None:
    assert not is_isogram("lOok")


def test_should_return_true_for_empty_string() -> None:
    assert is_isogram("")


# def test_should_handle_leading_and_trailing_spaces() -> None:
#     assert is_isogram("playgrounds  ") == True


def test_should_correctly_identify_isograms_and_non_isograms() -> None:
    assert is_isogram("playground")


def test_words_with_repeated_letters_non_consecutive() -> None:
    assert not is_isogram("Adam")
