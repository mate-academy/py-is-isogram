from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "string,bool_value",
    [
        ("", True),
        ("Adam", False),
        ("look", False)
    ],
    ids=[
        "should return True, when str ia empty",
        "should return False, when words repeats in different cases",
        "should return False, when words repeats"
    ]
)
def test_with_no_word(string: str, bool_value: bool) -> None:
    assert is_isogram(string) is bool_value
