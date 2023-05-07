import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param("", True, id="test empty string"),
        pytest.param("text", False, id="test not isogram"),
        pytest.param("playgrounds", True, id="test isogram"),
        pytest.param("Mm", False, id="test caps")
    ]
)
def test_isogram(word: str, result: bool) -> None:
    assert (is_isogram(word) == result
            ), f"{word} is isogram == {result}"
