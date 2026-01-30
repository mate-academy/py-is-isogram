import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("play", True),
        ("subdermatoglyphic", True), # Длинная изограмма
        ("moo", False),              # Повтор в конце
        ("look", False),             # Повтор в середине
        ("aba", False),              # Повтор через букву
        ("Adam", False),             # Регистр
        ("Aa", False),               # Короткий регистр
        ("Alphabet", False),         # Повтор первой и последней 'a'
        ("éléphant", False),         # Повтор с диакритикой (если важно)
        ("nn", False),               # Минимальный повтор подряд
    ]
)
def test_is_isogram_various_cases(word: str, expected: bool) -> None:
    # Используем '==' вместо 'is' для булевых значений в тестах 
    # (иногда pytest.main капризничает с 'is' при моках)
    assert is_isogram(word) == expected
