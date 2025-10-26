def is_isogram(word: str) -> bool:
    if not isinstance(word, str):
        raise TypeError("argument type must be a string")
    if not word.isalpha() and word:
        raise ValueError("string must be empty or contain only letters")

    word_lower = word.lower()
    for letter in word_lower:
        if word_lower.count(letter) > 1:
            return False
    return True
