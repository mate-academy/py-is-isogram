def is_isogram(word: str) -> bool:
    if not word.isalpha() and word != "":
        raise ValueError
    word_lower = word.lower()
    for letter in word_lower:
        if word_lower.count(letter) > 1:
            return False
    return True
