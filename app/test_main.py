import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("", True),
        pytest.param("test", False),
        pytest.param("Test", False),
        pytest.param("o", True),
        pytest.param("oo", False),
        pytest.param("keyboard", True),
    ]
)
def test_is_isogram(
        word: str,
        result: bool
) -> None:
    assert is_isogram(word) == result
