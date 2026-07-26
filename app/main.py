def validate_word(word: str) -> None:
    if not isinstance(word, str):
        raise TypeError("`word` must be a string.")
    if " " in word:
        raise ValueError("Word cannot contain spaces.")


def is_isogram(word: str) -> bool:
    validate_word(word)
    word_lower = word.lower()
    for letter in word_lower:
        if word_lower.count(letter) > 1:
            return False
    return True
