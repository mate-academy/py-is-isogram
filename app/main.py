def is_isogram(word: str) -> bool:
    seen = set()
    for letter in word.lower():
        if letter in seen:
            return False
        seen.add(letter)
    return True
