def is_isogram(word: str) -> bool:
    word_lower = word.lower()
    for letter in word_lower:
        if letter.isnumeric():
            return False
        if word_lower.count(letter) > 1:
            return False
    return True
