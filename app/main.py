def is_isogram(word: str) -> bool:
    word_lower = word.lower()
    return len(word_lower) == len(set(word_lower))
