# flake8: noqa: *
import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected", [
        pytest.param("playgrounds", True, id="Default word in lowercase"),
        pytest.param("look", False, id="Word in lowercase with repeating letters"),
        pytest.param("Adam", False, id="Word in different cases with repeating letters"),
        pytest.param("", True, id="Blank word"),
    ]
)
def test_logic_is_isogram(word, expected):
    assert is_isogram(word) == expected
