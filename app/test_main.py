import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "input_string,result",
    [
        (
            "playgrounds",
            True
        ),
        (
            "look",
            False
        ),
        (
            "Adam",
            False
        ),
        (
            "",
            True
        )
    ]
)
def test_is_isogram_correctly(
        input_string: str,
        result: bool
) -> None:
    assert is_isogram(input_string) == result
