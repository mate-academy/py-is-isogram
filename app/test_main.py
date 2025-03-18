from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected_result",
    [
        pytest.param(
            "Bober",
            False,
            id="Bober, expected False",
        ),
        pytest.param(
            "car",
            True,
            id="Car, expected True",
        ),
        pytest.param(
            "mustang",
            True,
            id="Mustang, expected True",
        ),
        pytest.param(
            "",
            True,
            id="Empty, expected True",
        ),
        pytest.param(
            "Copper",
            False,
            id="Copper, expected False",
        )
    ]
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
