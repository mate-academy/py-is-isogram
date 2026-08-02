import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word_values, result_bool",
    [
        ("playgrounds", True),
        ("look", False),
        ("SILVANA", False),
        ("1234", True),
        ("1231", False),
        ("War#$%_Code", True),
        pytest.param("Adam", False, id="checking for capital letter"),
        pytest.param("", True, id="checking for an empty string"),
        pytest.param(" ", True, id="checking only one space"),
        pytest.param("Ker igan", True, id="checking word with one space"),
        pytest.param("No va ", False, id="checking word with multiple spaces")
    ]
)
def test_is_isogram_for_string_values(
        word_values: str,
        result_bool: bool
) -> None:
    assert is_isogram(word_values) == result_bool
