import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_result",
    [
        ("", True),
        ("a", True),
        ("C", True),
        ("playgrounds", True),
        ("sUbdermatoGlyphic", True),
        ("look", False),
        ("Adam", False),
        ("cheRRy", False)
    ]
)
def test_should_return_correct_bool(
        word: str,
        expected_result: bool
) -> None:
    assert is_isogram(word) is expected_result
