import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),             # порожній рядок
        ("a", True),            # одна літера
        ("playgrounds", True),  # звичайна ізограма
        ("look", False),        # повтор поспіль
        ("abca", False),        # повтор не поспіль
        ("Adam", False),        # повтор у різному регістрі
        ("PlayGrounds", True),  # змішаний регістр без повторів
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
