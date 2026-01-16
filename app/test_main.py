from app.main import is_isogram


def test_empty_str() -> None:
    assert is_isogram("")


def test_isogram_single_character() -> None:
    assert is_isogram("a")


def test_isogram_playgrounds() -> None:
    assert is_isogram("playgrounds")


def test_isogram_look() -> None:
    assert not is_isogram("look")


def test_isogram_adam() -> None:
    assert not is_isogram("Adam")


def test_isogram_uppercase_mixed() -> None:
    assert not is_isogram("Alphabet")


def test_isogram_case_insensitive() -> None:
    assert is_isogram("Dermatoglyphics")


def test_isogram_long_non_isogram() -> None:
    assert is_isogram("subdermatoglyphic")


def test_isogram_with_repeated_characters() -> None:
    assert not is_isogram("eleven")


def test_isogram_with_unique_characters() -> None:
    assert is_isogram("subway")


def test_isogram_with_all_alphabets() -> None:
    assert is_isogram("abcdefghijklmnopqrstuvwxyz")
