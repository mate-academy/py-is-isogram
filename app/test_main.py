import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "param_in, expected_result",
    [
        ("", True),
        ("a", True),
        ("Aa", False),
        ("abra", False),
        ("abrA", False),
        ("abcdefj", True),
    ]
)
def test_correct_values(param_in: str, expected_result: bool) -> None:
    assert is_isogram(param_in) == expected_result
