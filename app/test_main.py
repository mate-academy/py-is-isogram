from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, bool_result",
    [
        pytest.param(
            'playgrounds', True,
            id="should return 'True' if word is isogram"
        ),
        pytest.param(
            'look', False,
            id="should return 'False' if word is not isogram"
        ),
        pytest.param(
            'Adam', False,
            id="should return 'False' if word is not isogram"
        ),
        pytest.param(
            '', True,
            id="should return 'True' if word is empty"
        ),
    ]
)
def test_is_isogram(word: str, bool_result: bool) -> None:
    assert is_isogram(word) == bool_result
