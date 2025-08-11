import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "text, expected_output",
    [
        pytest.param("playgrounds", True),
        pytest.param("look", False),
        pytest.param("Adam", False),
        pytest.param("", True),
        pytest.param("r", True),
    ],
    ids=[
        "should return True on unique char in string",
        "should return False on neighboring similar characters",
        "should return False on similar characters",
        "should return True on empty string",
        "should return True on a single character in string",
    ]
)
def test_isogram_verifier(text: str, expected_output: bool) -> None:
    assert is_isogram(text) is expected_output
