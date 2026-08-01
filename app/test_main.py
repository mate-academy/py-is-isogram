import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "test_input,expected",
    [
        pytest.param("playgrounds", True,
                     id="should return True if no repeating letters"),
        pytest.param("look", False,
                     id="return False if some letters repeat"),
        pytest.param("Adam", False,
                     id="function should be case-insensitive"),
        pytest.param("", True,
                     id="empty string is an isogram"),
    ]
)
def test_is_isogram(test_input: str, expected: bool) -> None:
    assert is_isogram(test_input) == expected
