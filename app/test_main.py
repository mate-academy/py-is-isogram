import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        pytest.param(
            "",
            True,
            id="True if empty string"
        ),
        pytest.param(
            "playgrounds",
            True,
            id="True if no the same letters"
        ),
        pytest.param(
            "Playgrounds",
            True,
            id="True if no the same letters with uppercase"
        ),
        pytest.param(
            "look",
            False,
            id="False if the same letters"
        ),
        pytest.param(
            "Adam",
            False,
            id="False if the same letters with uppercase"
        ),
    ]
)
def test_should_return_correct_result(
        word: str, expected_result: bool
) -> None:
    assert is_isogram(word) == expected_result
