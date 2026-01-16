import pytest
from _pytest.monkeypatch import MonkeyPatch
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("isogram", True),
        ("Alphabet", False),
        ("Dermatoglyphics", True),
        ("moOse", False),
        ("subdermatoglyphic", True),
    ]
)
def test_is_isogram_cases(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


def test_isogram_is_case_insensitive(monkeypatch: MonkeyPatch) -> None:
    def case_sensitive_isogram(word: str) -> bool:
        for letter in word:
            if word.count(letter) > 1:
                return False
        return True

    monkeypatch.setattr("app.main.is_isogram", case_sensitive_isogram)
    assert not is_isogram("Adam"), (
        "String with different cases of the same letter is not an isogram."
    )


def test_empty_string_is_isogram(monkeypatch: MonkeyPatch) -> None:
    def non_empty_string_isogram(word: str) -> bool:
        if word == "":
            return False
        word_lower = word.lower()
        for letter in word_lower:
            if word_lower.count(letter) > 1:
                return False
        return True

    monkeypatch.setattr("app.main.is_isogram", non_empty_string_isogram)
    assert is_isogram("") is True, (
        "Empty string should be considered an isogram."
    )


def test_non_consecutive_letters_are_not_isogram(
    monkeypatch: MonkeyPatch
) -> None:
    def only_consecutive_letters_are_not_isogram(word: str) -> bool:
        word_lower = word.lower()
        for ind in range(len(word_lower) - 1):
            if word_lower[ind] == word_lower[ind + 1]:
                return False
        return True

    monkeypatch.setattr(
        "app.main.is_isogram", only_consecutive_letters_are_not_isogram
    )
    assert not is_isogram("look"), (
        "Non-consecutive duplicates should also break isogram status."
    )


def test_consecutive_letters_are_not_isogram(monkeypatch: MonkeyPatch) -> None:
    def only_non_consecutive_letters_are_not_isogram(word: str) -> bool:
        word_lower = word.lower()
        for ind in range(1, len(word_lower) - 1):
            if (
                word_lower.count(word_lower[ind]) >= 2
                and not (
                    word_lower[ind] == word_lower[ind + 1]
                    or word_lower[ind] == word_lower[ind - 1]
                )
            ):
                return False
        return True

    monkeypatch.setattr(
        "app.main.is_isogram", only_non_consecutive_letters_are_not_isogram
    )
    assert not is_isogram("look"), (
        "Consecutive duplicates should also break isogram status."
    )
