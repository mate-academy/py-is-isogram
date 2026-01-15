from app.main import is_isogram


def test_is_isogram_empty_string() -> None:
    assert is_isogram("") is True


def test_is_isogram_lowercase_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_lowercase_not_isogram() -> None:
    assert is_isogram("look") is False


def test_is_isogram_mixed_case_not_isogram() -> None:
    assert is_isogram("Adam") is False


def test_is_isogram_mixed_case_isogram() -> None:
    assert is_isogram("MoDeL") is True


def test_is_isogram_uppercase_isogram() -> None:
    assert is_isogram("WHATSUP") is True


def test_is_isogram_uppercase_not_isogram() -> None:
    assert is_isogram("ROBOTICS") is False
