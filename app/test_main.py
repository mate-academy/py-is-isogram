import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "check_word,bool_result",
    [
        pytest.param(
            "",
            True,
            id="should return 'True' if value is empty string"
        ),
        pytest.param(
            "playgrounds",
            True,
            id="should return 'True' if word is isogram"
        ),
        pytest.param(
            "look",
            False,
            id="should return 'False' if word is not isogram"
        ),
        pytest.param(
            "Iphone",
            True,
            id="function should be case-insensitive"
        ),
        pytest.param(
            "abcd",
            False,
            id="not only consecutive letters are not an isogram."
        )
    ]
)
def test_for_right_work_func(
        check_word: str,
        bool_result: bool
) -> None:

    assert is_isogram(check_word) == bool_result
