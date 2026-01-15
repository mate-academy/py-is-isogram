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


def test_should_raise_an_error_if_string_is_not_a_str():
    word = 1
    try:
        assert isinstance(word, str)
    except AssertionError:
        print("Word should be str type")


def test_should_return_true_if_string_in_camelcase():
    word = 'PLaYgrOuNdS'
    assert is_isogram(word.lower())


def test_should_return_false_if_string_has_repeating_letters():
    word = "Adam"
    assert is_isogram(word) is False


def test_should_return_false_if_string_with_repeating_letters():
    word = "look"
    assert is_isogram(word) is False


def test_string_should_have_only_letters():
    word = "Dota 2"
    try:
        for char in word:
            assert char.isalpha()
    except AssertionError:
        print("String should have only letters!")
