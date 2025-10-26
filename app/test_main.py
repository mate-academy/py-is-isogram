import pytest
from app.main import is_isogram


def test_is_isogram_returns_bool_for_valid_string() -> None:
    assert isinstance(is_isogram("hello"), bool)


@pytest.mark.parametrize("value, result", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True),
    ("Mm", False)
])
def test_is_isogram_examples_from_task(value: str, result: bool) -> None:
    assert is_isogram(value) == result


@pytest.mark.parametrize("value, expect", [
    pytest.param(1, TypeError, id="argument type must be a string"),
    pytest.param("abc123",
                 ValueError,
                 id="string must be empty or contain only letters"
                 )
])
def test_is_isogram_raises_error(value: object, expect: object) -> None:
    with pytest.raises(expect):
        is_isogram(value)
