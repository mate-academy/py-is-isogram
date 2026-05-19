def is_isogram(word: str) -> bool:
    if not isinstance(word, str):
        raise TypeError("Argument must be string")
    if not word.isalpha() and word != "":
        raise TypeError("Argument must be string with only letter")
    word_lower = word.lower()
    for letter in word_lower:
        if word_lower.count(letter) > 1:
            return False
    return True
