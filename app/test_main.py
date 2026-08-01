import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word",
        [
            "",
            "asa",
            "rock",
        ]
    )
    def test_is_isogram_should_return_boolean_type(
        self,
        word: str
    ) -> None:
        assert type(is_isogram(word)) == bool

    @pytest.mark.parametrize(
        "word",
        [
            ""
        ]
    )
    def test_is_isogram_should_return_true_if_empty_word(
        self,
        word: str
    ) -> None:
        assert is_isogram(word)

    @pytest.mark.parametrize(
        "word",
        [
            "look",
            "Adam",
        ]
    )
    def test_is_isogram_should_return_false(
        self,
        word: str
    ) -> None:
        assert not is_isogram(word)

    @pytest.mark.parametrize(
        "word",
        [
            "playgrounds",
            "rock",
        ]
    )
    def test_is_isogram_should_return_true(
            self,
            word: str
    ) -> None:
        assert is_isogram(word)
