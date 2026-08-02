from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_upper_and_lower_case_string() -> None:
    assert is_isogram("Sdf") is True
    assert is_isogram("Sdfs") is False
    assert is_isogram("SDf") is True
    assert is_isogram("SdDf") is False


def test_long_word() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("matemathic") is False
