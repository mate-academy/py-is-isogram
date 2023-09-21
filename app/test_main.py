from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    word = ""
    assert is_isogram(word) is True


def test_isogram_lowercase() -> None:
    word = "isogram"
    assert is_isogram(word) is True


def test_isogram_uppercase() -> None:
    word = "ISOGram"
    assert is_isogram(word) is True


def test_non_isogram() -> None:
    word = "hello"
    assert is_isogram(word) is False


def test_mixed_case_isogram() -> None:
    word = "AbCdEfG"
    assert is_isogram(word) is True


def test_non_alpha_characters() -> None:
    word = "12345"
    assert is_isogram(word) is True

# Додаткові тести для перевірки коректності
def test_isogram_with_whitespace() -> None:
    word = "this is an isogram"
    assert is_isogram(word) is False


def test_isogram_with_hyphen() -> None:
    word = "twenty-one"
    assert is_isogram(word) is False


def test_isogram_with_apostrophe() -> None:
    word = "I'm"
    assert is_isogram(word) is True
