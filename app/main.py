def is_isogram(word: str) -> bool:
    normalized_word = word.casefold()
    return len(normalized_word) == len(set(normalized_word))
