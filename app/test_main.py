from app.main import is_isogram


def test_is_isogram_wen_isempty() -> None:
    assert is_isogram("") is True


def test_string_with_different_cases_of_the_same_letter() -> None:
    assert is_isogram("Adam") is False


def test_not_only_non_consecutive_letters_are_not_an_isogram() -> None:
    assert is_isogram("look") is False

#
# from app.main import is_isogram
#
# import pytest
#
#
# def test_value_should_be_letters() -> None:
#     assert (isinstance(is_isogram(""), bool))

#
#
# @pytest.mark.parametrize(
#     "word, expected",
#     [
#         ("playgrounds", True),
#         ("look", False),
#         ("Adam", False),
#         ("", True)
#     ]
# )
# def test_check_is_isogram(word: str, expected: bool) -> None:
#     assert is_isogram(word) == expected