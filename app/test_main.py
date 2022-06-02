import pytest

from app.main import is_isogram


@pytest.mark.parametrize("word,result",
                         [pytest.param("playgrounds", True,
                                       id="test only unics letters"),
                          pytest.param("book", False,
                                       id="test repeating letters"),
                          pytest.param("Madam", False,
                                       id="test case-insensitive "
                                          "repeating letters"),
                          pytest.param("", True, id="test empty string")])
def test_is_isogram(word: str, result: bool):
    assert is_isogram(word) == result
