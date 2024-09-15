from app.main import is_isogram


def test_spase_should_true():
    assert is_isogram('') is True


def test_word_should_true():
    assert is_isogram('playgrounds') is True


def test_dubbing_letters_should_false():
    assert is_isogram('look') is False


def test_case_insensitive():
    assert is_isogram('Adam') is False
