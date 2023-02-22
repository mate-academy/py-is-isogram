import pytest
from app.main import is_isogram

@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Mi po", True),
        ("Mam", False)
    ],
    ids=[
        "-> 'playgrounds' <- must return -> True <-",
        "-> 'look' <- must return -> False <-",
        "-> 'Adam' <- must return -> False <-",
        "-> '' <- must return -> True <-",
        "-> 'Mi po' <- must return -> True <-",
        "-> 'Mam' <- must return -> False <-"
    ]
)
def test_is_isogram(word: int, expected_result: list) -> None:
    assert is_isogram(word) == expected_result


def test_is_isogram_for_non_str_values() -> None:
    with pytest.raises(TypeError):
        is_isogram(is_isogram(1, [1], {"1": 1}, True, False))
