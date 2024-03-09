from app.main import is_isogram


def test_is_true_if_empty() -> None:
    assert is_isogram("") is True


def test_upper_and_lower_are_the_same() -> None:
    assert is_isogram("Mum") is False


def test_is_true_if_isogram() -> None:
    assert is_isogram("playgrounds") is True
