from app.main import is_isogram


def test_should_return_true_for_isograms() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("subdermatoglyphic") is True
    assert is_isogram("") is True  # порожній рядок — ізограма


def test_should_return_false_for_non_isograms() -> None:
    assert is_isogram("look") is False
    assert is_isogram("banana") is False
    assert is_isogram("letter") is False


def test_should_be_case_insensitive() -> None:
    assert is_isogram("Adam") is False  # A та a повторюються
    assert is_isogram("Dermatoglyphics") is True
    assert is_isogram("Isogram") is True
