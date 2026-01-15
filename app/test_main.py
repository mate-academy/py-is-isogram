import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "isogram,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ]
)
def test_get_correct_combination(isogram: str, result: bool) -> None:
    assert is_isogram(isogram) == result
