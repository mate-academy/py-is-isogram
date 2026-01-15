from app.main import is_isogram
from pytest import mark


@mark.parametrize(
    "value,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_is_isogram(value: str, result: bool) -> None:
    assert is_isogram(value) == result
