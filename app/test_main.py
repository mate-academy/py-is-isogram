import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
   "string,result",
   [
       ("playgrounds", True),
       ("look", False),
       ("Adam", False),
       ("", True)
   ]
)
def test_isogram(string: str, result: bool) -> bool:
    assert is_isogram(string) == result
