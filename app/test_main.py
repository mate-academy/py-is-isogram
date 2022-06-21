from app.main import is_isogram


def test_should_return_true_when_string_is_isogram():
    assert is_isogram("playgrounds") is True


def test_should_return_true_when_string_is_empty():
    assert is_isogram("") is True


def test_should_return_false_when_letters_in_different_cases():
    assert is_isogram("lOok") is False


def test_should_return_false_if_the_letters_are_not_next_to_each_other():
    assert is_isogram("Adam") is False
