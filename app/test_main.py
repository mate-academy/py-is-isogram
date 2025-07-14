from app.main import is_isogram


def test_casual_case() -> None:
    assert is_isogram("over") == True


def test_false_case() -> None:
    assert is_isogram("hello") == False


def test_empty_string() -> None:
    assert is_isogram("") == True


def test_case_immune() -> None:
    assert is_isogram("helLo") == False


def test_non_consecutive_letters() -> None:
    assert is_isogram("aaaa")
