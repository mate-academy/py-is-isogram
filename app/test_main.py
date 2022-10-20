from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "string, expected",
    [
        pytest.param("playgrounds", True, 
                     id="should return 'True' for isogram"),
        pytest.param("look", False, 
                     id="should return 'False' for not isogram"),
        pytest.param("Adam", False, id="should be case-insensitive"),
        pytest.param("", True, id="empty string should be isogram")
    ]
)
def test_is_isogram_results_are_correct(string: str,
                                        expected: bool) -> None:
    assert is_isogram(string) == expected
