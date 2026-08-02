import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "input_word,expected_result",
    [
        pytest.param("word", True),
        pytest.param("WORD", True),
        pytest.param("wORd", True),
        pytest.param("again", False),
        pytest.param("AGAIN", False),
        pytest.param("aGAIn", False),
        pytest.param("hello", False),
        pytest.param("", True)
    ]
)
def test_is_isogram_correct(input_word: str, expected_result: bool) -> None:
    assert is_isogram(input_word) == expected_result
