import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "value,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_should_be_correctly_result_bool(value: str, result: bool) -> None:
    assert is_isogram(value) == result
