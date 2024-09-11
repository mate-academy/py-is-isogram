import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "input_word,expected_bool",
    [
        pytest.param(
            "playgrounds", True,
            id="should be True if every letters is different",
        ),
        pytest.param(
            "look", False,
            id="should be False if least one of letter dublicated",
        ),
        pytest.param(
            "Adam", False,
            id="should be False with case-sensetive word \
                and letters dublicate",
        ),
        pytest.param(
            "", True,
            id="should be True for empty word",
        ),
    ]
)
def test_is_isogram(input_word: str, expected_bool: bool) -> None:
    assert is_isogram(input_word) == expected_bool
