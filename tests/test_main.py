from app.main import is_isogram


def test_empty_string():
    assert is_isogram('')


def test_isogram_string():
    tested_string = 'abc'
    assert is_isogram(tested_string)


def test_non_isogram_string():
    tested_string = 'abcCbA'
    assert not is_isogram("abcCbA")
