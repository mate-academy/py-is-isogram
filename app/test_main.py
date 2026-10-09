from app.main import is_isogram


def test_should_return_true_when_string_is_empty() -> None:
    assert is_isogram("") is True


def test_should_return_true_when_word_has_one_letter() -> None:
    assert is_isogram("a") is True


def test_should_return_true_when_all_letters_are_different() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("background") is True


def test_should_return_false_when_consecutive_letters_repeat() -> None:
    assert is_isogram("look") is False
    assert is_isogram("oo") is False


def test_should_return_false_when_nonconsecutive_letters_repeat() -> None:
    assert is_isogram("aba") is False
    assert is_isogram("abca") is False
    assert is_isogram("isograms") is False


def test_should_ignore_case_when_checking_repeated_letters() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("aA") is False
    assert is_isogram("abcA") is False


def test_should_return_true_when_different_letters_have_any_case() -> None:
    assert is_isogram("Python") is True
    assert is_isogram("aB") is True
    assert is_isogram("ABc") is True
