from app.main import is_isogram


def test_when_used_different_register() -> None:
    assert not is_isogram("Adam")


def test_with_other_symbols() -> None:
    assert not is_isogram("_main_")


def test_when_value_is_empty() -> None:
    assert is_isogram("")


def test_when_word_is_isogram() -> None:
    assert is_isogram("table")
