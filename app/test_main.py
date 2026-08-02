from app.main import is_isogram


def test_should_return_true_if_the_string_is_empty():
    assert is_isogram('')


def test_should_return_true_if_the_word_has_no_repeating_letters():
    assert is_isogram('playgrounds')


def test_should_return_false_if_word_has_repeating_letters():
    assert not is_isogram('look')


def test_should_return_false_if_word_has_repeating_lower_and_upper_letter():
    assert not is_isogram('Adam')
