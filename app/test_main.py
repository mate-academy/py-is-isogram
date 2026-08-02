import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word_for_check,expected_result",
    [
        pytest.param(
            "playgrounds", True,
            id="isogram can be not consecutive"
        ),
        pytest.param(
            "Adam", False,
            id="isogram can be not consecutive"
        ),
        pytest.param(
            "", True,
            id="isogram can be not consecutive"
        ),
        pytest.param(
            "looK", False,
            id="isogram can be not consecutive"
        )
    ]
)
def test_isogram_can_be_not_consecutive(
        word_for_check: str,
        expected_result: bool
) -> None:
    assert is_isogram(word_for_check) == expected_result
