from app.main import is_isogram


def test_should_return_true_for_empty_string() -> None:
    assert is_isogram("") is True


def test_should_return_true_for_isogram_string() -> None:
    assert is_isogram("playgrounds") is True


def test_should_return_false_for_same_upper_lover_letters() -> None:
    assert is_isogram("Adam") is False


def test_should_return_false_for_two_same_letters() -> None:
    assert is_isogram("look") is False
