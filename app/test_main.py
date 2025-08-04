from app.main import is_isogram


def test_empty_string() -> None:
    word = ""
    assert is_isogram(word) is True


def test_different_cases_of_the_same_letter() -> None:
    word = "Adam"
    assert is_isogram(word) is False


def test_identical_letters() -> None:
    word = "dder"
    assert is_isogram(word) is False


def test_different_letters() -> None:
    word = "playgrounds"
    assert is_isogram(word) is True
