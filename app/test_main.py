from app.main import is_isogram


def test_should_string_is_empty() -> None:
    assert is_isogram("")


def test_should_word_is_isogram() -> None:
    assert is_isogram("Playground")


def test_should_word_case_insensivity() -> None:
    assert not is_isogram("Adam")


def test_should_word_is_repeating_letters() -> None:
    assert not is_isogram("look")
