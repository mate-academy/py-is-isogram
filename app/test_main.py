import pytest

from app.main import is_isogram


class TestMain:
    @pytest.mark.parametrize(
        "test_input, expected",
        [
            pytest.param("", True,
                         id="Should return True for empty string"),
            pytest.param("playgrounds", True,
                         id="Should return True for isogram"),
            pytest.param("look", False,
                         id="Should return False for non-isogram"),
            pytest.param("Adam", False,
                         id="Function should be case-insensitive"),
            pytest.param("some w ", False,
                         id="Should return False for few whitespace")
        ]
    )
    def test_is_isogram(self, test_input: str, expected: bool) -> None:
        assert is_isogram(test_input) == expected
