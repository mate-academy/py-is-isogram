from app.main import is_isogram


def test_is_isogram() -> None:
    assert is_isogram("abcdef")
    assert is_isogram("word")
    assert is_isogram("")
    assert is_isogram("A")
    assert is_isogram("Word")
    assert not is_isogram("zZ")
    assert not is_isogram("aa")
    assert not is_isogram("aabbcc")


def test_non_consecutive_letters_are_not_isogram() -> None:
    assert not is_isogram("hello")
    assert not is_isogram("ball")
