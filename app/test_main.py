from app.main import is_isogram


def test_should_return_true_for_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_should_return_false_for_repeated_letters() -> None:
    assert is_isogram("look") is False


def test_should_be_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_should_return_true_for_empty_string() -> None:
    assert is_isogram("") is True


def test_should_return_true_for_single_letter() -> None:
    assert is_isogram("a") is True


def test_should_detect_non_consecutive_repeated_letters() -> None:
    assert is_isogram("letter") is False


def test_should_handle_uppercase_isogram() -> None:
    assert is_isogram("WORLD") is True
