import pytest

from app import main


def test_isogram_is_case_insensitive(monkeypatch):
    def case_sensitive_isogram(word: str):
        for letter in word:
            if word.count(letter) > 1:
                return False
        return True

    monkeypatch.setattr(main, "is_isogram", case_sensitive_isogram)

    test_result = pytest.main(["app/test_main.py"])
    assert test_result.value == 1, (
        "String with different cases of the same letter is not an isogram."
    )


def test_empty_string_is_isogram(monkeypatch):
    def non_empty_string_isogram(word: str):
        if word == "":
            return False
        word_lower = word.lower()
        for letter in word_lower:
            if word_lower.count(letter) > 1:
                return False
        return True

    monkeypatch.setattr(main, "is_isogram", non_empty_string_isogram)

    test_result = pytest.main(["app/test_main.py"])
    assert test_result.value == 1, (
        "Empty string is an isogram."
    )


def test_non_consecutive_letters_are_not_isogram(monkeypatch):
    def only_consecutive_letters_are_not_isogram(word):
        word_lower = word.lower()
        for ind in range(len(word_lower) - 1):
            if word_lower[ind] == word_lower[ind + 1]:
                return False
        return True

    monkeypatch.setattr(
        main, "is_isogram", only_consecutive_letters_are_not_isogram
    )

    test_result = pytest.main(["app/test_main.py"])
    assert test_result.value == 0, (
        "Not only consecutive letters are not an isogram."
    )


def test_consecutive_letters_are_not_isogram(monkeypatch):
    def only_non_consecutive_letters_are_not_isogram(word):
        word_lower = word.lower()
        for ind in range(1, len(word_lower) - 1):
            if (word_lower.count(word_lower[ind]) >= 2 and
                    not (word_lower[ind] == word_lower[ind + 1] or
                         word_lower[ind] == word_lower[ind - 1])):
                return False
        return True

    monkeypatch.setattr(
        main, "is_isogram", only_non_consecutive_letters_are_not_isogram
    )

    test_result = pytest.main(["app/test_main.py"])
    assert test_result.value == 0, (
        "Not only non-consecutive letters are not an isogram."
    )
