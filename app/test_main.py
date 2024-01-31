import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "world,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test(world: str, result: bool) -> None:
    assert is_isogram(world) == result
