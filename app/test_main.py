from app.main import is_isogram


def test_should_return_expected_is_isogram():
    word = is_isogram('playgrounds')

    assert word is True


def test_should_return_expected_when_empty_string():
    word = is_isogram('')

    assert word is True


def test_should_return_expected_not_isogram():
    word = is_isogram('Adam')

    assert word is False


def test_should_word_is_consecutive_letters():
    word = is_isogram('look')

    assert word is False
