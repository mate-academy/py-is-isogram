from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param("playgrounds", True, id="test 1"),
        pytest.param("look", False, id="test 2"),
        pytest.param("Adam", False, id="test 3"),
        pytest.param("", True, id="empty text test"),
    ],

)
def test_is_isogram(word: str,
                    result: bool,
                    ) -> None:
    assert is_isogram(word) == result
