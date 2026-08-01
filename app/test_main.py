import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param("", True, id="empty string should be True"),
        pytest.param("j", True, id="one letter should be True"),
        pytest.param(
            "bB",
            False,
            id="two equal letters with different case should be False",
        ),
        pytest.param(
            "look", False, id="equal letters in a word should be False"
        ),
        pytest.param(
            "PlayGrounds", True, id="'PlayGrounds' word should be True"
        ),
        pytest.param("ZzaPper", False, id="'ZzaPper' word should be False"),
        pytest.param("damAge", False, id="'damAge' word should be False"),
    ],
)
def test_with_different_params(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize(
    "data, exception",
    [
        pytest.param(
            [],
            AttributeError,
            id="should raise AttributeError if data is list",
        ),
        pytest.param(
            123,
            AttributeError,
            id="should raise AttributeError if data is integer",
        ),
        pytest.param(
            None, AttributeError, id="should raise AttributeError if no data"
        ),
    ],
)
def test_without_params(
    data: list | int | None, exception: type[Exception]
) -> None:
    with pytest.raises(exception):
        is_isogram(data)
