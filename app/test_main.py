from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,expected_is_isogram",
    (
        pytest.param("playgrounds", True, id="test word is isogram"),
        pytest.param("", True, id="test empty string is isogram"),
        pytest.param("ABCDahf", False, id="test diff register is not isogram"),
        pytest.param("0123", True, id="test unique numbers is isogram"),
        pytest.param("01230", False, id="test 01230 is isogram")

    )
)
def test_is_isogram(word: str, expected_is_isogram: bool) -> None:
    assert is_isogram(word) == expected_is_isogram
