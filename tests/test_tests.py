from app import main
import pytest


@pytest.mark.parametrize("word, expected", [("Aa", False), ("abc", True)])
def test_isogram_is_case_insensitive(monkeypatch, word, expected):
    def case_sensitive_isogram(word: str):
        for letter in word:
            if word.count(letter) > 1:
                return False
        return True

    monkeypatch.setattr(main, "is_isogram", case_sensitive_isogram)

    test_result = pytest.main(["app/test_main.py"])
    assert test_result.value == 0, \
        f"String with different cases of the same letter is not an isogram. " \
                                   f"Input: {word}, Expected: {expected}"


@pytest.mark.parametrize("word, expected", [("", True), ("abc", True)])
def test_empty_string_is_isogram(monkeypatch, word, expected):
    def only_empty_string_is_isogram(word):
        return word == ""


    monkeypatch.setattr(main, "is_isogram", only_empty_string_is_isogram)

    test_result = pytest.main(["app/test_main.py"])
    assert (
        test_result.value == 0
    ), f"Empty string is an isogram. Input: {word}, Expected: {expected}"



@pytest.mark.parametrize("word, expected", [("abc", True), ("aba", False)])
def test_consecutive_letters_are_not_isogram(monkeypatch, word, expected):
    def only_non_consecutive_letters_are_not_isogram(word):
        word_lower = word.lower()
        for ind in range(len(word_lower) - 1):
            if word_lower[ind] == word_lower[ind + 1]:
                return False
        return True

    monkeypatch.setattr(
        main, "is_isogram", only_non_consecutive_letters_are_not_isogram
    )

    test_result = pytest.main(["app/test_main.py"])
    assert (
        test_result.value == 0
    ), f"Not only consecutive letters are not an isogram. Input: {word}, Expected: {expected}"


@pytest.mark.parametrize("word, expected", [("abc", True), ("aba", False)])
def test_consecutive_letters_are_not_isogram(monkeypatch, word, expected):
    def only_non_consecutive_letters_are_not_isogram(word):
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
        main, "is_isogram", only_non_consecutive_letters_are_not_isogram
    )

    test_result = pytest.main(["app/test_main.py"])
    assert (
        test_result.value == 0
    ), f"Not only non-consecutive letters are not an isogram. Input: {word}, Expected: {expected}"
