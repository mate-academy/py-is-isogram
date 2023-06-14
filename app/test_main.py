import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "income_string, exp_result",
    [
        pytest.param("", True, id="empty string should return True"),
        pytest.param("Adam", False, id="letter case and isogram"),
        pytest.param("look", False, id="in case when str isn't isogram")
    ]
)
def test_is_isogram(income_string: str, exp_result: bool) -> None:
    assert is_isogram(income_string) == exp_result
