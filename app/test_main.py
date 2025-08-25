from app.main import is_isogram
import pytest


def test_func_return_bool_value() -> None:
    word = "Tom"
    result = is_isogram(word=word)
    assert isinstance(result, bool)


@pytest.mark.parametrize(
    "word,result",
    [
        ("Tom", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("playgrounds", True)
    ]
)
def test_correct_work_of_func(word: str, result: bool) -> None:
    assert is_isogram(word=word) == result
