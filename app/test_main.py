import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            pytest.param(
                "",
                True,
                id="should return True "
                   "if word is empty"
            ),
            pytest.param(
                "playgrounds",
                True,
                id="should return True "
                   "if string is isogram"
            ),
            pytest.param(
                "House",
                True,
                id="should return True "
                   "if string is isogram has large letter"
            ),
            pytest.param(
                "FAMILY",
                True,
                id="should return True "
                   "if string is isogram has only large letters"
            ),
            pytest.param(
                "look",
                False,
                id="should return False "
                   "if string is not isogram"
            ),
            pytest.param(
                "Adam",
                False,
                id="should return False "
                   "if string is not isogram has large letter"
            ),
            pytest.param(
                "BABY",
                False,
                id="should return False "
                   "if string is not isogram has only large letters"
            ),
        ]
    )
    def test_is_isogram(
            self,
            word: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(word) == expected_result

    @pytest.mark.parametrize(
        "word, expected_error",
        [
            pytest.param(
                18,
                AttributeError,
                id="should raise error for integer value"
            ),
            pytest.param(
                None,
                AttributeError,
                id="should raise error for None types"
            ),
        ]
    )
    def test_is_isogram_exceptions(
            self,
            word: int | None,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            is_isogram(word)
