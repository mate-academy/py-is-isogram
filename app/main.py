def is_isogram(word: str) -> bool:
    if not isinstance(word, str):
        raise TypeError("Input must be a string")

    word_lower = word.lower()
    return len(word_lower) == len(set(word_lower))
