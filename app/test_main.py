from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("")


def test_single_letter() -> None:
    assert is_isogram("a")


def test_repeated_letter() -> None:
    assert not is_isogram("look")


def test_isogram_all_lowercase() -> None:
    assert is_isogram("playgrounds")


def test_isogram_mixed_case() -> None:
    assert is_isogram("DerMatOglYphIc")


def test_non_isogram_mixed_case() -> None:
    assert not is_isogram("Adam")


def test_long_isogram() -> None:
    assert is_isogram("subdermatoglyphic")


def test_long_non_isogram() -> None:
    assert not is_isogram("subdermatoglyphics")
