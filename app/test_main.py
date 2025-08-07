import pytest
from app.main import is_isogram


@pytest.mark.parametrize("isogram,result", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True)
], ids=[
    "playgrounds is isogram",
    "look is not isogram",
    "Adam is not isogram",
    "if nothing is written, it is an isogram"

])
def test_isogram(isogram: str, result: bool) -> None:
    assert is_isogram(isogram) is result


def test_invalid_input_type_raises_error() -> None:
    with pytest.raises(AttributeError):
        is_isogram(25)
