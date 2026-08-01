from app.main import is_isogram


def test_if_empty_string() -> None:
    assert is_isogram("")


def test_if_string_is_isogram() -> None:
    assert is_isogram("Polyc")


def test_if_string_is_not_isogram() -> None:
    assert not is_isogram("aba")


def test_if_string_is_not_isogram_case_insensitive() -> None:
    assert not is_isogram("Okrio")
