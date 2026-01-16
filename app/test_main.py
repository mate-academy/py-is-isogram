import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "input_letters, expected_bool",
    [
        pytest.param(
            "word",
            True,
            id="should return correct result for isometric: 'word'"
        ),
        pytest.param(
            "banana",
            False,
            id="should return correct result for not isometric: 'banana'"
        ),
        pytest.param(
            "mEdicIne",
            False,
            id="should not be case sensitive: 'mEdicIne'"
        ),
        pytest.param(
            "",
            True,
            id="should return correct result for empty string"
        ),
        pytest.param(
            "Joke cuz tar",
            False,
            id="should return False if more then one space"
        ),
        pytest.param(
            "DOOM",
            False,
            id="should return correct result for "
               "non-isometric, consecutive: 'DOOM'"
        )
    ]
)
def test_correct_answers(
        input_letters: str,
        expected_bool: bool
) -> None:

    result = is_isogram(input_letters)

    assert result == expected_bool
