from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    word = ""
    assert is_isogram(word)


def test_isogram_lowercase() -> None:
    word = "isogram"
    assert is_isogram(word)


def test_isogram_uppercase() -> None:
    word = "ISOGram"
    assert is_isogram(word)


def test_non_isogram() -> None:
    word = "hello"
    assert not is_isogram(word)


def test_mixed_case_isogram() -> None:
    word = "AbCdEfG"
    assert is_isogram(word)


def test_non_alpha_characters() -> None:
    word = "12345"
    assert is_isogram(word)
