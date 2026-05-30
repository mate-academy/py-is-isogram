import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word_arg, result",
    [
        ("", True),
        ("Mamo", False),
        ("A", True),
        ("zz", False),
        ("qwertyuiopasdfghjklzxcvbnm", True),
        ("Asdfgertyapomqwne", False)
    ]
)
def test_arguments_for_isogram(
    word_arg: str,
    result: bool
) -> None:
    assert is_isogram(word_arg) == result
