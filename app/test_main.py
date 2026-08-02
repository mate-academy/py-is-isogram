from app.main import is_isogram


def test_empty_string():
    result = is_isogram("")
    assert result is True


def test_uppercase_letter():
    result = is_isogram("Ananas")
    assert result is False


def test_same_letter():
    result = is_isogram("look")
    assert result is False


def test_expected_isogram():
    result = is_isogram("Olena")
    assert result is True


def test_for_symbol():
    result = is_isogram("73DNA")
    assert result is False
