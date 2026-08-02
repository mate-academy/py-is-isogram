from app.main import is_isogram


def test_check_empty_string() -> None:
    assert is_isogram("")


def test_check_string_with_same_letters() -> None:
    result = is_isogram("look")
    assert not result


def test_check_string_with_diferent_letters() -> None:
    result = is_isogram("playgrounds")
    assert result


def test_check_string_with_diferent_upper_letters() -> None:
    result = is_isogram("PlayGrOunDs")
    assert result


def test_check_string_with_same_upper_letters() -> None:
    result = is_isogram("lOok")
    assert not result


def test_check_string_with_integer() -> None:
    result = is_isogram("10")
    assert not result
