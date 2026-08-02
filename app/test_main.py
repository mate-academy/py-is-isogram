import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_result",
    (
        pytest.param(
            "",
            True,
            id="should return True when word is an empty string"
        ),
        pytest.param(
            "playgrounds",
            True,
            id="should return True when word='playgrounds'"
        ),
        pytest.param(
            "cooking",
            False,
            id="should return False when word='cooking'"
        ),
        pytest.param(
            "Adam",
            False,
            id="should return False when word='Adam'"
        ),
    )
)
def test_is_isogram(word: str, expected_result: bool):
    assert is_isogram(word) == expected_result
