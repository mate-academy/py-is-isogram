import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "incoming_string,boolean_result",
    [
        pytest.param(
            "",
            True,
            id="empty string should return True"
        ),
        pytest.param(
            "Adam",
            False,
            id="letters are repeated in 'Adam'"
        ),
        pytest.param(
            "look",
            False,
            id="letters are repeated in 'look'"
        ),
        pytest.param(
            "playgrounds",
            True,
            id="'playgrounds' is isogram"
        ),
        pytest.param(
            "qwertyuioplkjhgfdsazxcvbnm",
            True,
            id="'qwertyuioplkjhgfdsazxcvbnm' is isogram"
        ),
    ]
)
def test_is_isogram(incoming_string: str, boolean_result: bool) -> None:
    assert is_isogram(incoming_string) == boolean_result
