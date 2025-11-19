import pytest

from app.main import is_isogram


def test_should_return_bool() -> None:
    assert (
        isinstance(is_isogram("look"), bool) is True
    ), "Function 'is_isogram' should return bool"


@pytest.mark.parametrize(
    "word, bool_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("isIsoGram", False),
        ("", True)
    ]
)
def test_coin_combination(word: str, bool_result: bool) -> None:
    assert is_isogram(word) == bool_result, (
        f"Function 'is_isogram' should return {bool_result} "
        f"when value is {word}"
    )
