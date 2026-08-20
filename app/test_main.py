import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,correct_output",
    [
        pytest.param(
            "", True, id="if word is empty"
        ),
        pytest.param(
            "Adam", False, id="test for case insensitivity"
        ),
        pytest.param(
            "playgrounds", True, id="long word test"
        ),
        pytest.param(
            "aabb", False, id="consecutive letters test"
        )
    ]
)
def test_func(word: str, correct_output: bool) -> None:
    assert is_isogram(word) == correct_output
