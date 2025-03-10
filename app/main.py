# app/main.py

def is_isogram(word: str) -> bool:
    """
    Проверяет, является ли слово изограммой (слово без повторяющихся букв).

    :param word: слово для проверки
    :return: True, если слово является изограммой, иначе False
    """
    word_lower = word.lower()
    seen_letters = set()
    for letter in word_lower:
        if letter in seen_letters:
            return False
        seen_letters.add(letter)
    return True
