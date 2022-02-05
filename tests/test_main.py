from app.main import is_isogram


def test_is_isogram_returns_true_when_string_is_empty():
    assert is_isogram("") is True


def test_is_isogram_returns_true_when_no_repeating_letters():
    assert is_isogram("playgrounds") is True


def test_is_isogram_returns_false_when_repeating_letters_occur():
    assert is_isogram("childhood") is False


def test_is_isogram_case_insensitive():
    assert is_isogram("Choice") is False
