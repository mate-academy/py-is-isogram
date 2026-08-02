from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_isogram_word() -> None:
    assert is_isogram("playgrounds") is True


def test_non_isogram_word() -> None:
    assert is_isogram("look") is False


def test_case_insensitivity() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("MaDaM") is False


def test_mixed_case_isogram() -> None:
    assert is_isogram("MixEd") is True


def test_repeated_letters() -> None:
    assert is_isogram("aa") is False
    assert is_isogram("aba") is False
    assert is_isogram("racecar") is False


def test_mixed_case_repeated_letters() -> None:
    assert is_isogram("Aa") is False
    assert is_isogram("aA") is False
    assert is_isogram("AA") is False


def test_long_word() -> None:
    assert is_isogram("abcdefghijklmnopqrstuvwxyz") is True
