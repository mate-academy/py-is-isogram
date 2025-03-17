import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_res",
    [
        pytest.param("playgrounds", True,
                     id="test word without repeating letters"),
        pytest.param("look", False,
                     id="test word with repeating letters"),
        pytest.param("Adam", False,
                     id="test word with big and small letters"),
        pytest.param(" ", True, id="test empty string")
    ]
)
def test_should_return_true_if_word_is_isogram(word: str,
                                               expected_res: bool) -> None:
    assert is_isogram(word) == expected_res
