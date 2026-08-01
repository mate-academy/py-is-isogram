import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param(
            "",
            True,
            id="should return 'True' for empty string"
        ),
        pytest.param(
            "look",
            False,
            id="should return 'False' if there is two same letters in a row"
        ),
        pytest.param(
            "Adam",
            False,
            id="should return 'False' if there is two same letters in the word"
        ),
        pytest.param(
            "playgrounds",
            True,
            id="should return 'True' if there is no same letters in the word"
        )
    ]
)
def test_should_return_correct_result(
        word: str,
        result: bool
) -> None:
    assert is_isogram(word) == result


@pytest.mark.parametrize(
    "word,expected_error",
    [
        pytest.param(
            None,
            ValueError,
            id="should raise 'ValueError' if word type is 'None'"
        ),
        pytest.param(
            123,
            TypeError,
            id="should raise 'TypeError' if word type is wrong"
        ),
        pytest.param(
            True,
            TypeError,
            id="should raise 'TypeError' if word type is wrong"
        )
    ]
)
def test_should_raise_correct_error(
        word: str,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        is_isogram(word)
