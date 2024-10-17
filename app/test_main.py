import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "input_string,result",
    [
        pytest.param(
            "THE stRing",
            False,
            id="with UPPERcase and with 2 t"
        ),
        pytest.param(
            ".....",
            False,
            id="with points"
        ),
        pytest.param(
            "./0184=-bsdjA,#@ *",
            True,
            id="with different non-consecutive values"
        ),
        pytest.param(
            " ",
            True,
            id="with only one space"
        ),
        pytest.param(
            "",
            True,
            id="with empty string"
        ),
        pytest.param(
            "RUN",
            True,
            id="with upper non-consecutive word"
        ),
        pytest.param(
            "people",
            False,
            id="with lower consecutive word"
        )
    ]
)
def test_consecutive_or_non_consecutive_string(
        input_string: str,
        result: bool
) -> bool:
    assert is_isogram(input_string) == result
