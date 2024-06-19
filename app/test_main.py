from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, result",
    [
        ("background", True),
        ("Downstream", True),
        ("lumberjacks", True),
        ("isogram", True),
        ("Google", False),
        ("Community", False),
        ("System", False),
        ("Colony", False),
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
