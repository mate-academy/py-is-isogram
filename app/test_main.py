from app.main import is_isogram

import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "one_word,expected_bool",
        [
            pytest.param(
                "",
                True,
                id="should return True if empty string given"
            ),
            pytest.param(
                " ",
                True,
                id="should return True if space given"
            ),
            pytest.param(
                "Bob",
                False,
                id="should return False if used both registers of letter"
            ),
            pytest.param(
                "subway",
                True,
                id="should return True if isogram given"
            ),
            pytest.param(
                "BLACK",
                True,
                id="should return True if used upper case"
            ),
            pytest.param(
                "abcdefghijklmnopqrstuvwxyz",
                True,
                id="should return True if alphabet given"
            ),
            pytest.param(
                ".,:;!?",
                True,
                id="should return True if symbols given"
            ),
            pytest.param(
                "1234",
                True,
                id="should return True if number given"
            )
        ]
    )
    def test_is_isogram(
            self,
            one_word: str,
            expected_bool: bool
    ) -> None:
        assert is_isogram(one_word) == expected_bool

    @pytest.mark.parametrize(
        "one_word,expected_error",
        [
            pytest.param(
                ["string"],
                AttributeError,
                id="should raise error if list type given"
            ),
            pytest.param(
                True,
                AttributeError,
                id="should raise error if bool type given"
            ),
            pytest.param(
                {"white": "orange"},
                AttributeError,
                id="should raise error if dict type given"
            )
        ]
    )
    def test_is_isogram_error(
            self,
            one_word: list[str] | bool | dict,
            expected_error: type[Exception]
    ) -> None:
        with pytest.raises(expected_error):
            is_isogram(one_word)
