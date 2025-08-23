from app.main import is_isogram


def test_if_value_is_empty() -> None:
    assert is_isogram("") is True

def test_if_value_has_only_unique_letters() -> None:
    assert is_isogram("bad") is True
    assert is_isogram("isogram") is True

def test_if_value_has_not_unique_letters() -> None:
    assert is_isogram("look") is False
    assert is_isogram("banana") is False

def test_if_value_have_same_letter_any_case() -> None:
    assert is_isogram("pokO") is False
    assert is_isogram("HelLo") is False
