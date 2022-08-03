from app.main import is_isogram


def test_if_empty_string():
    assert is_isogram("") is True


def test_if_identical_letters_next_to_each_other():
    assert is_isogram("Annet") is False


def test_if_identical_letters_separately():
    assert is_isogram("Anka") is False


def test_if_no_identical_letters():
    assert is_isogram("President") is True
