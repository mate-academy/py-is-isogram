from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "text, expected_result",
    [
        ("playgrounds", True),
        ("hello", False),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Ukraine", True),
        ("Yehor", True),
        ("macbook", False),
        ("PyThOn", True),
        ("language", False),
    ]
)
def test_is_isogram(text: str, expected_result: bool) -> None:
    assert is_isogram(text) == expected_result
