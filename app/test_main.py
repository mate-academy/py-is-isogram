import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param(
            "",
            True,
            id="True for empty string"
        ),
        pytest.param(
            "look",
            False,
            id="Repeated letters - should be False"
        ),
        pytest.param(
            "Adam",
            False,
            id="Case insensitive repeat - should be False"
        ),
        pytest.param(
            "uNcopyriGhtaBle",
            True,
            id="Long isogram with upper letters - should be True"
        )
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
