def is_isogram(word: str) -> bool:
    word_lower = word.lower()
    # Check if it's an isogram
    seen_chars = set()
    for char in word_lower:
        if char.isalpha():
            if char in seen_chars:
                return False
            seen_chars.add(char)
    return True
