import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "word, isogram",
    [
        pytest.param(
            "playgrounds", True,
            id="playgrounds is True"
        ),
        pytest.param(
            "look", False,
            id="look is False"
        ),
        pytest.param(
            "Adam", False,
            id="Adam is False"
        ),
        pytest.param(
            "", True,
            id="empty string is True"
        ),

    ]
)
def test_is_isogram(word: str, isogram: bool) -> None:
    assert is_isogram(word) == isogram
