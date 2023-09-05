import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "input_data, expected_data",
    [
        pytest.param("playgrounds", True),
        pytest.param("", True),
        pytest.param("Play", True),
        pytest.param("look", False),
        pytest.param("Adam", False)
    ],
    ids=[
        "words contains only letter",
        "check if empty string is an isogram",
        "check if the function is case-insensitive",
        "check if letter repeated in word",
        "check if letter repeated in word"
    ]
)
def test_check_input_data(input_data: str, expected_data: bool) -> None:
    assert is_isogram(input_data) == expected_data
