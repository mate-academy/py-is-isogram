from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, bool_result", [
            pytest.param("isogram", True,
                         id="should return True"),
            pytest.param("bamboo", False,
                         id="False if there are repeating letters"),
            pytest.param("", True,
                         id="True if word is empty string"),
            pytest.param("Gig", False,
                         id="uppercase and lowercase letters "
                            "are considered the same letter")
        ]
    )
    def test_check_is_isogram_correctly(self,
                                        word: str,
                                        bool_result: bool
                                        ) -> None:
        assert is_isogram(word) == bool_result
