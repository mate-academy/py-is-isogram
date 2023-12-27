import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "test_word,expected_result",
    [
        pytest.param(
            "MOTHER", True, id="Testing isogram with uppercase letters"
        ),
        pytest.param(
            "father", True, id="Testing isogram with lowercase letters"
        ),
        pytest.param(
            "sister", False, id="Testing not isogram with lowercase letters"
        ),
        pytest.param(
            "BrotheR", False, id="Testing not isogram with uppercase letters"
        ),
        pytest.param(
            "", True, id="Testing isogram with no letters"
        ),
        pytest.param(
            "au nt", True, id="Testing isogram with space in word"
        ),
        pytest.param(
            "assert", False, id="Testing not isogram with consecutive letters"
        )
    ]
)
def test_is_isogram_function(test_word: str, expected_result: bool) -> None:
    assert is_isogram(test_word) == expected_result
