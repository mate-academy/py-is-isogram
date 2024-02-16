import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param("qwertyuiop", True,
                     id="Should return true for qwertyuiop word"),
        pytest.param("asdfghjkl", True,
                     id="Should return true for asdfghjkl word"),
        pytest.param("zxcvbnm", True,
                     id="Should return true for zxcvbnm word"),
        pytest.param("", True,
                     id="Should return true for empty word")
    ]
)
def test_should_return_true(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param("rruujhjh", False,
                     id="Is not isogram"),
        pytest.param("wwwww", False,
                     id="Is not isogram"),
        pytest.param("qqqqqqqq", False,
                     id="Is not isogram")
    ]
)
def test_should_return_false(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
