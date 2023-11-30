import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "string_to_check, result",
    [
        ("", True),
        ("aa", False),
        ("Bb", False),
        ("abc", True),
        ("AbcdA", False)
    ]
)
def test_can_find_isogram(
        string_to_check: str,
        result: bool) -> None:
    assert (
            is_isogram(string_to_check) == result
    ), f"Function {is_isogram} should " \
       f"return {result} for {string_to_check}"
