import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param(
            "test", False
        ),

        pytest.param(
            "Test", False
        ),
        pytest.param(
            "", True
        ),
        pytest.param(
            "Ivan", True
        )
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
