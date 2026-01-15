from app.main import is_isogram


def test_result_is_bool() -> None:
    result = is_isogram("Ring")
    assert isinstance(result, bool)


def test_empty_string() -> None:
    result = is_isogram("")
    assert result is True


def test_not_repeat_letters() -> None:
    result = is_isogram("playgrounds")
    assert result is True


def test_repeat_letters() -> None:
    result = is_isogram("Arian")
    assert result is False


def test_repeated_letters_in_one_word() -> None:
    result = is_isogram("Aaaa")
    assert result is False
