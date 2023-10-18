import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("isogram", True),        # Изограмное слово
        ("hello", False),         # Не изограмное слово
        ("", True),               # Пустая строка (изограм)
        (" ", True),              # Строка с пробелом (изограм)
        ("#@!123", True),         # Строка с символами (изограм)
        ("racecar", False),       # Не изограмное слово
        ("Python", True),
        ("Adam", False)
    ]
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
