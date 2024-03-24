from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "isogram, result",
    [
        ("", True),
        ("wash", True),
        ("see", False),
        ("COMPUTER", True),
        ("SCISSORS", False),
        ("plEase", False)
    ]
)
def test_isograms_return_true(isogram: str, result: bool) -> None:
    assert is_isogram(isogram) is result
