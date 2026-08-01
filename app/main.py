def is_isogram(word: str) -> bool:
    if not isinstance(word, str):
        raise TypeError("Argument should be a string")
    if word and not word.isalpha():
        raise ValueError("Argument must contain only letters")

    word_lower = word.lower()
    for letter in word_lower:
        if word_lower.count(letter) > 1:
            return False
    return True
