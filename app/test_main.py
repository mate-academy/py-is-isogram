from app.main import is_isogram


def test_poss_situations() -> None:
    assert is_isogram("playground") is True
    assert is_isogram("look") is False
    assert is_isogram("Adam") is False
    assert is_isogram("") is True
