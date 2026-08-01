import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result,exception",
    [
        ("playgrounds", True, None),
        ("look", False, None),
        ("Adam", False, None),
        ("", True, None)
    ],
    ids=[
        "'playgrounds is isogram'",
        "'look' is not isogram",
        "'Adam' with capitalize letter is not isogram",
        "Empty string considers isogram"
    ]
)
def test_is_isogram_function(word: str,
                             result: bool,
                             exception: Exception) -> None:
    assert (
        is_isogram(word) == result
    ), f"{word} should be {result}"
