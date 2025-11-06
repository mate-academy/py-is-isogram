from app.main import is_isogram
import pytest


class TestIsIsogram:

    @pytest.mark.parametrize(
        "word,expected",
        [
            pytest.param("playgrounds", True,
                         id="should return True if all letters are unique"),
            pytest.param("look", False,
                         id="should return False if same letters "
                            "from word are duplicated"),
            pytest.param("False", True, id="should be case-insensitive"),
            pytest.param("", True, id="should retturn True if word is empty"),
        ]
    )
    def test_is_isogram(self, word: str, expected: bool) -> None:
        assert is_isogram(word) == expected


def test_error_occured() -> None:
    with pytest.raises(AttributeError):
        is_isogram(None)
        is_isogram(1)
