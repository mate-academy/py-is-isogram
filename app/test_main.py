from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "words, result",
    [
        ("", True),
        ("adda", False),
        ("WhaTsup", True),
        ("WarwAR", False),

    ],
    ids=[
        "Empty string should return True",
        "Word 'adda' should return False",
        "Word 'WhaTsup' should return True",
        "Word 'WarwAR' should return False"
    ]
)
def test_is_isogram(words: str, result: bool) -> None:
    assert is_isogram(words) == result
