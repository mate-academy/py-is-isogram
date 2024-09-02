from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("")


def test_case_sensitive() -> None:
    assert is_isogram("Dermatoglyphics")


def test_non_isogram() -> None:
    assert not is_isogram("Adam")
