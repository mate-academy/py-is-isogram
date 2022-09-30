from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,expected_bool",
    [
        pytest.param(
            "", True,
            id="if word is empty should return True"
        ),
        pytest.param(
            "ABCabc", False,
            id="if word has different cases of the same letter return False"
        ),
        pytest.param(
            "umbrella", False,
            id="Not only consecutive letters are not an isogram"
        ),
        pytest.param(
            "lamBo", True,
            id="func should be case-insensitive"
        ),
        pytest.param(
            "uncopyrightable", True,
            id="should return True if some all letters different"
        ),

    ]
)
def test_should_return_expected_error(word, expected_bool):
    assert is_isogram(word) == expected_bool
