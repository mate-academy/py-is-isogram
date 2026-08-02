from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    ("word", "expected_boolean"),
    [
        pytest.param(
            "",
            True,
            id="empty string should me an isogram"
        ),
        pytest.param(
            "zephyr",
            True,
            id="zephyr is an isogram"
        ),
        pytest.param(
            "symphony",
            False,
            id="repeated non-consecutive letters are not an isogram"
        ),
        pytest.param(
            "puzzled",
            False,
            id="repeated consecutive and "
               "different cases letters are not an isogram"
        ),
        pytest.param(
            "Bumble",
            False,
            id="different cases of the same letter is not an isogram"
        )
    ]
)
def test_word_is_isogram(word: str, expected_boolean: bool) -> None:
    assert is_isogram(word) == expected_boolean
