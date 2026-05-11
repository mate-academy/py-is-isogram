import pytest
import app.main as main


@pytest.mark.parametrize(
    "word, expected",
    [
        ("something", True),
        ("football", False),
        ("Anna", False),
        ("", True)
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert main.is_isogram(word) == expected
