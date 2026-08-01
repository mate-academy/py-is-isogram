def is_isogram(word: str) -> bool:
    lower_word = word.lower()
    return len(set(lower_word)) == len(lower_word)
