import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    ("word", "expected"),
    [
        ("", True),             # порожній рядок — ізограма
        ("playgrounds", True),  # усі літери унікальні
        ("look", False),        # повторюється 'o'
        ("Adam", False),        # A == a (регістр ігноруємо)
        ("Python", True),
        ("Alphabet", False),
        ("Isogram", True),
        ("letter", False),      # повтор у кінці
        ("a", True),            # одна літера
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
