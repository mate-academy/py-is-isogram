def is_isogram(word: str) -> bool:
    if word == "":
        return True
    if not isinstance(word, str):
        raise TypeError
    if not word.isalpha():
        raise ValueError
    word_lower = word.lower()
    for letter in word_lower:
        if word_lower.count(letter) > 1:
            return False
    return True
