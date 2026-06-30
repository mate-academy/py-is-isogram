from app.main import is_isogram

def test_should_return_true_if_str_empty():
    assert is_isogram("") == True


def test_should_be_case_insensitive():
    assert is_isogram("aA") is False


def test_should_return_false_when_letters_repeat():
    assert is_isogram("look") is False
