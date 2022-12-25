from app.main import is_isogram


def test_for_true_case() -> None:
    assert is_isogram('playgrounds') is True


def test_for_false_case() -> None:
    assert is_isogram('look') is False
    assert is_isogram('Adam') is False


def test_for_empty_string() -> None:
    assert is_isogram('') is True
