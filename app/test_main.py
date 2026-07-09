from typing import Any

import pytest

from app.main import is_isogram


class TestIsIsogram:

    @pytest.mark.parametrize(
        "word,expected_error",
        [
            pytest.param(
                2,
                AttributeError,
                id="If word is not string"
            )
        ]
    )
    def test_exception_raising(
            self,
            word: Any,
            expected_error: type[AttributeError]
    ) -> None:
        with pytest.raises(expected_error):
            is_isogram(word)

    @pytest.mark.parametrize(
        "word,expected_val",
        [
            pytest.param(
                "",
                True,
                id="Empty word"
            ),
            pytest.param(
                "playgrounds",
                True,
                id="Lower case word"
            ),
            pytest.param(
                "look",
                False,
                id="Double letter word"
            ),
            pytest.param(
                "PlayGrounds",
                True,
                id="Upper case word"
            ),
            pytest.param(
                "PLAYGROUND",
                True,
                id="All letters with Uppercase"
            ),
            pytest.param(
                "Adam",
                False,
                id="Double letter uppercase word"
            ),
            pytest.param(
                "  playgrounds   ",
                False,
                id="Double letter uppercase word"
            ),
            pytest.param(
                "semi-truck",
                True,
                id="With symbol word"
            ),
            pytest.param(
                "0123456789",
                True,
                id="Line of digits"
            ),
            pytest.param(
                "0112345567890",
                False,
                id="Double of digits in line"
            ),
            pytest.param(
                "цінність",
                False,
                id="Double cyr letters with lowercase"
            ),
            pytest.param(
                "ЦіНнІсть",
                False,
                id="Double cyr letters with Uppercase"
            ),
            pytest.param(
                "AАBВ",
                True,
                id="Mixed cyr and lat"
            ),
            pytest.param(
                "AbCdEFghIJklMNOpQrSTuvWxYZ",
                True,
                id="ABC with random cases"
            ),
            pytest.param(
                (
                    "AbCdEFghIJklMNOpQrSTuvWxYZ"
                    "AbCdEFghIJklMNOpQrSTuvWxYZ"
                    "AbCdEFghIJklMNOpQrSTuvWxYZ"
                    "AbCdEFghIJklMNOpQrSTuvWxYZ"
                    "AbCdEFghIJklMNOpQrSTuvWxYZ"
                    "AbCdEFghIJklMNOpQrSTuvWxYZ"
                    "AbCdEFghIJklMNOpQrSTuvWxYZ"
                    "AbCdEFghIJklMNOpQrSTuvWxYZ"
                ),
                False,
                id="Long string",
            ),
            pytest.param(
                "-AbCdE.FghIJkl,MNOpQ'rSTuvWxYZ-",
                False,
                id="Double symbols"
            ),
            pytest.param(
                "-AbCdE.FghIJkl,MNOpQ'rSTuvWxYZ",
                True,
                id="No Double symbols"
            ),
        ])
    def test_modify_func_correctly(
            self,
            word: Any,
            expected_val: bool
    ) -> None:
        assert is_isogram(word) == expected_val
