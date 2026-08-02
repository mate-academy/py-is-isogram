from app.main import is_isogram


def test_false_in_different_registers() -> None:
    word = "Adam"
    assert is_isogram(word) is False


def test_false_in_same_registers() -> None:
    word = "look"
    assert is_isogram(word) is False


def test_true_if_word_is_empty() -> None:
    word = ""
    assert is_isogram(word) is True
