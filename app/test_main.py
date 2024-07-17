from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, valid_bool",
    [
        pytest.param(
            "", True,
            id="check with empty str"
        ),

        pytest.param(
            "   ", False,
            id="check multiple spaces"
        ),

        pytest.param(
            "m", True,
            id="check with only one letter"
        ),

        pytest.param(
            "mm", False,
            id="check with two equals letters"
        ),

        pytest.param(
            "Zzz", False,
            id="check with three equals letters but in different case"
        ),

        pytest.param(
            "Amur", True,
            id="check valid isogram"
        ),

        pytest.param(
            "adAm", False,
            id="check upper case letter in end of word"
        ),

        pytest.param(
            "abcdefghclmnioprst", False,
            id="check different letters"
        ),
    ]
)
def test_different_solutions(word: str, valid_bool: bool) -> None:
    assert is_isogram(word) == valid_bool
