from app.main import is_isogram


def test_should_return_true_for_empty_string() -> None:
    assert is_isogram("")


def test_should_return_true_for_isogram() -> None:
    assert is_isogram("playgrounds")


def test_should_return_false_for_same_neighbors() -> None:
    assert not is_isogram("look")


def test_should_return_false_for_same_non_consecutive_letters() -> None:
    assert not is_isogram("abca")


def test_should_return_false_for_different_case_of_same_letter() -> None:
    assert not is_isogram("Adam")
