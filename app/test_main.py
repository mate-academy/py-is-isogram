from app.main import is_isogram
import pytest


def test_empity_string_returns_true() -> None:
    assert is_isogram("") is True


@pytest.mark.parametrize(
    ["word", "result"],
    [
        ("playground", True),
        ("look", False),
        ("Adam", False),
    ]
)
def test_if_function_is_case_insensitive(word: str, result: bool) -> None:
    assert is_isogram(word) is result


@pytest.mark.parametrize(
    ["word"],
    [
        (10,),
        (["playground"],),
        ({"word": "dict"},),
    ]
)
def test_if_raises_atribute_error_if_another_type_enter(word: str) -> None:
    with pytest.raises(AttributeError):
        is_isogram(word)
