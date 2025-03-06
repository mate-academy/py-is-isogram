import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "string,result",
    [
        pytest.param(
            "",
            True,
            id=("when strimg is empty")
        ),
        pytest.param(
            "playgrounds",
            True,
            id=("when string is isogram")
        ),
        pytest.param(
            "look",
            False,
            id=("when string is not isogram")
        ),
        pytest.param(
            "Adam",
            False,
            id=("when one letter is upper-case")
        )
    ]
)
def test_of_is_isogram(string: str, result: bool) -> None:
    assert (
        is_isogram(string) == result
    )
