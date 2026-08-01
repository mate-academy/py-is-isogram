from typing import Any

import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param(
            "qwertyuiopasdfghjkl",
            True,
            id="Some issue with counting letters"
        ),
        pytest.param("look",
                     False,
                     id="Should return False for not isogram"),
        pytest.param("a",
                     True,
                     id="Should return True for one letters"),
        pytest.param("aaa",
                     False,
                     id="Should return False for consecutive letters"),
        pytest.param("",
                     True,
                     id="Should return True for empty line"),
        pytest.param("AbCdEfGi",
                     True,
                     id="Should work with different case"),
        pytest.param("qwer tyuiod fgh",
                     False,
                     id="Multiply spaces can't be isogram")
    ]
)
def test_should_work_with_different_words(
        word: str,
        result: bool
) -> None:
    assert is_isogram(word) is result


@pytest.mark.parametrize(
    "word",
    [1, [1, "s"], True],
    ids=["int type", "list type", "bool type"]
)
def test_should_raise_error_with_incorrect_types(word: Any) -> None:
    with pytest.raises(AttributeError):
        is_isogram(word)
