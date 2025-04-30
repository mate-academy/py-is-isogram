from app.main import is_isogram


def test_should_return_true_for_empty_string() -> None:
    assert is_isogram("") == True


def test_should_return_true_for_all_unique_letters() -> None:
    assert is_isogram("playgrounds") == True


def test_should_return_false_for_duplicate_letters() -> None:
    assert is_isogram("look") == False


def test_should_be_case_insensitive() -> None:
    assert is_isogram("Adam") == False


def test_should_return_true_for_single_letter() -> None:
    assert is_isogram("a") == True


def test_should_return_false_for_same_letter_different_case() -> None:
    assert is_isogram("aA") == False

def test_should_return_false_for_duplicate_letters_2() -> None:
    assert is_isogram("local") == False

