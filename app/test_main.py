from app.main import is_isogram


def test_empty_string_is_an_isogram() -> None:
    assert is_isogram("") is True


def test_single_letter_is_an_isogram() -> None:
    assert is_isogram("a") is True
    assert is_isogram("b") is True
    assert is_isogram("A") is True
    assert is_isogram("B") is True


def test_isogram_word() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("subdermatoglyphic") is True
    assert is_isogram("unsubcontracted") is False


def test_non_isogram_word() -> None:
    assert is_isogram("look") is False
    assert is_isogram("tango") is True
    assert is_isogram("bookkeeper") is False


def test_mixed_case_words() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("ArT") is True
    assert is_isogram("MuM") is False
    assert is_isogram("Sun") is True
