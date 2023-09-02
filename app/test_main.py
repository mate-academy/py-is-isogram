from app.main import is_isogram


def test_is_isogram_be_empty() -> None:
    assert is_isogram("")


def test_is_isogram_be_repeating_letters() -> None:
    assert not is_isogram("apple")


def test_is_isogram_no_repeating_letters() -> None:
    assert is_isogram("machine")


def test_is_isogram_be_case_insensitive() -> None:
    assert not is_isogram("Adam")
