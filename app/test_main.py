import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param("atmospheric", True, id="testing an isogram word"),
        pytest.param("smalL", False, id="testing when word has the same "
                                        "letter in different case"),
        pytest.param("", True, id="testing empty string"),
        pytest.param("lOOk", False, id="testing word with two "
                                       "letters in uppercase"),
        pytest.param("Arab", False, id="testing word with two "
                                       "letters in uppercase")
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
