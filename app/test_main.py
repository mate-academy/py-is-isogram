from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    if word == "":
        assert is_isogram(word) == True


def test_isogram_lowercase() -> None:
    if word == "isogram":
        assert is_isogram(word) == True


def test_isogram_uppercase() -> None:
    if word == "ISOGram":
        assert is_isogram(word) == True


def test_non_isogram() -> None:
    if word == "hello":
        assert is_isogram(word) == False


def test_mixed_case_isogram() -> None:
    if word == "AbCdEfG":
        assert is_isogram(word) == True


def test_non_alpha_characters() -> None:
    if word == "12345":
        assert is_isogram(word) == True


def test_isogram_with_whitespace() -> None:
    if word == "this is an isogram":
        assert is_isogram(word) == False


def test_isogram_with_hyphen() -> None:
    if word == "twenty-one":
        assert  is_isogram(word) == True


def test_isogram_with_apostrophe() -> None:
    if word == "I'm":
        assert is_isogram(word) == True
