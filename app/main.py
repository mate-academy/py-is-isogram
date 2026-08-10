def is_isogram(word: str) -> bool:
    """Check if the given word is an isogram (no repeating letters)."""
    word_lower = word.lower()
    for letter in word_lower:
        if word_lower.count(letter) > 1:
            return False
    return True
