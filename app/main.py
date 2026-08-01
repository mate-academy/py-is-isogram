def is_isogram(word: str) -> bool:
    if not isinstance(word, str):
        raise TypeError("Word must be a string")

    word_lower = word.lower()
    for letter in word_lower:
        if word_lower.count(letter) > 1:
            return False
    return True
