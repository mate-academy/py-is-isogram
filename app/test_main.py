from app.main import is_isogram


def test_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_repeated_consecutive_letters() -> None:
    assert is_isogram("look") is False


def test_repeated_letters_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_single_letter() -> None:
    assert is_isogram("a") is True


def test_all_unique_letters() -> None:
    assert is_isogram("python") is True


def test_repeated_non_consecutive_letters() -> None:
    assert is_isogram("hello") is False


def test_uppercase_letters() -> None:
    assert is_isogram("PYTHON") is True


def test_mixed_case_unique_letters() -> None:
    assert is_isogram("AbCdEf") is True


def test_repeated_letter_with_different_case() -> None:
    assert is_isogram("aAbB") is False
