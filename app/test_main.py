from app.main import is_isogram


# write your code here
def test_isogram_true() -> None:
    assert is_isogram("playgrounds") is True


def test_isogram_false() -> None:
    assert is_isogram("look") is False


def test_different_cases() -> None:
    assert is_isogram("Adam") is False


def test_empty_string() -> None:
    assert is_isogram("") is True
