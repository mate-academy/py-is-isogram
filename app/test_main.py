import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("quiz", True, id="Lowercase 'quiz should return True"),
        pytest.param("QUIZ", True, id="Uppercase 'QUIZ' should return True"),
        pytest.param("look", False, id="Lower 'look' should return  False"),
        pytest.param("LOOK", False, id="Upper 'LOOK' should return False"),
        pytest.param("AdaM", False, id="Mixed 'AdaM' should return False"),
        pytest.param("", True, id="Empty string should return True"),
    ],
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) is result


if __name__ == "__main__":
    pytest.main()
