import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_value",
    [
        ("", True),
        ("BEe", False),
        ("Sphere", False)


    ],
    ids=[
        "should return True if word is empty string",
        "is_isogram should be case insensitive",
        "should return False if same letters non-consecutive"
    ]

)
def test_is_isogram(word: str, expected_value: bool) -> None:
    assert is_isogram(word) == expected_value
