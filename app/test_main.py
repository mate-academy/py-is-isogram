import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word", [("love"), ("eviIl"), ("qwertyu")])
def test_return_boolean(word: str) -> None:
    assert isinstance(is_isogram(word), bool), "Function must return boolean"


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("love", True, id="word is love"),
        pytest.param("eviIl", False, id="word is eviIl"),
        pytest.param("Qwertyu", True, id="word is Qwertyu"),
        pytest.param("QwErtyu", True, id="word is QwErtyu"),
        pytest.param("eErtyu", False, id="word is eErtyu"),
        pytest.param("erEtyeu", False, id="word is erEtyeu"),
        pytest.param("", True, id="word is empty string"),
    ],
)
def test_return_result(word: str, result: bool) -> None:
    assert is_isogram(word) == result, f"Function must return {result}"


@pytest.mark.parametrize("word", [(3), (["word"])])
def test_raise_attributeerror(word: str) -> None:
    with pytest.raises(AttributeError):
        is_isogram(word)
