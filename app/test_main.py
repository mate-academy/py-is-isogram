from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "test_str, get_is_isogram_res",
    [
        pytest.param(
            "playgrounds",
            True,
            id="there are no repeating letters in the word"
        ),
        pytest.param(
            "look",
            False,
            id="in a word in a word we have a repetition of letters"
        ),
        pytest.param(
            "Adam",
            False,
            id="different cases of one letter is a repetition"
        ),
        pytest.param(
            "",
            True,
            id="empty string is isogram"
        )
    ]
)
def test_checking_correct_results(
        test_str: str,
        get_is_isogram_res: bool
) -> None:
    goals = is_isogram(test_str)
    assert goals == get_is_isogram_res
