from app.main import is_isogram


def test_one_letter() -> None:
    assert is_isogram("l") is True


def test_two_letters() -> None:
    assert is_isogram("is") is True


def test_three_letters() -> None:
    assert is_isogram("too") is False


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_case_insensitivity() -> None:
    assert is_isogram("Adam") is False
