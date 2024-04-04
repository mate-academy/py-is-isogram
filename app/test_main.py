import pytest

from app.main import is_isogram


# write your code here
class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,correct_result",
        [
            pytest.param("playgrounds", True,
                         id="str 'playgrounds' must return True"),
            pytest.param("look", False,
                         id="str 'look' must return False"),
            pytest.param("Adam", False,
                         id="str 'Adam' must return False"),
            pytest.param("", True,
                         id="str '' must return True"),
        ]
    )
    def test_is_isogram_with_correct_parameters(
            self,
            word: str,
            correct_result: bool
    ) -> None:
        assert is_isogram(word) == correct_result

    @pytest.mark.parametrize(
        "word",
        [
            pytest.param(123,
                         id="not str must raise AttributeError")
        ]
    )
    def test_is_isogram_with_incorrect_parameters(
            self,
            word: str
    ) -> None:
        with pytest.raises(AttributeError):
            assert is_isogram(word)
