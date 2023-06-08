import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "initial_input, expected_result",
    [
        pytest.param(
            'playgrounds',
            True,
            id="check parameter without repetition"
        ),
        pytest.param(
            'look',
            False,
            id="check parameter with repetition"
        ),
        pytest.param(
            'Adam',
            False,
            id="check parameter with upper repetition"
        ),
        pytest.param(
            '',
            True,
            id="check parameter with empty string"
        )
    ]
)
def test_modify_isogram(initial_input, expected_result):
    assert is_isogram(initial_input) == expected_result


@pytest.mark.parametrize(
    "initial_error, expected_error",
    [
        pytest.param(
            1,
            AttributeError,
            id="should raise error when parameter no equal type of string"
        )
    ]
)
def test_raising_error_correctly(initial_error, expected_error):
    with pytest.raises(expected_error):
        is_isogram(initial_error)
