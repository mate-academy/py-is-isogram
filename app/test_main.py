import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "string, bool_value",
    [
        pytest.param("", True,
                     id="Word is empty string"),
        pytest.param("PlaYgRouNDs", True,
                     id="Isogram with different cases"),
        pytest.param("UNCOPYRIGHTABLE ", True,
                     id="Isogram with only uppercase"),
        pytest.param("Adam", False,
                     id="Word with repeated letters"),
        pytest.param("f", True,
                     id="Word with only 1 letter"),
        pytest.param("Aa", False,
                     id="Uppercase and lowercase near"),
    ]
)
def test_word_is_isogram(string: str, bool_value: bool) -> None:
    assert is_isogram(string) is bool_value
