import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param(
            "", True, id="Empty input"
        ),
        pytest.param(
            "playgrounds", True, id="all unique letters"
        ),
        pytest.param(
            "unique", False, id="repeat 'u'"
        ),
        pytest.param(
            "Unique", False, id="repeat 'u'"
        ),
        pytest.param(
            "Unilet", True, id="upper case"
        ),
        pytest.param(
            "subdermatoglyphic", True, id="long correct word"
        ),
        pytest.param(
            "aaaaaa", False, id="all same letters"
        )
    ]
)
def test_is_isogram(
        word: str,
        expected: bool
) -> None:
    assert is_isogram(word) is expected
