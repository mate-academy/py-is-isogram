import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param(
            "",
            True,
            id="should return the wright result: True"
        ),
        pytest.param(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            True,
            id="should return the wright result: True"
        ),
        pytest.param(
            "abcdefghijklmnopqrstuvwxyz",
            True,
            id="should return the wright result: True"
        ),
        pytest.param(
            "abcfea",
            False,
            id="should return the wright result: False"
        ),
        pytest.param(
            "seAbcdat",
            False,
            id="should return the wright result: False"
        ),
        pytest.param(
            "acntrSSlo",
            False,
            id="should return the wright result: False"
        ),
    ]
)
def test_calculation_correctly(
        word: int,
        result: bool
) -> None:
    assert is_isogram(word) == result
