from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected_result",
    [
        pytest.param("", True,
                     id="The empty string is an isogram"),
        pytest.param("greetings", False,
                     id="This word is not an isogram string."),
        pytest.param("great", True,
                     id="This word is an isogram string."),
        pytest.param("Treat", False,
                     id="This word is not an isogram string.")
    ]
)
def test_is_isogram(
        word: str,
        expected_result: bool
) -> None:
    assert (
        is_isogram(word) == expected_result
    )
