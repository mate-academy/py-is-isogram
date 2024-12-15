from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected_data",
    [
        pytest.param(
            "",
            True,
            id="the empty string is an isogram"
        ),
        (
            "playgrounds",
            True
        ),
        (
            "look",
            False
        ),
        (
            "Adam",
            False
        ),
    ]
)
def test_check_data_correctly(word : str,
                              expected_data: bool) -> None:
    assert is_isogram(word) == expected_data
