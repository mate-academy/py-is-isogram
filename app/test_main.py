import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "string,bool_result",
    [
        pytest.param(
            "", True,
            id="str could be empty"
        ),
        pytest.param(
            "look", False,
            id="Cannot be duplicates"
        ),
        pytest.param(
            "Adam", False,
            id="Cannot be upper case"
        ),
        pytest.param(
            "playground", True,
            id="All letters must be uniq and no duplicating"
        )
    ]
)
def test_uniq_letters(string: str, bool_result: bool) -> None:
    assert is_isogram(string) == bool_result
