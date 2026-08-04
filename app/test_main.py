import pytest

from app.main import is_isogram


class TestIsogramString:
    @pytest.mark.parametrize(
        "word,expected",
        [
            pytest.param(
                "playgrounds",
                True,
                id="should return `True` for playgrounds",
            ),
            pytest.param(
                "",
                True,
                id="should return `True` for empty string",
            ),
            pytest.param(
                "Adam",
                False,
                id="`A` and `a` should be considered as the same words",
            ),
            pytest.param(
                "abcdef",
                True,
                id="should return `True` for `abcdef`",
            ),
            pytest.param(
                "hello",
                False,
                id="should return `False` for `hello`",
            ),
        ],
    )
    def test_is_isogram_string(self, word: str, expected: bool) -> None:
        assert is_isogram(word) == expected
