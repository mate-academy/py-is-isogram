import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "input_word,expected",
    [
        ("", True),
        ("a", True),
        ("bb", False),
        ("word", True),
        ("letter", False),
        ("laptop", False)
    ]
)
def test_function_must_return_correct_boolean(
        input_word: str,
        expected: bool
) -> None:
    assert is_isogram(input_word) == expected


@pytest.mark.parametrize(
    "input_word,expected_error",
    [
        (["a"], AttributeError),
        (1, AttributeError),
        ({"word"}, AttributeError),
        (("letter",), AttributeError),
        ({"laptop": True}, AttributeError),
    ]
)
def test_function_must_raise_error_if_input_type_is_not_correct(
        input_word: str,
        expected_error: type[Exception]
) -> None:
    with pytest.raises(expected_error):
        is_isogram(input_word)
