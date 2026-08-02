import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param("", True, id="When word is given empty string"),
        pytest.param("playgrounds", True, id="When word is isogram"),
        pytest.param("look", False, id="When word is not isogram"),
        pytest.param(
            "Ozone", False, id="When word has same upper and lowercase letters"
        ),
    ]
)
def test_func_should_return_the_right_result(word: str, result: bool) -> None:
    assert is_isogram(word) == result
