import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "inputted_text, expected",
    [
        pytest.param("playgrounds", True),
        pytest.param("look", False),
        pytest.param("Adam", False),
        pytest.param("", True),
        pytest.param("ambidextrously", True),
        pytest.param("Vivi", False),
        pytest.param("Viv", False),
    ]
)
def test_is_isogram(inputted_text: str, expected: bool) -> None:
    assert is_isogram(inputted_text) == expected
