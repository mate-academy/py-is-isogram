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
def test_should_return_right_values(word: str, result: list) -> None:
    assert (
        is_isogram(word) == result
    )
