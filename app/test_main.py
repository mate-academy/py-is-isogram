from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_not_only_consecutive_letters() -> None:
    assert is_isogram("aba") is False

def different_case_of_letters() -> None:
    assert is_isogram("isIsogram") is False


def test_is_isogram() -> None:
    assert is_isogram("isogram") is True


def test_different_cases_of_the_same_letter() -> None:
    assert is_isogram("moOse") is False
