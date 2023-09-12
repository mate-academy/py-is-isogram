import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expect_bool",
    [
        pytest.param("playgrounds", True),
        pytest.param("look", False),
        pytest.param("Adam", False),
        pytest.param("", True)
    ]
)
def test_is_isogram(word: str, expect_bool: bool) -> None:
    assert is_isogram(word) == expect_bool
