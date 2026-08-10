from app.main import is_isogram


def test_is_isogram_empty_string() -> None:
    """Test that an empty string is an isogram."""
    assert is_isogram("") is True


def test_is_isogram_case_insensitive() -> None:
    """Test that function is case-insensitive."""
    assert is_isogram("Adam") is False
    assert is_isogram("Dermatoglyphics") is True


def test_is_isogram_repeating_letters() -> None:
    """Test words with repeating letters."""
    assert is_isogram("look") is False
    assert is_isogram("playgrounds") is True


def test_is_isogram_no_repeating_letters() -> None:
    """Test words with no repeating letters."""
    assert is_isogram("isogram") is True
    assert is_isogram("uncopyrightable") is True
