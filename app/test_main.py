import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "given_str,expected_result",
    [
        pytest.param(
            "qwrtyytrewq",
            False,
            id="test should return False if `word` have a few same letters"
        ),
        pytest.param(
            "qwrtyy",
            False,
            id="test should return False if `word` have one same letter"
        ),
        pytest.param(
            "qwrty",
            True,
            id="test should return True if `word` have no duplicated letters"
        ),
    ]
)
def test_check_str_with_lower_characters(
        given_str: str,
        expected_result: bool
) -> None:
    assert is_isogram(given_str) == expected_result


@pytest.mark.parametrize(
    "given_str,expected_result",
    [
        pytest.param(
            "qwrtYytrewQ",
            False,
            id="test should return False if `word` have a few same letters"
               "with the same case"
        ),
        pytest.param(
            "qwrtYy",
            False,
            id="test should return False if `word` have one same letter"
               "with the same case"
        ),
        pytest.param(
            "qWrTy",
            True,
            id="test should return True if `word` have no duplicated letters"
               "and letters have a different case"
        ),
    ]
)
def test_check_str_with_different_case_characters(
        given_str: str,
        expected_result: bool
) -> None:
    assert is_isogram(given_str) == expected_result


@pytest.mark.parametrize(
    "given_str,expected_result",
    [
        pytest.param(
            "qwrty!11",
            False,
            id="test should return False if `word` "
               "have a few same numeric characters"
        ),
        pytest.param(
            "qwrt$y$",
            False,
            id="test should return False if `word` have one same letter"
        ),
        pytest.param(
            "qWrTy1$_+",
            True,
            id="test should return True if `word`"
               "have no duplicated numbers or special characters"
        ),
        pytest.param(
            "",
            True,
            id="test should return True if `word`"
               "have no characters at all"
        ),
        pytest.param(
            " ",
            True,
            id="test should return True if `word`"
               "have no characters but have a whitespace"
        ),
        pytest.param(
            "  ",
            False,
            id="test should return False if `word`"
               "have no characters but have a few whitespaces"
        ),
    ]
)
def test_check_str_with_different_special_characters_or_numbers(
        given_str: str,
        expected_result: bool
) -> None:
    assert is_isogram(given_str) == expected_result


@pytest.mark.parametrize(
    "given_data",
    [
        (set()),
        (tuple()),
        (list()),
        (dict()),
        (111)
    ]
)
def test_func_should_raise_correct_errors(
        given_data: set | tuple | list | dict | int
) -> None:
    with pytest.raises(AttributeError):
        is_isogram(given_data)
