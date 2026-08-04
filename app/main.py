def is_isogram(word: str) -> bool:
    if not isinstance(word, str):
        raise TypeError("word must be a string")
    if word != "" and not word.isalpha():
        raise ValueError("word must contain only letters")

    # порожній рядок — ізограма
    if word == "":
        return True

    word = word.lower()
    seen = set()
    for ch in word:
        if ch in seen:
            return False
        seen.add(ch)
    return True
