from app.main import is_isogram


def test_empty() -> None:
    assert is_isogram("") is True


def test_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_upper() -> None:
    assert is_isogram("PlaYgRouNds") is True


def test_repeating_registry() -> None:
    assert is_isogram("PpLlAaYyGgRrOoUuNnDdSs") is False


def test_non_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("abc") is False
