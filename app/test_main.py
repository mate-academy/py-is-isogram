import pytest
from app.main import is_isogram


# write your code here
@pytest.mark.parametrize(
    "word, status",
    [
        ("", True),
        ("abs", True),
        ("Aa", False),
        ("aa", False),
        ("absA", False)
    ]
)
def test_is_isogram(word: str, status: bool) -> None:
    assert is_isogram(word) == status
