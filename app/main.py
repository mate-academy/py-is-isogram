def is_isogram(word: str) -> bool:
    if word == "":
        return True
    word_lower = word.lower()
    for letter in word_lower:
        if word_lower.count(letter) > 1:
            return False
    return True
