import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    ("word", "expected"),
    [
        # Порожній рядок та одна літера
        ("", True),
        ("a", True),
        ("A", True),
        # Валідні ізограми (усі літери унікальні)
        ("playgrounds", True),
        ("Dermatoglyphics", True),
        ("AbCdEf", True),
        # Повторення поруч
        ("look", False),
        ("letter", False),
        # Повторення не поруч
        ("moose", False),
        ("aba", False),
        # Повторення в різному регістрі (case-insensitive)
        ("Adam", False),
        ("isogramI", False),
        ("AA", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
