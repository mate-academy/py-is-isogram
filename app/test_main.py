from app.main import is_isogram


def test_() -> None:
    assert is_isogram("playgrounds") is True


def test_should_return_false_simply() -> None:
    assert is_isogram("look") is False


def test_should_return_false_when_uppercase() -> None:
    assert is_isogram("Adam") is False


def test_should_return_true_when_empty() -> None:
    assert is_isogram("") is True
