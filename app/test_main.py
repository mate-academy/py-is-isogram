from app.main import is_isogram


def test_is_isogram_should_return_true_for_isogram_word() -> None:
    assert is_isogram("Dermatoglyphics") is True
    assert is_isogram("isogram") is True


def test_is_isogram_should_return_false_for_repeating_letters() -> None:
    assert is_isogram("aba") is False
    assert is_isogram("moose") is False


def test_is_isogram_should_be_case_insensitive() -> None:
    # Важливо: 'm' та 'M' мають вважатися однаковою літерою
    assert is_isogram("moOse") is False
    assert is_isogram("isIsogram") is False


def test_is_isogram_should_return_true_for_empty_string() -> None:
    assert is_isogram("") is True
