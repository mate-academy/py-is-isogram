from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("", True, id="Empty string"),
        pytest.param(" ", True, id="Empty string"),
        pytest.param(
            "Adam",
            False,
            id="Upper and lower case chars in string"
        ),
        pytest.param("look", False, id="Same chars"),
        pytest.param("playgrounds", True, id="Isogram word"),
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
