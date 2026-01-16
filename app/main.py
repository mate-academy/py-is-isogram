def is_isogram(word: str) -> bool:
    """
    Проверяет, является ли слово изограммой.

    Изограмма — это слово без повторяющихся букв
    (без учета регистра). Пустая строка считается изограммой.

    Args:
        word (str): Слово, состоящее только из букв.

    Returns:
        bool: True, если слово — изограмма, иначе False.
    """
    word_lower = word.lower()
    return len(set(word_lower)) == len(word_lower)
