from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param(
            "playgrounds", True,
            id="The test returns True because it is an isogram"
        ),
        pytest.param(
            "look", False,
            id="The test returns False because the text is not an isogram"
        ),
        pytest.param(
            "Aa", False,
            id="The test returns False because the text is not an isogram"
        ),
        pytest.param(
            "aA", False,
            id="The test returns False because the text is not an isogram"
        ),
        pytest.param(
            "", True,
            id="Test returns True because is an isogram (empty string)"
        )
    ]

)
def test_is_isogram(word, result):
    assert is_isogram(word) is result
