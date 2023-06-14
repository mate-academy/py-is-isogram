import pytest

from app.main import is_isogram


@pytest.mark.parametrize("value,result",
                         [("playgrounds", True),
                          ["look", False]])
def test_usual_input(value: str, result: bool) -> None:
    assert is_isogram(value) is result


def test_empty_line() -> None:
    assert is_isogram("") is True


def test_input_upper_letters() -> None:
    assert is_isogram("Adam") is False


@pytest.mark.parametrize("value",
                         [1, 2.3, {}, [], ()])
def test_correct_errors(value: any) -> None:
    try:
        is_isogram(value)
    except (AttributeError, TypeError):
        pass
