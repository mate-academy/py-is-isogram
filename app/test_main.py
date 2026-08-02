import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_value",
    [
        ("", True),
        ("look", False),
        ("Wow", False),
        ("damn", True),
        ("MoOn", False),
        ("dangerous", True),
        ("kitty", False),
        ("develop", False)
    ]
)
def test_is_isogram_bool(word: str, expected_value: bool) -> None:
    assert is_isogram(word) == expected_value
