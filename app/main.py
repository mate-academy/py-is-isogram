def is_isogram(word: str) -> bool:
    word_lower = word.lower()
    for letter in word_lower:
        if word_lower.count(letter) > 1:
            return False
    return True


print(
    is_isogram("playgrounds") is True,
    is_isogram("look") is False,
    is_isogram("Adam") is False,
    is_isogram("") is True,
)
