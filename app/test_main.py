from app.main import is_isogram
import pytest


def test_should_return_bool() -> None:
    assert is_isogram("word") is True, "Must return true"


@pytest.mark.parametrize(
    "word,is_true",
    [
        ("", True),
        ("word", True),
        ("soS", False),
        ("round", True),
        ("qwertyuiopasdfghjkl", True),
        ("metachArsEtwindowS", False)
    ],
    ids=[
        "must be true when string is empty",
        "must be true when word is 'word'",
        "must be false for same letters in upper and lower",
        "must be true for 'round'",
        "must ber true for different letters",
        "must be false when letters repeat in word"
    ]
)
def test_should_return_correct_result_for_each_arguments(
        word: str,
        is_true: bool
) -> None:
    assert is_isogram(word) == is_true, f"result must be{is_true}"
