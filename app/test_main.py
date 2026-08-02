import pytest

from app.main import is_isogram


@pytest.mark.parametrize("string, expected_return",
                         [
                             ("playgrounds", True),
                             ("PlayGround", True),
                             ("look", False),
                             ("Adam", False),
                             ("adam", False),
                             ("", True)
                         ])
def test_isogram(string: str, expected_return: bool) -> None:
    assert (is_isogram(string) == expected_return)
