from app.main import is_isogram


def test_true_when_str_playgrounds():
    assert is_isogram('playgrounds') is True


def test_false_when_str_look():
    assert is_isogram('look') is False


def test_false_when_str_adam():
    assert is_isogram('Adam') is False


def test_true_when_str_is_empty():
    assert is_isogram('') is True


def test_spaces():
    assert is_isogram(" lucky ") is False
