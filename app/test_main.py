import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("playgrounds", True, id="Lowercase isogram"),
        pytest.param("PLAYGROUNDS", True, id="Uppercase isogram"),
        pytest.param("look", False, id="Lowercase not isogram"),
        pytest.param("LOOK", False, id="Uppercase not isogram"),
        pytest.param("AdUlT", True, id="Mixed case isogram"),
        pytest.param("AdaM", False, id="Mixed case not isogram"),
        pytest.param("", True, id="Empty string isogram"),
    ],
)
def test_is_isogram(word: str, result: bool) -> None:
    """
    Test the is_isogram function with various inputs and expected results.
    """
    assert is_isogram(word) is result


if __name__ == "__main__":
    pytest.main()
