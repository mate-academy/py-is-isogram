from app.main import is_isogram


def test_should_return_true_when_string_empty() -> None:
    assert is_isogram("") is True


def test_should_return_false_with_different_cases_same_letters() -> None:
    assert is_isogram("Aloha") is False
