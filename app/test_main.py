import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("PLAY", True),
        ("lOoK", False),
        (" ", True),
        ("", True),
        ("two words", False)
    ],
    ids=[
        "check lowercase true statement",
        "check lowercase false statement",
        "check Uppercase true statement",
        "check Randomcase false statement",
        "check whitespace true statement",
        "check empty string true statement",
        "check two words false statement"
    ]
)
def test_standart_queries(word: str, result: bool) -> None:
    assert is_isogram(word) == result
