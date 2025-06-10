from app.main import is_isogram


def test_should_check_isogram() -> None:
    assert is_isogram("today") == True


def test_should_return_false() -> None:
    assert is_isogram("look") == False


def test_should_be_case_insensitive() -> None:
    assert is_isogram("Adam") == False


def test_should_check_empty_string() -> None:
    assert is_isogram("") == True
