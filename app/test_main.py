from app.main import is_isogram


def test_is_isogram_empty_string() -> None:
    assert is_isogram("")


def test_is_isogram_single_letter() -> None:
    assert is_isogram("A")


def test_is_isogram_all_unique() -> None:
    assert is_isogram("playgrounds")


def test_is_isogram_repeated_letters() -> None:
    assert not is_isogram("look")


def test_is_isogram_mixed_case() -> None:
    assert not is_isogram("Adam")


def test_is_isogram_case_insensitive_true() -> None:
    assert is_isogram("Dermatoglyphics")


def test_is_isogram_case_insensitive_false() -> None:
    assert not is_isogram("Alphabet")
