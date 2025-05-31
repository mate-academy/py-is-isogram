from app.main import is_isogram


def test_should_return_true_if_string_empty() -> None:
    assert is_isogram("")


def test_should_return_true_if_string_is_isogram() -> None:
    assert is_isogram("playgrounds")


def test_should_return_false_if_string_is_not_isogram() -> None:
    assert not is_isogram("look")


def test_should_be_case_insensitive() -> None:
    assert not is_isogram("Adam")
