from app import main


def test_is_isogram_true():
    assert main.is_isogram("playgrounds") is True


def test_is_isogram_false_with_repeated_letters():
    assert main.is_isogram("look") is False


def test_is_isogram_case_insensitive():
    assert main.is_isogram("Adam") is False  # 'A' == 'a'


def test_empty_string_is_isogram():
    assert main.is_isogram("") is True


def test_is_isogram_with_consecutive_repeats():
    assert main.is_isogram("committee") is False


def test_is_isogram_with_non_consecutive_repeats():
    assert main.is_isogram("alphabet") is False


def test_is_isogram_single_letter():
    assert main.is_isogram("a") is True


def test_is_isogram_mixed_case_is_same():
    assert main.is_isogram("Dermatoglyphics") is True
