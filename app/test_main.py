import pytest

from app.main import is_isogram


def test_if_empty_is_isogram() -> None:
    assert is_isogram("") is True


def test_dif_case_repeating_letters_is_isogram() -> None:
    assert is_isogram("Aa") is False


@pytest.mark.parametrize(
    "example,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False)
    ], ids=["all dif low case",
            "duplicate low case",
            "duplicate dif case"]
)
def test_dif_examples(example: str, result: bool) -> None:
    assert is_isogram(example) == result
