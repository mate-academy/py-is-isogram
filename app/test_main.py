import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("", True),
        (" ", True),
        ("Can", True),
        ("Add", False),
        ("ADerd", False),
        ("Ad_dit", False),
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert (is_isogram(word) == result)
