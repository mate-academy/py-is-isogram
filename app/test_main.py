import pytest

from typing import List
from app.main import get_coin_combination, is_isogram


def test_basic_cases() -> None:
    """Test basic examples from the requirements"""
    assert get_coin_combination(1) == [1, 0, 0, 0], "1 cent should be 1 penny"
    assert get_coin_combination(6) == [1, 1, 0, 0], (
        "6 cents should be 1 penny + 1 nickel"
    )
    assert get_coin_combination(17) == [2, 1, 1, 0], (
        "17 cents should be 2 pennies + 1 nickel + 1 dime"
    )
    assert get_coin_combination(50) == [0, 0, 0, 2], (
        "50 cents should be 2 quarters"
    )


def test_zero_cents() -> None:
    """Test edge case with 0 cents"""
    assert get_coin_combination(0) == [0, 0, 0, 0], (
        "0 cents should return all zeros"
    )


def test_single_coin_types() -> None:
    """Test cases that should use only one type of coin"""
    assert get_coin_combination(3) == [3, 0, 0, 0], \
        "3 cents should be 3 pennies"
    assert get_coin_combination(5) == [0, 1, 0, 0], \
        "5 cents should be 1 nickel"
    assert get_coin_combination(10) == [0, 0, 1, 0], \
        "10 cents should be 1 dime"
    assert get_coin_combination(25) == [0, 0, 0, 1], \
        "25 cents should be 1 quarter"


def test_combinations() -> None:
    """Test various combinations of coins"""
    assert get_coin_combination(41) == [1, 1, 1, 1], \
        "41 cents should be 1 of each coin"
    assert get_coin_combination(67) == [2, 1, 1, 2], (
        "67 cents should use multiple coins optimally"
    )
    assert get_coin_combination(99) == [4, 0, 2, 3], (
        "99 cents should use optimal combination"
    )


def test_large_amount() -> None:
    """Test a larger amount to ensure proper calculation"""
    assert get_coin_combination(137) == [2, 0, 1, 5], (
        "137 cents should work with larger numbers"
    )


@pytest.mark.parametrize("cents, expected", [
    (4, [4, 0, 0, 0]),
    (7, [2, 1, 0, 0]),
    (12, [2, 0, 1, 0]),
    (27, [2, 0, 0, 1]),
    (30, [0, 1, 0, 1]),
])
def test_various_amounts(cents: int, expected: List[int]) -> None:
    """Test various amounts using parametrize"""
    assert get_coin_combination(cents) == expected, (
        f"{cents} cents should return {expected}"
    )


def test_minimum_coins() -> None:
    """Test that the function returns the minimum number of coins"""
    for amount in [17, 41, 67, 99]:
        result: List[int] = get_coin_combination(amount)
        total_coins: int = sum(result)
        quarters: int = amount // 25
        remainder: int = amount % 25
        dimes: int = remainder // 10
        remainder = remainder % 10
        nickels: int = remainder // 5
        pennies: int = remainder % 5
        min_possible: int = quarters + dimes + nickels + pennies
        assert total_coins >= min_possible, (
            f"Should use minimum coins for {amount}"
        )


# Тести для is_isogram
def test_is_isogram_basic() -> None:
    """Test basic examples for is_isogram"""
    assert is_isogram("playgrounds") is True, \
        "playgrounds should be an isogram"
    assert is_isogram("look") is False, \
        "look has repeating 'o'"
    assert is_isogram("Adam") is False, \
        "Adam has repeating 'a' (case-insensitive)"
    assert is_isogram("") is True, \
        "empty string should be an isogram"


def test_is_isogram_case_insensitivity() -> None:
    """Test that is_isogram is case-insensitive"""
    assert is_isogram("Aa") is False, "Aa has repeating 'a' (different cases)"
    assert is_isogram("mOOn") is False, \
        "mOOn has repeating 'o' (different cases)"
    assert is_isogram("HelLo") is False, \
        "HelLo has repeating 'l' (different cases)"
    assert is_isogram("ABCde") is True, "ABCde has no repeating letters"


def test_is_isogram_consecutive_and_non_consecutive() -> None:
    """Test consecutive and non-consecutive repeating letters"""
    assert is_isogram("aa") is False, "aa has consecutive repeating 'a'"
    assert is_isogram("aba") is False, "aba has non-consecutive repeating 'a'"
    assert is_isogram("abc") is True, "abc has no repeating letters"


@pytest.mark.parametrize("word, expected", [
    ("lumberjack", True),
    ("bookkeeper", False),
    ("AaBbCc", False),  # Виправлено
    ("radar", False),
    ("Python", True),
    ("aabb", False),
    ("abca", False),
])
def test_is_isogram_various_words(word: str, expected: bool) -> None:
    """Test various words using parametrize"""
    assert is_isogram(word) is expected, (
        f"{word} should return {expected}"
    )
