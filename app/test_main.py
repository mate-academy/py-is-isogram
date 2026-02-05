import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("Adam", False),
        ("look", False),
        ("", True)
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result


def test_is_isogram_with_no_string_value() -> None:
    with pytest.raises(TypeError):
        is_isogram(["string"])
