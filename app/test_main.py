import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_bool_result",
    [
        (
            "", True
        ),
        (
            "qwerty", True
        ),
        (
            "QWERTYqwerty", False
        ),
        (
            "QQ", False
        )
        ,
        (
            "qq", False
        )
    ]
)
def test_is_isogram(
    word: str, expected_bool_result: bool
) -> None:
    assert is_isogram(word) == expected_bool_result
