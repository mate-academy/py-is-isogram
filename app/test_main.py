import pytest
from app.main import is_isogram

@pytest.mark.parametrize(
    "initial_word,expected_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
<<<<<<< HEAD
        ("", True),
        ("local", False)
=======
        ("", True)
>>>>>>> 1f2e963eab504713395a098e011632759067b5f2
    ]
)
def test_is_isogram(initial_word: str, expected_result: bool) -> None:
    assert (
        is_isogram(initial_word) == expected_result
    )
