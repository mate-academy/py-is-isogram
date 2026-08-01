import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param(
            "",
            True,
            id="empty string"
        ),
        pytest.param(
            "playgrounds",
            True,
            id="isogram word"
        ),
        pytest.param(
            "look",
            False,
            id="not isogram word"
        ),
        pytest.param(
            "Adam",
            False,
            id="case-insensitive"
        ),
        pytest.param(
            "a",
            True,
            id="one letter"
        ),
        pytest.param(
            "aaaa",
            False,
            id="all same letters"
        )
    ]
)
def test_identify_isograms_correctly(
        word: str,
        expected: bool
) -> None:
    assert is_isogram(word) == expected
