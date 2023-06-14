from app.main import is_isogram


def test_must_work_with_uppercase() -> None:
    assert is_isogram("zoOm") is False


def test_should_return_true_when_str_empty() -> None:
    assert is_isogram("") is True


def test_non_consecutive_letters() -> None:
    assert is_isogram("bozo") is False
