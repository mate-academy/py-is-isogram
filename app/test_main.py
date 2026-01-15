from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_case_insensitive() -> None:
    assert is_isogram("Lola") is False


def test_different_letters() -> None:
    assert is_isogram("hgaiyolajdnp") is False


def test_non_isogram() -> None:
    assert is_isogram("abba") is False
