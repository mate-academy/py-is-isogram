from app.main import is_isogram


def test_is_isogram_true() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_false_repeated_letters() -> None:
    assert is_isogram("look") is False


def test_is_isogram_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_is_isogram_empty_string() -> None:
    assert is_isogram("") is True


def test_is_isogram_single_letter() -> None:
    assert is_isogram("A") is True


def test_is_isogram_known_long_isogram() -> None:
    assert is_isogram("Subdermatoglyphic") is True


def test_is_isogram_all_same_letters() -> None:
    assert is_isogram("AAAA") is False


def test_is_isogram_mixed_case_duplicates() -> None:
    assert is_isogram("Alphabet") is False


def test_is_isogram_long_non_isogram() -> None:
    assert is_isogram("backgrounds") is True
