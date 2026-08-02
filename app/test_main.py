from app.main import is_isogram


def test_should_return_true_for_isogram() -> None:
    assert is_isogram("Playgrounds") is True


def test_should_return_false_for_one_letter_with_different_cases() -> None:
    assert is_isogram("Adam") is False


def test_should_return_false_for_repeating_letters() -> None:
    assert is_isogram("look") is False


def test_should_return_true_for_empty_string() -> None:
    assert is_isogram("") is True
