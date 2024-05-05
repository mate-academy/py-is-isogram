from app.main import is_isogram


def test_is_isogram_empty_string():
    assert is_isogram('') == True


def test_is_isogram_case_insensitive():
    assert is_isogram('Adam') == False
    assert is_isogram('adam') == False
    assert is_isogram('AdamM') == False


def test_is_isogram_isograms():
    assert is_isogram('playgrounds') == True
    assert is_isogram('background') == True
    assert is_isogram('subdermatoglyphic') == True

def test_is_isogram_non_isograms():
    assert is_isogram('look') == False
    assert is_isogram('mirror') == False
    assert is_isogram('apple') == False