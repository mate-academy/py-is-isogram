from app.main import is_isogram


def test_is_isogram_empty_string() -> None:
    # Test for empty string
    assert is_isogram("") is True


def test_is_isogram_single_character() -> None:
    # Test for single character strings
    assert is_isogram("a") is True
    assert is_isogram("Z") is True


def test_is_isogram_case_insensitivity() -> None:
    # Test case-insensitivity
    assert is_isogram("Adam") is False
    # 'A' and 'a' are the same letter
    assert is_isogram("isogram") is True


def test_is_isogram_no_repeats() -> None:
    # Test strings with no repeating characters
    assert is_isogram("playgrounds") is True
    assert is_isogram("background") is True


def test_is_isogram_with_repeats() -> None:
    # Test strings with repeating characters
    assert is_isogram("look") is False  # 'o' repeats
    assert is_isogram("banana") is False  # 'a' and 'n' repeat
    assert is_isogram("letter") is False  # 't' repeats
