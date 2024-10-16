def is_isogram(word: str) -> bool:
    if not word:
        return True
    word_lower = word.lower()
    letter_set = set()
    for letter in word_lower:
        if letter in letter_set:
            return False
        letter_set.add(letter)
    return True
