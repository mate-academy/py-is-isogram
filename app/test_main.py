import pytest
from app.main import is_isogram


class TestIsIsogram:

    @pytest.mark.parametrize(
        'words_taken, result_of_function',
        [
            pytest.param("playgrounds", True,
                         id="should return True when word is isogram"),
            pytest.param("look", False,
                         id="should return False if letter are repeated "),
            pytest.param("Adam", False,
                         id="function should be case-insensitive"),
            pytest.param("", True,
                         id="empty string is isogram"),
            pytest.param("AdAm", False,
                         id="uppercase letter repeated")
        ]
    )
    def test_isogram_function_work(self,
                                   words_taken,
                                   result_of_function):
        assert is_isogram(words_taken) == result_of_function
