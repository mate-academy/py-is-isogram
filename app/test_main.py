def is_isogram(word: str) -> bool:
    """Check if a word is an isogram."""
    if not word:
        return True

    word_lower = word.lower()
    for letter in word_lower:
        if word_lower.count(letter) > 1:
            return False
    return True


def test_isogram_is_case_insensitive() -> None:
    """Test that function is case-insensitive."""
    result = is_isogram("Adam")
    assert not result, (
        "String with different cases of the same letter is not an isogram."
    )


def test_empty_string_is_isogram() -> None:
    """Test that empty string is considered an isogram."""
    result = is_isogram("")
    assert result, "Empty string should be an isogram."


def test_non_consecutive_letters_are_not_isogram() -> None:
    """Test that non-consecutive repeating \
    letters make the word not an isogram."""
    result = is_isogram("banana")
    assert not result, (
        "Non-consecutive repeating letters are not handled properly."
    )


def test_consecutive_letters_are_not_isogram() -> None:
    """Test that consecutive repeating letters make the word not an isogram."""
    result = is_isogram("look")
    assert not result, (
        "Consecutive repeating letters are not handled properly."
    )
