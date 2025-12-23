import pytest
from app.main import is_isogram


def test_is_isogram() -> None:
    assert is_isogram("playgrounds"),\
        "Expected True for 'playgrounds', but got False"
    assert not is_isogram("look"),\
        "Expected False for 'look', but got True"
    assert not is_isogram("Adam"),\
        "Expected False for 'Adam', but got True"
    assert is_isogram(""),\
        "Expected True for '', but got False"
    assert is_isogram("abcdef"),\
        "Expected True for 'abcdef', but got False"
    assert not is_isogram("AaBbCc"),\
        "Expected False for 'AaBbCc', but got True"
    assert is_isogram("isogram"),\
        "Expected True for 'isogram', but got False"
    assert not is_isogram("test"),\
        "Expected False for 'test', but got True"
    assert not is_isogram("unique"),\
        "Expected False for 'unique', but got True"


if __name__ == "__main__":
    pytest.main()
