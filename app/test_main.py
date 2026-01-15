import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "string,result",
    [
        pytest.param("", True, id="String is empty"),
        pytest.param("Odesa", True, id="Good city without extra words"),
        pytest.param("transparent", False, id="Some characters are repeated"),
        pytest.param("GoOdWiN", False, id="Repeated characters and swapcase"),
    ]
)
def test_is_isogram(string: str, result: bool):
    assert is_isogram(string) == result
