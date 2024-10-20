from app.main import is_isogram


def test_is_isogram_with_empty_string() -> None:
    assert is_isogram("") is True


def test_is_isogram_with_isogram_word() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_with_repeated_letters() -> None:
    assert is_isogram("look") is False


def test_is_isogram_case_insensitive_true() -> None:
    assert is_isogram("Playground") is True


def test_is_isogram_case_insensitive_false() -> None:
    assert is_isogram("Adam") is False


def test_is_isogram_with_single_letter() -> None:
    assert is_isogram("a") is True


def test_is_isogram_with_mixed_case_isogram() -> None:
    assert is_isogram("Dermatoglyphics") is True


def test_is_isogram_with_mixed_case_non_isogram() -> None:
    assert is_isogram("Elephant") is False
