def is_isogram(word: str) -> bool:
    word_lower = word.lower()  # Convert to lowercase for case insensitivity
    seen_letters = set()  # Store seen letters

    for letter in word_lower:
        if letter in seen_letters:
            return False  # Found a duplicate letter
        seen_letters.add(letter)

    return True  # No duplicates found
