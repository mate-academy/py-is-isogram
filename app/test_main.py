import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param(
            "playgrounds",
            True,
            id="This word is an isogram"
        ),
        pytest.param(
            "look",
            False,
            id="Word has repeating letters, consecutive or non-consecutive."
        ),
        pytest.param(
            "Adam",
            False,
            id="Function should be case-insensitive"
        ),
        pytest.param(
            "",
            True,
            id="The empty string in this case is an isogram"
        ),
    ]
)
def test_check_isogram_result(word: str, result: bool) -> None:
    assert (
        is_isogram(word) is result
    )
