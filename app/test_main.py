import pytest
from app.main import is_isogram

def test_is_isogram() -> None:
    assert is_isogram('') == True
    assert is_isogram('abiogeneses') == False
    assert is_isogram('cholangiogram') == False
    assert is_isogram('stu') == False
    assert is_isogram('background') == True


if __name__ == '__main__':
    pytest.main()


