import pytest

import app.main as main


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("a", True),
        ("A", True),
        ("aA", False),
        (" ", True),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert main.is_isogram(word) == expected


def test_is_isogram_raises_type_error_with_int() -> None:
    with pytest.raises(TypeError):
        main.is_isogram(123)
