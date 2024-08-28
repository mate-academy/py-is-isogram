import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("python", True),
        ("smart", True),
        ("background", True),
        ("look", False),
        ("froNtend", False),
        ("backend", True),
        ("Paprica", False)
    ]
)
def test_with_different_attributes(word, expected): # noqa
    assert is_isogram(word) == expected


@pytest.mark.parametrize(
    "word,expected",
    [
        (123, AttributeError),
        ([1], AttributeError)
    ]
)
def test_with_incorrect_value_type(word, expected): # noqa
    with pytest.raises(expected):
        is_isogram(word)
