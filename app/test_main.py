from app.main import is_isogram
import pytest


class TestIsIsogram:

    @pytest.mark.parametrize(
        "word,result",
        [
            pytest.param("playgrounds", True,
                         id="Should return True if playgrounds"
                         ),
            pytest.param("look", False,
                         id="Should return False if look"
                         ),
            pytest.param("Adam", False,
                         id="Should return False if Adam"
                         ),
            pytest.param("", True,
                         id="Should return True if empty string"
                         )
        ]
    )
    def test_is_isogram(self, word: str, result: bool) -> None:
        assert is_isogram(word) == result


if __name__ == "__main__":
    pytest.main()
