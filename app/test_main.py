from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, bool_result",
    [
        ("", True),
        ("application", False),
        ("Girl", True),
        ("boOl", False),
        ("remove", False)
    ]
)
def test_all(
        word: str,
        bool_result: bool
) -> None:
    assert is_isogram(word) is bool_result
