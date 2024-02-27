import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_result",
    [
        pytest.param(
            "", True, id="empty string is isogram"
        ),
        pytest.param(
            "mM", False, id="should be case insensitive"
        ),
        pytest.param(
            "mas", True, id="test string with not duplicated chars is isogram"
        ),
        pytest.param(
            "asdqwed", False,
            id="test string with duplicated chars is not isogram"
        )
    ]
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
