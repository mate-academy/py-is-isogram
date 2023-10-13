import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param(
            "playgrounds",
            True,
            id="lowercase input word"
        ),
        pytest.param(
            "PlayGrounds",
            True,
            id="input word with uppercase letters"
        ),
        pytest.param(
            "",
            True,
            id="empty string is isogram"
        ),
        pytest.param(
            "appear",
            False,
            id="input string with repeated letter P"
        ),
        pytest.param(
            "Edward",
            False,
            id="input string with repeated letter D and one uppercase letter"
        )
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
