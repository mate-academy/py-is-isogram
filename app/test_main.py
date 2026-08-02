import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param(
            "playgrounds",
            True,
            id="function should return 'True' if word has no letter rep"
        ),
        pytest.param(
            "look",
            False,
            id="function should return 'False' if word has letter rep"
        ),
        pytest.param(
            "Adam",
            False,
            id="function should be case sensetive"
        ),
        pytest.param(
            "",
            True,
            id="the empty string is an isogram"
        )
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
