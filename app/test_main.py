from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_case_sensitive() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("ADAM") is False
    assert is_isogram("adam") is False
    assert is_isogram("Python") is True


def test_single_character() -> None:
    assert is_isogram("a") is True
    assert is_isogram("A") is True


def test_isogram_words() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("background") is True
    assert is_isogram("lumberjacks") is True


def test_non_isogram_words() -> None:
    assert is_isogram("look") is False
    assert is_isogram("banana") is False
    assert is_isogram("mississippi") is False
