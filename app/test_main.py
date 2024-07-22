import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        pytest.param("playgrounds", True, id="should return True for isogram"),
        pytest.param(
            "Adam",
            False,
            id="should return False for letters with different cases",
        ),
        pytest.param("", True, id="should return True for empty string"),
        pytest.param("aaa", False, id="should return False for consecutive letters"),
    ],
)
def test_should_return_correct_results(
    word: str, expected_result: bool
) -> None:
    assert is_isogram(word) == expected_result
