import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        pytest.param(
            "playgrounds", True,
            id="returns True if all letters in the word are different"
        ),
        pytest.param(
            "look", False,
            id="returns False if some letters are repeated"
        ),
        pytest.param(
            "Adam", False,
            id="returns False if the word has the same "
               "uppercase and lowercase letters"
        ),
        pytest.param(
            "", True,
            id="returns True if an empty string is passed"
        )
    ]
)
def test_whether_the_word_is_an_isogram(
        word: str,
        expected_result: bool
) -> None:
    assert is_isogram(word) == expected_result
