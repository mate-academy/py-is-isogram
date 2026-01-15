def is_isogram(word: str) -> bool:
    """
    Determine if a word is an isogram (no repeating letters, ignoring case
    and non-letter characters).

    Args:
        word: Input string to check

    Returns:
        bool: True if isogram, False otherwise
    """
    cleaned = [char.lower() for char in word if char.isalpha()]
    return len(cleaned) == len(set(cleaned))
