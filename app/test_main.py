from app.main import is_isogram


def test_should_return_true_during_checking() -> None:
    assert is_isogram(word="playgrounds")


def test_return_false_if_in_word_exist_same_upper_and_lower_letter() -> None:
    assert not is_isogram(word="Adam")


def test_return_false_if_in_word_exist_same_letters() -> None:
    assert not is_isogram(word="look")


def test_should_return_true_if_empty_string() -> None:
    assert is_isogram(word="")
