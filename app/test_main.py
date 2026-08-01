from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "string,result",
    [
        ("playgrounds", True,),
        ("look", False),
        ("Adam", False),
        pytest.param("", True, id="empty is isogram"),
        pytest.param(None, False,
                     marks=pytest.mark.xfail(reason="None as an input"),
                     id="expected fail",)
    ]
)
def test_correct_n_expected(string: str, result: bool) -> bool:
    assert is_isogram(string) == result
