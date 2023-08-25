import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "string,result",
    [
        pytest.param(
            "playgrounds",
            True,
            id="should return true if the "
               "word don't have any repeating letters",
        ),
        pytest.param(
            "look",
            False,
            id="should return false if the word has two same letters",
        ),
        pytest.param(
            "Adam",
            False,
            id="should return false if there "
               "is two same letters despite case difference",
        ),
        pytest.param("", True, id="should return true if an empty string"),
    ],
)
def test_is_isogram(string, result) -> None:
    assert is_isogram(string) == result
