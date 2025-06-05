from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "input_value, result_value",
    [
        ("", True),
        ("core", True),
        ("land", True),
        ("computer", True),
        ("laptop", False),
        ("analysis", False),
        ("cucumber", False),
        ("helm", True),
        ("annihilation", False)
    ],
    ids=["test_case_1",
         "test_case_2",
         "test_case_3",
         "test_case_4",
         "test_case_5",
         "test_case_6",
         "test_case_7",
         "test_case_8",
         "test_case_9"]
)
def test_check_functionality_of_the_function_above(input_value: str,
                                                   result_value: bool) -> None:
    assert is_isogram(input_value) == result_value
