import pytest
from app.main import is_isogram


def test_should_return_bool() -> None:
    assert isinstance(is_isogram(""), bool)


@pytest.mark.parametrize(
    "word,result",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False)
    ]
)
def test_checks(word: str, result: bool) -> None:
    assert is_isogram(word) is result
