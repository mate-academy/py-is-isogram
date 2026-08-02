from app.main import is_isogram


def test_empty_word_value():
    assert is_isogram("") is True


def test_upper_lower_case_value():
    assert is_isogram("Aa") is False


def test_spaces_true_value():
    assert is_isogram("bla ") is True
    assert is_isogram(" aw") is True


def test_spaces_false_value():
    assert is_isogram(" bla ") is False
    assert is_isogram("  bla") is False


def test_all_true_values():
    assert is_isogram("ocean7!&?") is True


def test_all_false_values():
    assert is_isogram("ook") is False
    assert is_isogram("&&as") is False
