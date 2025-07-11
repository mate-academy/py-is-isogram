import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "string,result",
    [
        pytest.param("", True, id="empty-string"),
        pytest.param("playgrounds", True, id="isogram-lowercase"),
        pytest.param("look", False, id="repeating-o"),
        pytest.param("Adam", False, id="repeating-a-different-case"),
        pytest.param("AAmre", False, id="repeating-uppercase-a"),
        pytest.param(
            "AAmeremaflasgiwda",
            False,
            id="repeating-more-than-one-character"
        ),
        pytest.param(
            "abcdefghijklmnopqrstuvwxyz",
            True,
            id="all-unique-letters"
        )
    ]
)
def test_is_isogram(string: str, result: bool) -> None:
    assert is_isogram(string) == result
