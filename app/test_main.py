import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def tests_checks_all_edged_situations(
        word: str,
        result: bool
) -> None:
    assert is_isogram(word) == result


def test_incorrect_type_of_data() -> None:
    with pytest.raises(AttributeError):
        is_isogram(5)
