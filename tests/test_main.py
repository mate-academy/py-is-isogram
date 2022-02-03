from app.main import is_isogram


# 1. PEP 8: E712 comparison to True should be 'if cond is True:' or 'if cond:'
# 2. PEP 8: E712 comparison to False should be 'if cond is False:'
#    or 'if not cond:'

def test_empty_string():
    assert is_isogram("") == 1


def test_case_insensitive():
    assert is_isogram("LKJFSDLIlsdfeojf") == 0
    assert is_isogram("QWERTyuiop") == 1


def test_core_functionality():
    assert is_isogram("sldkfjrjfdmo") == 0
    assert is_isogram("asdfghjk09865") == 1
