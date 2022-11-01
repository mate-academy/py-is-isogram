from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_consecutive_same_letters() -> None:
    assert is_isogram("loOk") is False


def test_non_consecutive_same_letters() -> None:
    assert is_isogram("Adam") is False


def test_isogram_word() -> None:
    assert is_isogram("playGrounds") is True
