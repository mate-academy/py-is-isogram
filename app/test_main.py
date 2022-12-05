import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "check_word,bool_result",
    [
        pytest.param(
            "",
            True,
            id="should return 'True' if value is empty string"
        ),
        pytest.param(
            "playgrounds",
            True,
            id="should return 'True' if word is isogram"
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
def test_for_right_work_func(
        check_word: str,
        bool_result: bool
) -> None:

    assert is_isogram(check_word) == bool_result
