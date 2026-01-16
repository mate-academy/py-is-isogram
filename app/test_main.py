from app.main import is_isogram


def test_isogram_in_number() -> None:
    assert is_isogram("") is True
    assert is_isogram("hello") is False
    assert is_isogram("abacadae") is False
    assert is_isogram("HeLLo") is False
    assert is_isogram("HelLo") is False
