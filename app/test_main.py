import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ]
)
def test_return_best_result(word: str,
                            result: bool
                            ) -> None:
    assert is_isogram(word) == result
