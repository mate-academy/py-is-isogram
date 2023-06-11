def is_isogram(word: str) -> bool:
    word_lower = word.lower()
    if " " in word:
        raise ValueError("There is space(s) in the word")
    for letter in word_lower:
        if word_lower.count(letter) > 1:
            return False
    return True
