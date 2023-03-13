import pytest

from app.main import is_isogram


@pytest.mark.parametrize("income_world, expected_result",
                         [
                             ("playgrounds", True),
                             ("look", False),
                             ("Adam", False),
                             ("", True)
                         ])
def test_isogram(income_world: str,
                 expected_result: bool) -> None:
    assert is_isogram(income_world) == expected_result
