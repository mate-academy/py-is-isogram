from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_all_unique_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_repeated_letters_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_reapet_letters() -> None:
    assert is_isogram("Mm") is False


def test_non_isogram() -> None:
    assert is_isogram("look") is False
