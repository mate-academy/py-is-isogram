import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_result",
    [
        pytest.param(
            "playgrounds", True,
            id="test if word is 'playgrounds'"
        ),
        pytest.param(
            "look", False,
            id="test if word is 'look'"
        ),
        pytest.param(
            "Adam", False,
            id="test if word is 'Adam'"
        ),
        pytest.param(
            "", True,
            id="test if word is empty"
        )
    ]
)
def test_correct_return(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
