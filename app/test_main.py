import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, excepted",
    [
        ("playgrounds", True),
        ("", True),
        ("look", False),
        ("Adam", False),
    ]
)
def test_check_right_result(word: str, excepted: bool) -> None:
    assert is_isogram(word) == excepted
