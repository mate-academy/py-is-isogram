from app.main import is_isogram


def test_is_isogram_empty_string() -> None:
    assert is_isogram("") is True


def test_is_isogram_lowercase() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_mixed_case() -> None:
    assert is_isogram("Adam") is False


def test_is_isogram_duplicate_letters() -> None:
    assert is_isogram("look") is False


def test_is_isogram_case_insensitive() -> None:
    assert is_isogram("mOnItorIng") is False
    assert is_isogram("lIstEn") is True
    assert is_isogram("QuIz") is True
    assert is_isogram("aBCdEf") is True


def test_is_isogram_special_characters() -> None:
    assert is_isogram("hello_world") is False
    assert is_isogram("1234") is True
    assert is_isogram("@#*^$") is True
