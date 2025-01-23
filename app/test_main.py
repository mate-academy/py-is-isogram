import pytest
from app import main
from _pytest.monkeypatch import MonkeyPatch


def test_empty_string_is_isogram() -> None:
    assert main.is_isogram("") is True


def test_simple_isogram() -> None:
    assert main.is_isogram("abcde") is True


def test_non_isogram_with_consecutive_letters() -> None:
    assert main.is_isogram("aabbc") is False


def test_non_isogram_with_non_consecutive_letters() -> None:
    assert main.is_isogram("abcda") is False


def test_case_insensitive_isogram() -> None:
    assert main.is_isogram("AbCdE") is True


def test_case_insensitive_non_isogram() -> None:
    assert main.is_isogram("AbCdAa") is False


def test_another_isogram() -> None:
    assert main.is_isogram("zxcvbnm") is True


def test_another_non_isogram() -> None:
    assert main.is_isogram("programming") is False


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("", True),
        ("abcde", True),
        ("aabbc", False),
        ("abcda", False),
        ("AbCdE", True),
        ("AbCdAa", False),
        ("zxcvbnm", True),
        ("programming", False),
    ],
)
def test_is_isogram_parametrized(word: str, expected_result: bool) -> None:
    assert main.is_isogram(word) is expected_result


def test_isogram_is_case_insensitive(monkeypatch: MonkeyPatch) -> None:
    def case_sensitive_isogram(word: str) -> bool:
        for letter in word:
            if word.count(letter) > 1:
                return False
        return True

    monkeypatch.setattr(main, "is_isogram", case_sensitive_isogram)

    # Запускаємо тести з поточного файлу
    test_result = pytest.main([__file__])
    assert test_result.value == 1, (
        "String with different cases of the same letter is not an isogram."
    )
