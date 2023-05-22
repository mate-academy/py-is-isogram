from app.main import is_isogram


def test_the_empty_string_is_an_isogram() -> None:
    assert is_isogram("") is True

def test_can_be_is_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_the_function_should_be_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_consecutive_letters_are_not_isogrm() -> None:
    assert is_isogram("look") is False