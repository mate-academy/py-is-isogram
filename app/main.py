def is_isogram(word: str) -> bool:
    if not word:
        return True
    word_lower = word.lower()
    unique_letters = set()
    for letter in word_lower:
        if letter in unique_letters:
            return False
        unique_letters.add(letter)
    return True
