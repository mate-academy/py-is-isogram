from app.main import is_isogram


def test_is_isogram_empty_string() -> None:
    assert is_isogram("") is True


def test_is_isogram_true() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("alphabet") is False  # 'a' się powtarza
    assert is_isogram("subdermatoglyphic") is True


def test_is_isogram_case_insensitive() -> None:
    assert is_isogram("Adam") is False  # 'a' (A) występuje dwa razy
    assert is_isogram("Aa") is False
    assert is_isogram("Bb") is False


def test_is_isogram_single_letter() -> None:
    assert is_isogram("a") is True
    assert is_isogram("Z") is True


def test_is_isogram_with_repeats() -> None:
    assert is_isogram("look") is False
    assert is_isogram("moose") is False
