import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,condition",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
    ids=[
        "playgrounds is True",
        "look is False",
        "Adam is False",
        "'' is True",
    ]
)
def test_can_sum(word: str, condition: bool) -> None:
    assert is_isogram(word) is condition
