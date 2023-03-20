import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,result",
        [
            pytest.param(
                "playgrounds", True,
                id="should return 'True' if all letters are different"),
            pytest.param(
                "look", False,
                id="should return 'False' if some letters are equal "
                   "and in different cases(upper or lower)"),
            pytest.param(
                "Adam", False,
                id="should return 'False' if some letters are equal "
                   "and in same cases(upper or lower)"),
            pytest.param(
                "", True,
                id="should return 'True' if 'word' is an empty string")
        ]
    )
    def test_return_valid_result(
            self,
            word: str,
            result: bool
    ) -> None:
        assert is_isogram(word) == result

    @pytest.mark.parametrize(
        "word",
        [
            pytest.param(
                12,
                id="should raise an error when argument isn't a string"),
        ]
    )
    def test_should_raise_error_if_incorrect_type(
            self,
            word: str,
    ) -> None:
        with pytest.raises(AttributeError):
            is_isogram(word)
