import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_result",
    [
        pytest.param(
            "playgrounds",
            True,
            id="long word",
        ),
        pytest.param(
            "look",
            False,
            id="word with doubling",
        ),
        pytest.param(
            "Adam",
            False,
            id="word with capital letter",
        ),
        pytest.param(
            "",
            True,
            id="empty string",
        )
    ]
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
