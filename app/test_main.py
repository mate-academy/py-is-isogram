from app.main import is_isogram


def test_should_return_true_if_is_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_should_return_false_if_is_not_isogram_start_with_capital() -> None:
    assert is_isogram("Adam") is False


def test_should_return_false_if_is_not_isogram_start_with_lower() -> None:
    assert is_isogram("look") is False


def test_should_return_true_for_empty_string() -> None:
    assert is_isogram("") is True
