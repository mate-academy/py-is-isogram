from app.main import is_isogram


def test_empty_string_is_isogram():
    goals = is_isogram('')

    assert goals is True


def test_non_consecutive_letters_are_not_isogram():
    goals = is_isogram('acba')

    assert goals is False


def test_isogram_is_case_insensitive():
    goals = is_isogram('Adam')

    assert goals is False
