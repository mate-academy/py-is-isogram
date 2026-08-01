import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "isogram, excepts",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_is_isogram_text(isogram: str, excepts: bool) -> None:
    assert is_isogram(isogram) == excepts
