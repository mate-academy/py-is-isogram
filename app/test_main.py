import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, returned", [("playgrounds", True),
                                            ("look", False),
                                            ("Adam", False),
                                            ("", True)])
def test_some_function(word: str, returned: bool) -> None:
    assert is_isogram(word) == returned
