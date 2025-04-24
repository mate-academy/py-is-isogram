from app.main import is_isogram


def test_should_is_isogram() -> None:
    assert is_isogram("")
    assert is_isogram("abcd")
    assert is_isogram("print")
    assert is_isogram("A")
    assert not is_isogram("Ww")
    assert not is_isogram("hallo")
    assert not is_isogram("ALsds")
    assert not is_isogram("ddd")
