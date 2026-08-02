import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param("playgrounds", True, id="No repeating letters here"),
        pytest.param("look", False, id="There's double letter here"),
        pytest.param("Adam", False, id="There's double letters here"),
        pytest.param("", True, id="The empty string is an isogram"),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
