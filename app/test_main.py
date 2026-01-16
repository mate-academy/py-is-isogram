from app.main import is_isogram


def test_non_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("")


def test_base_pass_phrase() -> None:
    assert is_isogram("playgrounds")


def test_base_not_pass_test() -> None:
    assert not is_isogram("look")


def test_isogram_is_case_insensitive() -> None:
    assert not is_isogram("lOok")


def test_consecutive_letters() -> None:
    assert not is_isogram("abababa")
