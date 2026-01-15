import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "value, expected",
    [
        pytest.param("", True, id="'True' for empty value"),
        pytest.param("playgrounds", True, id="'True' for isogram"),
        pytest.param("Adam", False, id="Function should be case-insensitive"),
        pytest.param("look", False, id="'False' if the letters are repeated")
    ]
)
def test_isogram(value: str, expected: bool) -> None:
    assert is_isogram(value) == expected
