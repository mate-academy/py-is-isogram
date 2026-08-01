def is_isogram(word: str) -> bool:
    if not isinstance(word, str):
        raise TypeError

    clean_word = word.lower()
    return len(clean_word) == len(set(clean_word))
