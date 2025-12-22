import pytest
import app.main as main


# --- Przykłady z treści zadania ---
@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),  # 'a' powtarza się niezależnie od wielkości litery
        ("", True),
    ],
)
def test_examples_from_spec(word: str, expected: bool) -> None:
    assert main.is_isogram(word) is expected


# --- Pojedyncza litera zawsze jest isogramem ---
@pytest.mark.parametrize("word", ["a", "Z", "m"])
def test_single_letter_is_isogram(word: str) -> None:
    assert main.is_isogram(word) is True


# --- Wszystkie litery różne ---
def test_all_unique_letters_is_isogram() -> None:
    word_str = "abcdefgHIJklmn"
    assert main.is_isogram(word_str) is True


# --- Powtórzenia niekolejne też dyskwalifikują ---
@pytest.mark.parametrize("word", ["paper", "banana", "letter"])
def test_non_consecutive_repeated_letter_is_not_isogram(word: str) -> None:
    assert main.is_isogram(word) is False


# --- Niezależność od wielkości liter ---
@pytest.mark.parametrize("word", ["IsoGramM", "Aa", "mMm"])
def test_case_insensitive_detection(word: str) -> None:
    assert main.is_isogram(word) is False
