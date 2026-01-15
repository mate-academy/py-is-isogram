def is_isogram(word: str) -> bool:
    word = word.lower()
    return len(word) == len(set(word))
