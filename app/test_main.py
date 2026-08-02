import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "input_string,expected_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_function_returns_expected_result(input_string: str,
                                          expected_result: bool) -> None:

    result = is_isogram(input_string)

    assert result == expected_result
