from typing import Any

from app.main import is_isogram

import pytest


class TestIsIsogramClass:
    @pytest.mark.parametrize(
        "word, excepted_error",
        [
            pytest.param(1, AttributeError, id="test_is_str"),
            pytest.param(5243, AttributeError, id="test_is_str"),
            pytest.param(False, AttributeError, id="test_is_str"),
            pytest.param(True, AttributeError, id="test_is_str"),
        ]
    )
    def test_is_str(self, word: str, excepted_error: Exception) -> None:
        with pytest.raises(excepted_error):
            assert is_isogram(word)

    @pytest.mark.parametrize(
        "word, second_argument, excepted_error",
        [
            pytest.param(1, "a", TypeError, id="test_takes_one_argument"),
            pytest.param(5243, "B", TypeError, id="test_takes_one_argument"),
            pytest.param(False, "123", TypeError, id="test_takes_one_argument"),
            pytest.param(True, "HellO", TypeError, id="test_takes_one_argument"),
        ]
    )
    def test_takes_one_argument(self, word: str, second_argument: Any, excepted_error: Exception) -> None:
        with pytest.raises(excepted_error):
            assert is_isogram(word, second_argument)

    @pytest.mark.parametrize(
        "word, excepted_result",
        [
            pytest.param("aA", False,
                         id="test_same_latters_with_different_cases"),
            pytest.param("playgGrounds", False,
                         id="test_same_latters_with_different_cases"),
        ]
    )
    def test_same_latters_with_different_cases(self, word: str, excepted_result: bool) -> None:
        assert is_isogram(word) == excepted_result

    @pytest.mark.parametrize(
        "word, excepted_result",
        [
            pytest.param("", True,
                         id="test_empty_string_is_an_isogram"),
        ]
    )
    def test_empty_string_is_an_isogram(self, word: str, excepted_result: bool) -> None:
        assert is_isogram(word) == excepted_result

    @pytest.mark.parametrize(
        "word, excepted_result",
        [
            pytest.param("letter", False,
                         id="test_not_only_consecutive_letters_are_not_an_isogram"),
            pytest.param("alphabet", False,
                         id="test_not_only_consecutive_letters_are_not_an_isogram"),
        ]
    )
    def test_not_only_consecutive_letters_are_not_an_isogram(self, word: str, excepted_result: bool) -> None:
        assert is_isogram(word) == excepted_result
