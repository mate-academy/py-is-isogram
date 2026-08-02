from app.main import is_isogram


def test_is_isogram_returns_true_for_isogram_word() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_returns_false_for_non_isogram_word() -> None:
    assert is_isogram("look") is False


def test_is_isogram_returns_false_for_non_isogram_word_case_insensitive()\
        -> None:
    assert is_isogram("Adam") is False


def test_is_isogram_returns_true_for_empty_string() -> None:
    assert is_isogram("") is True


def test_is_isogram_accepts_only_letters() -> None:
    assert is_isogram("123") is True
    assert is_isogram("@#$%") is True
