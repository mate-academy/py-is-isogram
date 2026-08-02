import pytest
from app import main


# Тести для перевірки, чи є слово ізограмою
@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("test", False),
        ("abcdefg", True),
        ("aA", False),
        ("mississippi", False),
        ("AaBbCc", False),
        ("aabbcc", False),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    """
    Тестує функцію is_isogram, яка перевіряє, чи є слово ізограмою.

    Параметри:
    - word (str): перевірене слово.
    - expected (bool): очікуваний результат.
    """
    result = main.is_isogram(word)
    assert result == expected, (f"Помилка при слові {word}, "
                                f"отримано {result}")


# Тест для випадку, коли слово складається з одного символу
def test_single_letter() -> None:
    """
    Перевіряє випадок, коли слово складається з одного символу (ізограма).
    """
    result = main.is_isogram("a")
    assert result is True, (f"Помилка при слові 'a', "
                            f"отримано {result}")


# Тест для випадку, коли слово складається з однакових літер
def test_same_letter_multiple() -> None:
    """
    Перевіряє випадок, коли слово складається з однакових літер.
    Очікується, що результат буде False.
    """
    result = main.is_isogram("aaaa")
    assert result is False, (f"Помилка при слові 'aaaa' "
                             f"отримано {result}")


# Тест для випадку великої кількості символів
def test_large_input() -> None:
    """
    Перевіряє випадок з великим словом, яке є ізограмою.
    """
    result = main.is_isogram("abcdefghijklmnopqrstuvwxyz")
    assert result is True, (f"Помилка при великому слові, "
                            f"отримано {result}")
