from app.main import is_isogram


def test_isogram_is_true() -> None:
    assert is_isogram("playgrounds") is True


def test_isogram_is_false() -> None:
    assert is_isogram("look") is False


def test_empty_sting() -> None:
    assert is_isogram("") is True


def test_different_case_of_the_sme_letter() -> None:
    assert is_isogram("Adam") is False
