import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("", True, id="test empty string"),
        pytest.param("Futaba", False, id="test false and upper letter"),
        pytest.param("k", True, id="test one letter"),
        pytest.param("someone", False, id="test false on lower word"),
        pytest.param("phone", True, id="test simple word for true"),
        pytest.param("MAN", True, id="test upper word"),
        pytest.param("lkfajsdlwerqlwke", False, id="test long word"),
        pytest.param("siuuuuu", False, id="test consecutive repeating letters")
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result


def test_incorrect_value() -> None:
    with pytest.raises(AttributeError):
        is_isogram(1)
