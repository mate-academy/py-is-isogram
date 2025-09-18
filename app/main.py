def is_isogram(word: str) -> bool:
    if not isinstance(word, str):
        raise TypeError("word must be an string")
    word_lower = word.lower()
    for letter in word_lower:
        if word_lower.count(letter) > 1:
            return False
    return True

print(is_isogram('look'))