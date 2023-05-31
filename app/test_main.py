import pytest
import string

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param(
            "",
            True,
            id="The empty string is isogram"
        ),
        pytest.param(
            string.ascii_letters,
            False,
            id="The function should be case-insensitive"
        ),
        pytest.param(
            (
                string.ascii_lowercase
                + string.digits
                + string.whitespace
                + string.punctuation
            ),
            True,
            id="The function should return True if there is no repeating"
        ),
    ]
)
def test_correct_isogram_check(
        word: str,
        result: bool
) -> None:
    assert is_isogram(word) == result


@pytest.mark.parametrize(
    "word",
    [
        pytest.param(
            None,
            id="input type must be str, not NoneType"
        ),
        pytest.param(
            123,
            id="input type must be str, not int"
        ),
        pytest.param(
            {"None": None},
            id="input type must be str, not dict"
        ),
        pytest.param(
            (1, 2),
            id="input type must be str, not tuple"
        )
    ]
)
def test_correct_input_type(word: str) -> None:
    with pytest.raises(AttributeError):
        is_isogram(word)
