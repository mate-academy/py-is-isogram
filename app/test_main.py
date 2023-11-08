import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
        "word, expected",
    [
        ("playgrounds", True),
        ("CAiSDNipoik", False),
        ("LoOk", False),
        ("OOOOooOoOoooo", False),
        ("", True)
    ]
)
def test_check_is_isogtam_word(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
