def is_isogram(word: str):
    word_lower = word.lower()
    for letter in word_lower:
        if word_lower.count(letter) > 1:
            return False
    return True


def case_sensitive_isogram(word: str):
    for letter in word:
        if word.count(letter) > 1:
            return False
    return True
