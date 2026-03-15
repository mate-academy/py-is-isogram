def is_isogram(word: str) -> bool:
    if not isinstance(word, str):
        raise TypeError("Input must be a string")
    letters = [char.lower() for char in word if char.isalpha()]
    return len(letters) == len(set(letters))
