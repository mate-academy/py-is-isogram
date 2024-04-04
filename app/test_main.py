import pytest


from app.main import is_isogram


@pytest.mark.parametrize("test_input, expected", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("Moment", False),
    ("", True)
])
def test_is_isogram(test_input: str, expected: bool) -> None:
    if isinstance(test_input, str):
        assert is_isogram(test_input) == expected
