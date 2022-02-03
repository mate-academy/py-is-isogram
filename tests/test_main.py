from app.main import is_isogram


def test_if_string_is_empty():
    assert is_isogram("") is True


def test_if_string_contains_repeating_letters():
    assert is_isogram("loOk") is False
    assert is_isogram("Adam") is False


def test_if_string_does_not_contain_repeating_letters():
    assert is_isogram("playgrounds") is True
    assert is_isogram("Dmytro") is True
