def is_isogram(word: str) -> bool:

    if any(char.isdigit() for char in word):
        raise TypeError

    word_lower = word.lower()

    for letter in word_lower:
        if word_lower.count(letter) > 1:
            return False
    return True
