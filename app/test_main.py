import pytest


from app.main import is_isogram


# write your tests here
@pytest.mark.parametrize(
    "isogram,result",
    [
        pytest.param("playgrounds", True, id="should return this is isogram"),
        pytest.param("", True, id="should empty string is isogram"),
        pytest.param("look", False, id="should return this isn't isogram"),
        pytest.param("Adam", False, id="should check is this isogram "
                                       "after converting to lower"),

    ]
)
def test_get_coin_combination(isogram: str, result: bool) -> None:
    assert (is_isogram(isogram) == result)
