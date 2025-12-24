from app.main import is_isogram


def test_is_isogram() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("look") is False
    assert is_isogram("Adam") is False
    assert is_isogram("") is True
