from app.main import is_isogram


def test_should_be_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_should_return_true_when_string_is_empty() -> None:
    assert is_isogram("") is True


def test_should_return_false_when_string_have_same_letters() -> None:
    assert is_isogram("look") is False


def test_should_return_true_when_string_is_isogram() -> None:
    assert is_isogram("playgrounds") is True
