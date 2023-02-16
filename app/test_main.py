import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result_bool",
    [
        ('playgrounds', True),
        ('look', False),
        ('Adam', False),
        ("", True),
    ]
)
def test_correct_work(word: str, result_bool: bool) -> None:
    assert is_isogram(word) == result_bool


def test_doesnt_work_with_another_type():
    with pytest.raises(AttributeError):
        is_isogram(12)