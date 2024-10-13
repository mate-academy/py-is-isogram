import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "value,result",
    [
        pytest.param(
            "playgrounds",
            True,
            id="should return True if word is isogram"
        ),
        pytest.param(
            "look",
            False,
            id="should return False if word is not isogram"
        ),
        pytest.param(
            "Mam",
            False,
            id="should be case-insensitive"
        ),
        pytest.param(
            "",
            True,
            id="should return True for empty string"
        )
    ]
)
def test_is_isogram(value: str, result: bool) -> None:
    assert is_isogram(value) == result
