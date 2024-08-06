from app.main import is_isogram


def test_returns_true_on_empty_string() -> None:
    result = is_isogram("")

    assert result == (True)


def test_returns_false_for_letters_of_different_case() -> None:
    result = is_isogram("Adam")

    assert result == (False)


def test_returns_true_when_all_letters_are_not_repeated() -> None:
    result = is_isogram("playgrounds")

    assert result == (True)


def test_returns_false_for_letters_consecutive_identical_letters() -> None:
    result = is_isogram("look")

    assert result == (False)
