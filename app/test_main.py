import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param("", True, id="Empty input"),

        pytest.param("qwerty", True, id="lowercase iso"),
        pytest.param("QWERTY", True, id="uppercase iso"),
        pytest.param("qwertqqq", False, id="lowercase not iso"),
        pytest.param("QWERTQQW", False, id="uppercase not iso"),
        pytest.param("QwErtY", True, id="mixed iso"),
        pytest.param("Qweq", False, id="mixed upper-lower not iso"),
        pytest.param("qweQ", False, id="mixed lower-upper not iso")
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:

    assert is_isogram(word) == expected
