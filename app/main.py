def is_isogram(word: str) -> bool:
    word = word.lower()  # Переведемо всі букви у нижній регістр
    letters_seen = set()

    for letter in word:
        if letter.isalpha():
            if letter in letters_seen:
                return False
            letters_seen.add(letter)

    return True
