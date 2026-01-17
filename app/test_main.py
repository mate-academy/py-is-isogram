from app.main import is_isogram


def test_empty_word() -> None:
    assert (
        is_isogram("") is True
    ), "Should return True if passed empty word"


def test_repeat_in_word() -> None:
    assert (
        is_isogram("look") is False
    ), "Should return False if there are repeated symbols in word"


def test_check_case_insensitive_repeat() -> None:
    assert (
        is_isogram("Adam") is False
    ), ("Should return False if there are repeated symbols "
        "in word (case insensitive)")


def test_check_non_repeat_word() -> None:
    assert (
        is_isogram("playgrounds") is True
    ), ("Should return True if there are no repeated symbols "
        "in word")
