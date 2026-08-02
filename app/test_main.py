import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("Reperepe", False)
    ]
)
def test_check_input_data(word: str, result: bool) -> None:
    assert (
        is_isogram(word) == result
    )


def test_error_input_type_value() -> None:
    with pytest.raises(AttributeError):
        is_isogram(1)
