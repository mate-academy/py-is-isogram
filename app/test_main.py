from app.main import is_isogram


def test_is_isogram() -> None:
    assert is_isogram("playground")
    assert not is_isogram("Look")
    assert not is_isogram("Adam")
    assert is_isogram("")
