from app.main import is_isogram


def test_should_return_true_for_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_should_return_false_for_repeated_letters() -> None:
    assert is_isogram("looks") is False


def test_should_be_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_should_return_true_for_empty_string() -> None:
    assert is_isogram("") is True
