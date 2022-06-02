import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param(
            "playgrounds",
            True,
            id="test for isogram"
        ),
        pytest.param(
            "look",
            False,
            id="test for not isogram"
        ),
        pytest.param(
            "Adam",
            False,
            id="test  for upper case"
        ),
        pytest.param(
            "",
            True,
            id="test for empty string"
        )
    ]
)
def test_is_isogram(word, result):
    assert is_isogram(word) == result
