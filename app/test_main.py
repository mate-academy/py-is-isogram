from app.main import is_isogram


def test_is_isogram_case_insensitive() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("PlayGrounds") is True
    assert is_isogram("Adam") is False
    assert is_isogram("aA") is True


def test_is_isogram_empty_string() -> None:
    assert is_isogram("") is True


def test_is_isogram_no_repeating_letters() -> None:
    assert is_isogram("abcdef") is True


def test_is_isogram_repeating_letters() -> None:
    assert is_isogram("look") is False


def test_is_isogram_single_character() -> None:
    assert is_isogram("a") is True
    assert is_isogram("Z") is True


def test_is_isogram_with_mixed_case() -> None:
    assert is_isogram("aA") is True
    assert is_isogram("lOOK") is False
