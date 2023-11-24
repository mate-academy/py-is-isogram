from app.main import is_isogram


def test_upper_letters() -> None:
    assert is_isogram("leTerst") is False
    assert is_isogram("Wwords") is False


def test_add_empty_string() -> None:
    assert is_isogram("") is True
