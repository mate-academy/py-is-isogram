def is_isogram(word: str) -> bool:
    validate(word)

    word_lower = word.lower()
    for letter in word_lower:
        if word_lower.count(letter) > 1:
            return False
    return True


def validate(word: str) -> None:
    if not isinstance(word, str):
        raise TypeError

    for char in word:
        if not char.isalpha():
            raise ValueError
