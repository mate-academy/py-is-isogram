import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("playgrounds", True),
        ("look", False),
        ("English", True),
        ("Adam", False),
        ("", True)
    ],
    ids=[
        "checks if function works for isogram word",
        "checks if function works for not isogram word",
        "function is case-insensitive (isogram)",
        "function is case-insensitive (not isogram)",
        "check empty string"
    ]
)
def test_check_main_cases_and_edging_situations_for_isogram(
        word: str,
        result: bool
) -> None:
    assert is_isogram(word) == result


def test_function_for_wrong_input() -> None:
    with pytest.raises(AttributeError):
        is_isogram(8)
