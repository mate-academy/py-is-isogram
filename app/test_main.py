from app.main import is_isogram


def test_should_return_true_for_empty_string() -> None:
    assert is_isogram("") is True


def test_should_return_true_for_valid_isogram() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("world") is True
    assert is_isogram("isogram") is True


def test_should_return_false_when_letters_repeat() -> None:
    assert is_isogram("look") is False
    assert is_isogram("aba") is False
    assert is_isogram("alphabet") is False


def test_should_be_case_insensitive() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("Success") is False
    assert is_isogram("moOse") is False


def test_should_return_true_for_single_letter() -> None:
    assert is_isogram("A") is True
    assert is_isogram("z") is True
