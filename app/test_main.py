from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "line,result",
    [
        ("playground", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("worm", True)
    ]
)
def test_should_return_right_values(
        line: str,
        result: bool
) -> None:
    assert is_isogram(line) is result
