from app.main import is_isogram


def test_an_empty_line_must_be_an_isogram() -> None:
    assert is_isogram("") is True


def test_case_and_isogram() -> None:
    assert is_isogram("Faf") is False


def test_not_all_words_are_isograms() -> None:
    assert is_isogram("food") is False


def test_some_words_may_be_an_isogram() -> None:
    assert is_isogram("chemistry") is True
