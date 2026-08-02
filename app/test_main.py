import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "string,result",
    [
        pytest.param("playgrounds", True, id="no repeated letters"),
        pytest.param("look", False, id="there are repeated letters"),
        pytest.param("Adam", False, id=("there are repeated "
                                        "letters with Upper Case")),
        pytest.param("", True, id="empty string is isogram"),
    ]
)
def test_is_isogram(string: str, result: bool) -> None:
    assert is_isogram(string) == result
