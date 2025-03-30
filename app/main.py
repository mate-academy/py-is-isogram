def is_isogram(word: str) -> bool:
    word_lower = word.lower()
    return len(set(word_lower)) == len(word_lower)
