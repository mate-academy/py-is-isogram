import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_value",
    [
        pytest.param(
            "",
            True,
            id="empty string is isogram"),
        pytest.param(
            "noob",
            False,
            id="two 'o' in 'noob"),
        pytest.param(
            "Check",
            False,
            id="function should work with lower and upper case"),
        pytest.param(
            "playgrounds",
            True,
            id="playgrounds is isogram"),
        pytest.param(
            "qwertyuiopasdfghjklzxcvbnm",
            True,
            id="long string case")
    ]
)
def test_is_isogram(word: str, expected_value: bool) -> None:
    assert is_isogram(word) == expected_value
