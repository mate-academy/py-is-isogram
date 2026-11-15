import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            pytest.param(
                "playgrounds",
                True,
                id="test should be isogram"
            ),
            pytest.param(
                "look",
                False,
                id="test lower word should not be isogram"
            ),
            pytest.param(
                "Adam",
                False,
                id="test one letter upper and one letter lower"
            ),
            pytest.param(
                "",
                True,
                id="test empty input should be isogram"
            ),
            pytest.param(
                "a",
                True,
                id="test one letter should be isogram"
            ),
            pytest.param(
                "Python",
                True,
                id="test word start with big letter should be isogram"
            ),
            pytest.param(
                "AAA",
                False,
                id="test three upper letters should not be isogram"
            ),
            pytest.param(
                "letter",
                False,
                id="test non-consecutive repeated letters"
            ),
        ]
    )
    def test_is_isogram(
        self,
        word: str,
        expected_result: bool
    ) -> None:
        assert is_isogram(word) == expected_result
