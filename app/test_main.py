import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Hi World", True)
    ],
    ids=["playgrounds", "look", "Adam", "empty-string", "Hi World"]
)
def test_should_equal_expected_result(
    word: str,
    expected_result: bool
) -> None:
    assert is_isogram(word) == expected_result


@pytest.mark.parametrize(
    "word",
    [50, 56.34, ["hi", "bye"], False, None],
    ids=["int", "float", "list", "bool", "none-type"]
)
def test_should_raise_exception_if_passed_incorrect_data_type(
    word: str
) -> None:
    with pytest.raises(AttributeError):
        is_isogram(word)
