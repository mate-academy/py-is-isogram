import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,true_or_false",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_check_does_this_shit_work(word: str, true_or_false: bool) -> None:
    assert is_isogram(word) == true_or_false
