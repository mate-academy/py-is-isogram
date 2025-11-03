def is_isogram(word: str) -> bool:
    """
    Проверяет, является ли слово изограммой.
    Изограмма — это слово без повторяющихся букв
    (без учёта регистра). Пустая строка — изограмма.

    Args:
        word (str): входное слово, состоящее только из букв.

    Returns:
        bool: True, если слово — изограмма, иначе False.
    """
    word_lower = word.lower()
    for letter in word_lower:
        if word_lower.count(letter) > 1:
            return False
    return True
