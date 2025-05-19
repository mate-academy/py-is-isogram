from app.main import is_isogram


def test_return_type() -> None:
    result = is_isogram("ala")
    assert isinstance(result, bool)
    assert not result


def test_upper_case() -> None:
    result = is_isogram("Ala")
    assert not result


def test_result_is_false() -> None:
    result = is_isogram("look")
    assert not result


def test_result_is_true() -> None:
    result = is_isogram("playgrounds")
    assert result


def test_on_empty_string() -> None:
    result = is_isogram("")
    assert result
