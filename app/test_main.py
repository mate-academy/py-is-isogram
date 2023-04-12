import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param(
            "playgrounds", True,
            id="function return True"
        ),
        pytest.param(
            "look", False,
            id="function return False"
        ),
        pytest.param(
            "Adam", False,
            id="function is a case insensitive"
        ),
        pytest.param(
            "", True,
            id="empty string should return True"
        )
    ]
)
def test_is_isogram(
        word: str,
        result: bool
) -> None:
    assert (
        is_isogram(word) == result
    )
