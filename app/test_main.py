from app.main import is_isogram


def test_when_str_is_empty_should_return_true() -> None:
    assert is_isogram("") is True


def test_when_str_has_one_element_should_return_true() -> None:
    assert is_isogram("f") is True


def test_when_str_has_no_repeating_letters_should_return_true() -> None:
    assert is_isogram("false") is True


def test_when_str_has_repeating_letters_should_return_false() -> None:
    assert is_isogram("book") is False


def test_when_str_has_a_lot_of_duplicate_letters_should_return_false() -> None:
    assert is_isogram("dfghdghdfhfgdhgff") is False


def test_when_str_has_difference_register_should_return_false() -> None:
    assert is_isogram("aPple") is False


def test_when_letters_repeating_not_consecutive_should_return_false() -> None:
    assert is_isogram("celebrate") is False
