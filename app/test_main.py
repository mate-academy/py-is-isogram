from app.main import is_isogram


def test_string_with_repeating_letters() -> None:
    assert is_isogram("Molly") is False
    assert is_isogram("Adam") is False


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_string_with_only_unique_letters() -> None:
    assert is_isogram("Kevin") is True
