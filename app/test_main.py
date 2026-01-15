import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result", [
        pytest.param(
            "World", True, id="letter case is not essential"
        ),
        pytest.param(
            "", True, id="empty string is isogram"
        ),
        pytest.param(
            "colOr",
            False,
            id="non-consecutive letters are not isogram dispite of case"
        ),
        pytest.param(
            "cooler", False, id="consecutive letters are not isogram"
        )
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
