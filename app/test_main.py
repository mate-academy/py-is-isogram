import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "word, isogram",
    [
        ('playgrounds', True),
        ('look', False),
        ('Adam', False),
        ('', True),
    ],
)
def tests_is_isogram(word, isogram):
    assert is_isogram(word) is isogram, (
        f"Function should return {isogram}, when word is equal to '{word}'."
    )
