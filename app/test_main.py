from app.main import is_isogram


def test_should_check_true() -> None:
    assert is_isogram("playgrounds") is True


def test_should_check_false() -> None:
    assert is_isogram("look") is False


def test_should_return_bool() -> None:
    assert isinstance(is_isogram("look"), bool)


def test_should_check_null_string() -> None:
    assert is_isogram("") is True


def test_should_check_case_of_letters() -> None:
    assert is_isogram("loOk") is False
