import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, result",
        [
            pytest.param(
                "",
                True,
                id="Should return True"
            ),
            pytest.param("playgrounds", True),
                        ("look", False),
                        ("Adam", False),
                        ("cakE", True),
        ]
    )
    def test_is_isogram(self, word: str, result: bool):
        assert is_isogram(word) == result, (
            f"Function 'is_isogram' should return {result},"
            f"when 'word' equals to {word}"
        )

    @pytest.mark.parametrize(
        "word",
        [
            pytest.param(
                "playgrounds",
                id="Function must return bool type"
            )
        ]
    )
    def test_type_result(self, word: str):
        assert isinstance(is_isogram(word), bool)

    @pytest.mark.parametrize(
        "word",
        [
            pytest.param(
                "playgrounds",
                id="Argument which take function must be 'str' type"
            )
        ]
    )
    def test_type_argument(self, word: str):
        assert isinstance(word, str)
