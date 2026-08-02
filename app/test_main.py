import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
    ],
    ids=[
        "empty string is isogram",
        "isogram should return True",
        "not isogram should return False",
        "function should be case sensitive",
    ]
)
def test_is_isogram_work_corect(word: str,
                                expected_result: bool
                                ) -> None:
    assert is_isogram(word) == expected_result
