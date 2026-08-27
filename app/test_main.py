import pytest
from app import main


@pytest.mark.parametrize(
    "text,expected",
    [
        pytest.param("", True, id="empty string"),
        pytest.param("playgrounds", True, id="all unique letters"),
        pytest.param("Dermatoglyphics", True, id="mixed case isogram"),
        pytest.param("look", False, id="string not isogram"),
        pytest.param("Adam", False, id="string with capital not isogram"),
        pytest.param("alphabet", False, id="non-consecutive duplicate"),
    ]
)
def test_is_isogram(text: str, expected: bool) -> None:
    assert main.is_isogram(text) == expected
