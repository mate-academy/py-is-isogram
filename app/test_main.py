import pytest


from app.main import is_isogram


def test_returns_bool() -> None:
    assert (
        type(is_isogram("InputTest")) == bool
    ), "Function should return bool"


def test_empty_string() -> None:
    assert (
        is_isogram("") is True
    ), "Empty string is considered an isogram"


def test_function_is_case_insensitive() -> None:
    assert (
        is_isogram("Aa") is False
    ), "Function should be case insensitive"


@pytest.mark.parametrize(
    "input_string, result",
    [
        pytest.param(
            "Adam",
            False,
            id="Word with two letters of different case"
        ),
        pytest.param(
            "playgrounds",
            True,
            id="Long word isogram"
        )
    ]
)
def test_is_isogram_input_result(
        input_string: str,
        result: bool
) -> None:
    assert (
        is_isogram(input_string) == result
    ), f"{input_string} should result in {result}"
