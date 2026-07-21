from app.main import is_isogram


def test_should_return_true_if_str_empty() -> None:
    assert is_isogram("") is True


def test_should_be_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_should_return_false_when_letters_repeat() -> None:
    assert is_isogram("look") is False


def test_should_true_for_isogram() -> None:
    assert is_isogram("playground") is True


def test_should_return_non_consecutive_repeating_letters() -> None:
    assert is_isogram("alphabet") is False
