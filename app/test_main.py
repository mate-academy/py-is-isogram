import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,res", [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ]
)
def test_get_coin_combination(word: str, res: list) -> None:
    assert is_isogram(word) == res
