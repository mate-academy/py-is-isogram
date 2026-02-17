import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True),
])
def test_is_isogram(word: str, expected: list) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize("bad_word, expected_exception", [
    (1, AttributeError),      # Рядок неможливо перетворити на str
    (None, AttributeError),       # None викликає AttributeError при None
    ([], AttributeError),         # Список викликає AttributeError
    (object(), AttributeError),   # Об'єкт викликає AttributeError
])
def test_should_raise_error_on_invalid_types(bad_word: int,
                                             expected_exception: list) -> None:
    with pytest.raises(expected_exception):
        is_isogram(bad_word)
