from app.main import is_isogram


def test_should_return_true_when_input_is_empty_string():
    assert is_isogram("")


def test_should_return_true_when_all_letters_are_unique():
    assert is_isogram('playgrounds')


def test_should_return_false_when_have_repeating_letters():
    assert not is_isogram('look')


def test_should_return_false_when_have_repeating_letters_in_different_case():
    assert not is_isogram('Adam')
