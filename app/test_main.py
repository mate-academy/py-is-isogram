from app.main import is_isogram


def test_get_true_if_not_the_same_latters() -> None:
    assert is_isogram("playgrounds") is True


def test_get_false_if_word_have_the_same_latters() -> None:
    assert is_isogram("look") is False


def test_get_false_if_word_have_the_same_upper_latter() -> None:
    assert is_isogram("Adam") is False


def test_get_true_if_empty_string() -> None:
    assert is_isogram("") is True
