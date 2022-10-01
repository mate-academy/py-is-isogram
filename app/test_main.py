import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_rezult",
    [
        pytest.param("", True, id="An empty line is an isogram"),
        ("Adam", False),
        ("look", False),
        ("playgrounds", True)
    ]
)
def test_return_true_for_isogram(word, expected_rezult):
    assert is_isogram(word) == expected_rezult
