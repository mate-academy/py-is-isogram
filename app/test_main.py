from app.main import is_isogram


def test_get_bool_from_empty_string():
    word = ""

    value = is_isogram(word)

    assert value is True


def test_get_bool_if_string_is_isogram():
    word = "playgrounds"

    value = is_isogram(word)

    assert value is True


def test_get_bool_if_string_is_no_isogram():
    word = "look"

    value = is_isogram(word)

    assert value is False


def test_get_bool_if_string_is_capitalize():
    word = "Mam"

    value = is_isogram(word)

    assert value is False
