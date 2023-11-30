from app.main import is_isogram


def test_should_return_true_if_no_repeating_letters() -> None:
    assert is_isogram("playgrounds")


def test_should_return_true_if_empty() -> None:
    assert is_isogram("")


def test_should_return_equal_result_if_case_insensitive() -> None:
    assert is_isogram("playgrounds") == is_isogram("PlaYgRouNds")


def test_should_return_false_if_double_repeating_letters() -> None:
    assert is_isogram("book") == False


def test_should_return_false_if_repeating_letters_at_the_begin_and_end_word() -> None:
    assert is_isogram("fimhrdlf") == False


def test_should_return_false_if_double_repeating_letters_different_case() -> None:
    assert is_isogram("Adam") == False
