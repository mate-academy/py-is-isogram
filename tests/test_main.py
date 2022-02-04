from app.main import is_isogram


def test_empty_string_should_return_true():
    assert is_isogram("")


def test_lower_and_upper_cases():
    assert is_isogram("IsOGraM")
    assert not is_isogram("pashTet")


def test_is_isogram_true():
    assert is_isogram("cat")
    assert is_isogram("Duplicates")


def test_is_isogram_false():
    assert not is_isogram("Dictionary")
    assert not is_isogram("woodoo")


def test_symbols():
    assert is_isogram("!@#$%^&*()_+?><")
