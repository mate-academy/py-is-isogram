import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,is_isogram_result",
    [
        pytest.param(
            "word",
            True,
            id="word 'word' is isogram"
        ),
        pytest.param(
            "",
            True,
            id="empty string is isogram"
        ),
        pytest.param(
            "moment",
            False,
            id="repeating non-consecutive letters not allowed"
        ),
        pytest.param(
            "Moment",
            False,
            id="case of letters doesnt matter"
        ),
        pytest.param(
            "cool",
            False,
            id="repeating consecutive letters not allowed"
        )
    ]
)
def test_is_isogram_work_correct(word: str, is_isogram_result: bool) -> None:
    assert is_isogram(word) == is_isogram_result
