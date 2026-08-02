from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,result",
    [
        ("", True),
        pytest.param(
            "aA",
            False,
            id="value is case-insensitive"
        ),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False)
    ]
)
def test_logic_function_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result


def test_input_type_error() -> None:
    with pytest.raises(AttributeError):
        is_isogram(90)
