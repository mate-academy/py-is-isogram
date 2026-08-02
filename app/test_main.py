from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param(
            "",
            True,
            id="Empty string should be an isogram"
        ),
        pytest.param(
            "playgrounds",
            True,
            id="Unrepeated letters should be an isogram"
        ),
        pytest.param(
            "Admin",
            True,
            id="Unrepeated letters in different case should be an isogram"
        ),
        pytest.param(
            "look",
            False,
            id="Repeated letters should not be an isogram"
        ),
        pytest.param(
            "Adam",
            False,
            id="Repeated letters in different case should not be an isogram"
        ),
    ]
)
def test_word_should_be_isogram(
        word: str,
        expected: bool
) -> None:
    assert is_isogram(word) == expected
