def is_isogram(word: str) -> bool:
    return len(set(word.lower())) == len(word)
