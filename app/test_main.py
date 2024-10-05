import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param(
            "", True, id="the empty string is an isogram"
        ),
        pytest.param(
            "playgrounds", True, id="word `playgrounds` is a isogram"
        ),
        pytest.param(
            "Adam", False, id="function should be case-insensitive"
        ),
        pytest.param(
            "look", False, id="word should has no repeating letters"
        )

    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result


@pytest.mark.parametrize(
    "word, expected_error",
    [
        pytest.param(
            5, AttributeError, id="raise AttributeError when value not string"
        )
    ]
)
def test_is_isogram_invalid_input(
        word: str,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        is_isogram(word)
