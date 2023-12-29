from app.main import is_isogram


def test_is_isogram_empty_string() -> None:
    assert is_isogram("") is True


def test_is_isogram_case_insensitive() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("MaDaM") is False
    assert is_isogram("MoM") is False


def test_is_isogram_true_cases() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("abcdefghijklmnopqrstuvwxyz") is True
    assert is_isogram("qwertyuiopasdfghjklzxcvbnm") is True


def test_is_isogram_false_cases() -> None:
    assert is_isogram("look") is False
    assert is_isogram("repeated") is False
    assert is_isogram("hello") is False
