from app.main import is_isogram


def test_should_return_true_to_empty_word() -> None:
    assert (is_isogram("") is True
            ), "Should return true to empty word"


def test_should_return_true_to_isogram() -> None:
    assert (is_isogram("playgrounds") is True
            ), "Should return true to isogram"


def test_should_return_false_to_consecutive_repeating_letters() -> None:
    assert (is_isogram("look") is False
            ), "Should return false to consecutive repeating letters"


def test_should_return_false_to_nonconsecutive_repeating_letters() -> None:
    assert (is_isogram("Adam") is False
            ), "Should return false to non-consecutive repeating letters"
