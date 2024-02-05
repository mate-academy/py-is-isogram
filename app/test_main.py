from app.main import is_isogram


def test_return_the_empty_string_true() -> None:
    assert is_isogram("")


def test_letters_must_be_in_the_same_register() -> None:
    assert not is_isogram("Adam")


def test_ead_to_the_repetition_of_letters() -> None:
    assert not is_isogram("look")


def test_should_is_an_isogram() -> None:
    assert is_isogram("playgrounds")
