def is_isogram(word: str):
    word_lower = word.lower()
    if not word_lower.isalpha() and len(word) != 0:
        return False
    for letter in word_lower:
        if word_lower.count(letter) > 1:
            return False
    return True
