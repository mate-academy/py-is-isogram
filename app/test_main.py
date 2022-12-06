from app.main import is_isogram


def test_should_return_true_when_word_is_empty() -> None:
    assert is_isogram('') is True


def test_should_return_false_when_word_with_repeat_but_different_case() -> None:
    assert is_isogram('Anya') is False


def test_should_return_true_when_word_is_long_without_repeats() -> None:
    assert is_isogram('playgrounds') is True


def test_should_return_false_when_letters_are_consecutive() -> None:
    assert is_isogram('book') is False
