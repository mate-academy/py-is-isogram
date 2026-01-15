import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param(
            "HeLlo",
            False,
            id="test should return False for `HeLlo`"
        ),
        pytest.param(
            "lumberjacks",
            True,
            id="test should return True for `lumberjacks`"
        ),
        pytest.param(
            "loving",
            True,
            id="test should return True for `loving`"
        ),
        pytest.param(
            " Jam ",
            False,
            id="test should return False for `Jam `"
        ),
        pytest.param(
            "",
            True,
            id="test should return True for empty string"
        )
    ]
)
def test_func_should_correctly_return_result(word: str, result: bool) -> bool:
    assert is_isogram(word) == result
