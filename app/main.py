def is_isogram(word: str) -> bool:
    if not isinstance(word, str):
        raise TypeError("Input must be a string")

    word_lower = word.lower()
    return len(set(word_lower)) == len(word_lower)
