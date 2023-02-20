import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "input_value,expected_result",
    [
        pytest.param(
            "playgrounds",
            True,
            id="should return True if letters don't repeat"
        ),
        pytest.param(
            "look",
            False,
            id="should return False if letters are repeating"
        ),
        pytest.param(
            "Adam",
            False,
            id="should return False with upper-case repeated letters"
        ),
        pytest.param(
            "AdamaAAmDFdf",
            False,
            id="should return False with upper-case repeated letters"
        ),

        pytest.param(
            "",
            True,
            id="should return True is input is empty string"
        ),
    ]
)
def test_is_isogram_with_different_inputs(
        input_value: str,
        expected_result: bool
) -> None:
    assert is_isogram(input_value) == expected_result


def test_is_isogram_raises_errors() -> None:
    with pytest.raises(AttributeError):
        is_isogram(123)
