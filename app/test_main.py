from app.main import is_isogram


def test_single_lowercase_letter():
    assert is_isogram("a") is True


def test_single_uppercase_letter():
    assert is_isogram("A") is True


def test_playgrounds():
    assert is_isogram("playgrounds") is True


def test_look():
    assert is_isogram("look") is False


def test_adam():
    assert is_isogram("Adam") is False


def test_empty_string():
    assert is_isogram("") is True


def test_abc():
    assert is_isogram("abc") is True


def test_aa_mixed_case():
    assert is_isogram("Aa") is False


def test_dermatoglyphics():
    assert is_isogram("Dermatoglyphics") is True


def test_isogram():
    assert is_isogram("isogram") is True


def test_moose_mixed_case():
    assert is_isogram("moOse") is False