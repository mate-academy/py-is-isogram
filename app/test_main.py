from app.main import is_isogram


def test_casual_case() -> None:
    assert is_isogram("over")


def test_false_case() -> None:
    assert not is_isogram("hello")


def test_empty_string() -> None:
    assert is_isogram("")


def test_case_immune() -> None:
    assert not is_isogram("helLo")


def test_non_consecutive_letters() -> None:
    assert not is_isogram("aba")
