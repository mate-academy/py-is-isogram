from app.main import is_isogram


def test_empty_string() -> None:
    """An empty string is an isogram."""
    assert is_isogram("")


def test_isogram_lowercase() -> None:
    """Lowercase isograms should return True."""
    assert is_isogram("playgrounds")


def test_non_isogram_repeating_letters() -> None:
    """Words with repeating letters should return False."""
    assert not is_isogram("look")


def test_non_isogram_case_insensitive() -> None:
    """Case-insensitive checks should be done (A and a count as same)."""
    assert not is_isogram("Adam")


def test_mixed_case_isogram() -> None:
    """Ensure mixed-case isograms return True."""
    assert is_isogram("Dermatoglyphics")


def test_mixed_case_non_isogram() -> None:
    """Ensure mixed-case non-isograms return False."""
    assert not is_isogram("Alphabet")


def test_single_letter() -> None:
    """A single letter is always an isogram."""
    assert is_isogram("a")


def test_long_isogram() -> None:
    """A long isogram should be correctly identified."""
    assert is_isogram("subdermatoglyphic")
