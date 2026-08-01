from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    result = is_isogram("")
    assert result


def test_valid_isogram() -> None:
    result = is_isogram("tank")
    assert result


def test_word_with_consecutive_duplicates() -> None:
    result = is_isogram("look")
    assert not result


def test_word_with_non_consecutive_duplicates() -> None:
    result = is_isogram("bebra")
    assert not result


def test_case_insensitivity() -> None:
    result = is_isogram("Adam")
    assert not result


def test_all_uppercase() -> None:
    result = is_isogram("ADAM")
    assert not result


def test_mixed_case_valid_isogram() -> None:
    result = is_isogram("wHataHellIsthiSword")
    assert not result
