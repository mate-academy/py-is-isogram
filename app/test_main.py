from app.main import is_isogram


def test_basic_isogram_cases() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("look") is False
    assert is_isogram("Adam") is False


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_case_insensitive() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("ADAM") is False
    assert is_isogram("adam") is False
    assert is_isogram("AdAm") is False
    assert is_isogram("Playgrounds") is True


def test_single_letter() -> None:
    assert is_isogram("a") is True
    assert is_isogram("A") is True
    assert is_isogram("z") is True


def test_all_same_letter() -> None:
    assert is_isogram("aaaa") is False
    assert is_isogram("AAA") is False
    assert is_isogram("AaA") is False


def test_no_repeating_letters() -> None:
    assert is_isogram("abcdefghijklmnopqrstuvwxyz") is True
    long_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert is_isogram(long_string) is False
    assert is_isogram("abcdef") is True
    assert is_isogram("AbCdEf") is True


def test_consecutive_repeating_letters() -> None:
    assert is_isogram("hello") is False
    assert is_isogram("book") is False
    assert is_isogram("success") is False


def test_non_consecutive_repeating_letters() -> None:
    assert is_isogram("programming") is False
    assert is_isogram("python") is True
    assert is_isogram("javascript") is False


def test_mixed_case_repeats() -> None:
    assert is_isogram("MaTe") is True
    assert is_isogram("TeSt") is False
    assert is_isogram("CoDe") is True
    assert is_isogram("MaMa") is False
    assert is_isogram("TeTe") is False
