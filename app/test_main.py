import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param("", True, id="test empty"),
        pytest.param("word", True, id="test isogram"),
        pytest.param("Mm", False, id="test casesens"),
        pytest.param("m&m", False, id="test non iso"),
    ]
)
def test_variants(word: str, result: bool) -> None:
    assert (is_isogram(word) == result
            ), f"{word} should be equal to {result}"
