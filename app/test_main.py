import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "fraze,bool_type",
    [
        ("", True),
        ("playgrounds", True),
        ("PlaYgrOuNdS", True),
        ("look", False),
        ("Adam", False),
        (" playgrounds", True),
        (" playgrounds ", False),
        ("playgrounds!", True),
        ("*playgrounds?", True),
        ("$playgrounds$", False),
    ],)
def test_check_is_isogra(fraze: str, bool_type: bool) -> None:
    assert is_isogram(fraze) == bool_type
