import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, true_false",
    [
        pytest.param(
            "playgrounds", True,
            id="True when word has no repeating letters"
        ),
        pytest.param(
            "Dad", False,
            id="False when word has repeating letters"
        ),
        pytest.param(
            "", True,
            id="True when string is empty"
        )
    ]
)
def test_is_isogram_correctly(word: str, true_false: bool) -> None:
    assert is_isogram(word) == true_false


@pytest.mark.parametrize(
    "word, excepted_error",
    [
        pytest.param(
            13, AttributeError,
            id="should raise error when incorrect type"
        )
    ]
)
def test_raise_error_correctly(word: str, excepted_error: type) -> None:
    with pytest.raises(excepted_error):
        is_isogram(word)
