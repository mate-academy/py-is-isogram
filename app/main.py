def is_isogram(word: str) -> bool:
    word_lower = word.lower()
    for letter in word_lower:
        if letter.isdigit():
            raise ValueError
        if word_lower.count(letter) > 1:
            return False
    return True
