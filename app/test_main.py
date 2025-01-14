from app.main import is_isogram

def test_empty_string() -> None:
    assert is_isogram("") is True


def test_isogram_is_case_insensitive() -> None:
    assert is_isogram("HeLlo") is False


def test_not_only_consecutive_letters_are_not_an_isogram() -> None:
    assert is_isogram("helicopter") is False
