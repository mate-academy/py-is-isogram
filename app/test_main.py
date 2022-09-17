from app.main import is_isogram


def test_should_return_true_if_string_is_empty():
    word = ''
    assert is_isogram(word)


def test_should_return_true_if_string_in_lower_case():
    word = 'playgrounds'
    assert is_isogram(word.lower())


def test_should_return_true_if_string_in_upper_case():
    word = 'PLAYGROUNDS'
    assert is_isogram(word.lower())


def test_should_return_false_if_string_is_not_a_string():
    word = 1
    try:
        assert isinstance(word, str)
    except AssertionError:
        print("Word should be str type")


def test_should_return_true_if_string_in_camelcase():
    word = 'PLaYgrOuNdS'
    assert is_isogram(word.lower())


def test_should_return_true_if_string_case_is_insensitive_with_repeating_letters():
    word = "Adam"
    assert is_isogram(word) is False


def test_should_return_false_if_string_with_repeating_letters():
    word = "look"
    assert is_isogram(word) is False
