from app.main import is_isogram


def test_should_return_false() -> None:
    assert is_isogram("qazxswedcCvfrghbnkj") is False


def test_should_return_true_when_empty_string() -> None:
    assert is_isogram("") is True
