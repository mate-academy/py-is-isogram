import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "initial_word, result",
    [
        pytest.param(
            "playground ", True,
            id="should return 'True' when  letter in word not repeated"
        ),

        pytest.param(
            "", True,
            id="Should return 'True' when number of letter 1 or 0"
        ),
        pytest.param(
            "look", False,
            id="Should return 'False' when letter in word repeated"
        ),
        pytest.param(
            "Adam", False,
            id="Should return 'False' when letter in word repeated"
        )
    ]
)
def test_corectly_correct_result(initial_word: str, result: bool) -> None:
    assert is_isogram(initial_word) == result


@pytest.mark.parametrize(
    "initial_word",
    [
        pytest.param(1, id="type of 'word' should be str"),
        pytest.param([2], id="type of 'word' should be str")
    ]
)
def test_raised_attribute_error(initial_word: str) -> None:
    with pytest.raises(AttributeError):
        is_isogram(initial_word)
