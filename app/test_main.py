from app.main import is_isogram


def test_empty_string_is_an_isogram() -> None:
    result = is_isogram(word="")
    assert result is True, f"Result expected to be True, but got {result}"


def test_string_has_no_repeating_letters() -> None:
    result = is_isogram(word="playgrounds")
    assert result is True, f"Result expected to be True, but got {result}"


def test_string_should_be_case_insensitive() -> None:
    result = is_isogram(word="Playgrounds")
    assert result is True, f"Result expected to be True, but got {result}"


def test_consecutive_letters_are_not_an_isogram() -> None:
    result = is_isogram(word="look")
    assert result is False, f"Result expected to be True, but got {result}"


def test_non_consecutive_letters_are_not_an_isogram() -> None:
    result = is_isogram(word="Adam")
    assert result is False, f"Result expected to be True, but got {result}"
