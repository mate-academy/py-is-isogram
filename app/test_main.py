from app.main import is_isogram


def test_should_return_true_if_word_is_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_should_return_false_if_word_not_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_should_return_false_if_word_has_more_then_one_similar_letter() -> None:
    assert is_isogram("look") is False


def test_should_return_true_if_word_is_empy() -> None:
    assert is_isogram("") is True



