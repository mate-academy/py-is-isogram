from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word_lower,result",
    [
        pytest.param(
            "playgrounds", True,
            id="The test returns True because it is an isogram"
        ),
        pytest.param(
            "", True,
            id="The test returns True because it is an isogram"
        ),
        pytest.param(
            "MM", False,
            id="The test returns False because the text is not an isogram"
        ),
        pytest.param(
            "look", False,
            id="The test returns False because the text is not an isogram"
        ),
        pytest.param(
            "test", False,
            id="The test returns False because the text is not an isogram"
        )

    ]

)
def test_isogram_is_case_insensitive(word_lower: str, result: bool) -> None:
    assert is_isogram(word_lower) == result
