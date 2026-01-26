def is_isogram(word: str) -> bool:
    if word == "":
        return True
    if type(word) is not str:
        raise TypeError

    if not word.isalpha():
        raise ValueError

    word_lower = word.lower()
    for letter in word_lower:
        if word_lower.count(letter) > 1:
            return False
    return True
