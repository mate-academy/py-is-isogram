import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param(
            "", True,
            id="Empty string is an isogram",
        ),
        pytest.param(
            "playgrounds", True,
            id="'playgrounds' is an isogram",
        ),
        pytest.param(
            "look", False,
            id="'look' is not an isogram",
        ),
        pytest.param(
            "Adam", False,
            id="'Adam' is not an isogram",
        ),
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
