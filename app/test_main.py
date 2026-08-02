import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param(
            "playgrounds",
            True,
            id="should return True when word is isogram in lower case"
        ),
        pytest.param(
            "PLAYGROUNDS",
            True,
            id="should return True when word is isogram in upper case"
        ),
        pytest.param(
            "Playgrounds",
            True,
            id="should return True when word is isogram in mixed case"
        ),
        pytest.param(
            "",
            True,
            id="should return True when word is an empty string"
        ),
        pytest.param(
            "look",
            False,
            id="should return False when letter occurred more then once"
        ),
        pytest.param(
            "Adam",
            False,
            id="should return False when the same letter in different cases"
        )
    ]
)
def test_get_correct_result(word: str, result: bool) -> None:
    assert is_isogram(word) == result


def test_should_raise_typeerror_if_func_get_incorrect_data() -> None:
    with pytest.raises(AttributeError):
        is_isogram(10)
