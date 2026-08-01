from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("")


def test_single_character() -> None:
    assert is_isogram("a")
    assert is_isogram("b")


def test_isogram() -> None:
    assert is_isogram("abcd")
    assert is_isogram("python")


def test_not_isogram() -> None:
    assert not is_isogram("abba")
    assert not is_isogram("oppo")


def test_mixed_case() -> None:
    assert is_isogram("Abcd")
    assert not is_isogram("Abba")
    assert not is_isogram("Oppo")
