from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,expect",
    [
        (
            'playgrounds',
            True
        ),
        (
            'look',
            False
        ),
        (
            'Adam',
            False
        ),
        (
            '',
            True
        )
    ]
)
def test_function_correct_work(word, expect):
    assert is_isogram(word) == expect
