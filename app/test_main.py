import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        pytest.param(
            "playgrounds",
            True,
            id="it is not an isogram."),
        pytest.param(
            "",
            True,
            id="Empty string is an isogram."),
        pytest.param(
            "Adam",
            False,
            id="Not only consecutive letters are not an isogram."),
        pytest.param(
            "look",
            False,
            id="Not only non-consecutive letters are not an isogram."),

    ]
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
