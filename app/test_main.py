from app.main import is_isogram


def test_is_isogram() -> None:
    assert is_isogram("abcdef")
    assert is_isogram("word")
    assert is_isogram("Word")
    assert is_isogram("")
    assert is_isogram("A")
    assert not is_isogram("zZ")
    assert not is_isogram("aa")
    assert not is_isogram("aabbcc")

