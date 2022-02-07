import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("abcdefghijklmnopqrstuvwxyz", True),
        ("ABCdeFghijKlmnOpqrsTuvwxyZ", True),
        ("ZYXWVUTSRQPONMLKJIHGFEDCBA", True),
    ]
)
def test_for_all_alphabet_in_mixed_case(word, expected):
    assert is_isogram(word) is expected


def test_for_empty_string():
    assert is_isogram('') is True


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param(
            "FhjhuigfffFfFfFfFfFfFfAaAaAa",
            False,
            id="Test repeat letters in different cases"),
        pytest.param(
            "haroldddddddddddd",
            False,
            id="Test repeat letters in lower case"
        ),
        pytest.param(
            "QQQDDDDJJJJJJSSSFFFF",
            False,
            id="Test repeat letters in upper case"
        ),
    ]
)
def test_for_repeat_letters(word, expected):
    assert is_isogram(word) is expected
