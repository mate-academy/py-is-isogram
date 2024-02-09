from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") == True
