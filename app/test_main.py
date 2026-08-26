from app.main import is_isogram


def test_is_isogram_should_return_true_if_count_equal_to_1() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_should_return_true_if_string_empty() -> None:
    assert is_isogram("") is True


def test_is_isogram_should_return_false_if_count_higher_than_1() -> None:
    assert is_isogram("look") is False
    assert is_isogram("Adam") is False
