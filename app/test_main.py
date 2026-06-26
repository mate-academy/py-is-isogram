import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param(
            "playgrounds", True,
            id="test isogram word"
        ),
        pytest.param(
            "look", False,
            id="test not an isogram word"
        ),
        pytest.param(
            "Adam", False,
            id="test word with different cases"
        ),
        pytest.param(
            "", True,
            id="test empty string is isogram"
        )
    ]
)
def test_should_return_correct_answer(
        word: str,
        expected: bool
) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize(
    "word",
    [
        pytest.param(
            "2",
            id="test should raise exception if input is numeric"),
        pytest.param(
            "[}--abc",
            id="test should raise exception if input has special symbols"
        )
    ]
)
def test_should_raise_exception_if_input_is_not_a_word(word: str) -> None:
    with pytest.raises(ValueError):
        is_isogram(word)
