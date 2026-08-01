def is_isogram(word: str) -> bool:
    word_lower = word.lower()
    for letter in word_lower:
        if word_lower.count(letter) > 1:
            if letter == " " or letter == "-":
                continue
            return False
    return True
