import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param(
            "Hello",
            False,
        ),
        pytest.param(
            "playgrounds",
            True
        ),
        pytest.param(
            "look",
            False
        ),
        pytest.param(
            "Adam",
            False
        ),
        pytest.param(
            "",
            True
        ),
        pytest.param(
            " ",
            True
        ),
        pytest.param(
            "  ",
            False
        ),
        pytest.param(
            "Aa",
            False
        ),
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert (
        is_isogram(word) == result
    ), f"if word is {word}, the answre should be: {result}"
