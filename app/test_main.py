from app.main import is_isogram


def test_with_empty_string() -> None:
    assert (is_isogram("") is True), "Test should return True"


def test_uppercase_and_lowercase_do_not_matters() -> None:
    assert (is_isogram("AbCaBc") is False), "Test should return False"


def test_same_letters() -> None:
    assert (is_isogram("Hello") is False), "Test should return False"


def test_is_unique_all_letters() -> None:
    assert (is_isogram("Ukraine") is True), "Test should return True"
