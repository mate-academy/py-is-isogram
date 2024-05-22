import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "input_data,expected",
    [
        pytest.param("foO", False, id="test case-sensitivity"),
        pytest.param("baR", True, id="test case-sensitivity"),
        pytest.param("", True, id="test empty string"),
        pytest.param("51", True, id="test digits"),
        pytest.param("55", False, id="test digits"),
        pytest.param(" 123 fDq", False, id="test with combined symbols"),
        pytest.param("   ", False, id="test with whitespaces")
    ]
)
def test_string_passed(input_data: str, expected: bool) -> None:
    assert is_isogram(input_data) == expected


@pytest.mark.parametrize(
    "input_data,expected",
    [
        (33, AttributeError),
        (None, AttributeError),
        (True, AttributeError),
        (["some", "list"], AttributeError)
    ]

)
def test_another_data_types_passed(
        input_data: list | bool | type(None),
        expected: type(Exception)
) -> None:
    with pytest.raises(expected):
        is_isogram(input_data)
