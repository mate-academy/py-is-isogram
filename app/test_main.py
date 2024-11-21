from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True

def test_single_character() -> None:
    assert is_isogram("a") is True

def test_unique_characters() -> None:
    assert is_isogram("isogram") is True

def test_repeated_characters() -> None:
    assert is_isogram("repeated") is False

def test_case_insensitivity() -> None:
    assert is_isogram("Isogram") is True
    assert is_isogram("Alphabet") is False

def test_with_spaces() -> None:
    assert is_isogram("iso gram") is False

def test_with_hyphens() -> None:
    assert is_isogram("six-pack") is False
    assert is_isogram("iso-gram") is True

def test_with_numbers() -> None:
    assert is_isogram("12345") is True
    assert is_isogram("11234") is False

def test_special_characters() -> None:
    assert is_isogram("hello@!") is False
    assert is_isogram("@#$%^&") is True

def test_mixed_characters() -> None:
    assert is_isogram("abc123!@#") is True
    assert is_isogram("a1b2c3a!") is False
