import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "string", [
        {"asdfasdf"},
        321,
        ["344"],
        1.23,
    ]
)
def test_input_type_is_string(string: str) -> None:
    with pytest.raises(TypeError):
        is_isogram(string)


@pytest.mark.parametrize(
    "string", [
        "test45",
        "321",
        "test test",
        "play_grounds",
    ]
)
def test_input_invalid_string(string: str) -> None:
    with pytest.raises(ValueError):
        is_isogram(string)


@pytest.mark.parametrize(
    "string, result", [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ]
)
def test_logic_for_correct_string_values(string: str, result: bool) -> None:
    assert is_isogram(string) == result
