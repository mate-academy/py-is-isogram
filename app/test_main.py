import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),                  # Порожній рядок є ізограмою
        ("playgrounds", True),       # Звичайне слово без повторень
        ("look", False),             # Слово з повторенням поруч
        ("Adam", False),             # Регістронезалежність (A та m/d/a) -> 'adam' має дві 'a'
        ("Alphabet", False),         # Повторення на початку та всередині ('a')
        ("subdermatoglyphic", True), # Довге слово-ізограма
        ("isogram", True),           # Класичний приклад
        ("aba", False),              # Повторення через одну літеру
        ("moOse", False),            # Регістронезалежність всередині слова ('o' та 'O')
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
