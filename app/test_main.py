from app.main import is_isogram


def test_should_return_true_for_empty_string() -> None:
    assert is_isogram("")


def test_should_return_true_for_all_unique_letters() -> None:
    assert is_isogram("playgrounds")


def test_should_return_false_for_duplicate_letters() -> None:
    assert not is_isogram("look")


def test_should_be_case_insensitive() -> None:
    assert not is_isogram("Adam")


def test_should_return_true_for_single_letter() -> None:
    assert is_isogram("a")


def test_should_return_false_for_same_letter_different_case() -> None:
    assert not is_isogram("aA")


def test_should_return_false_for_duplicate_letters_2() -> None:
    assert not is_isogram("local")
