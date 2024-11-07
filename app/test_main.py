from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("")


def test_single_letter() -> None:
    assert is_isogram("a")


def test_isogram_word() -> None:
    assert is_isogram("category")


def test_repeating_letters() -> None:
    assert not is_isogram("look")


def test_mixed_case_word() -> None:
    assert is_isogram("Alex")


def test_mixed_case_word_with_doubles_letter() -> None:
    assert not is_isogram("Tests")
