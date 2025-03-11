import pytest

from app.main import is_isogram


class TestIsIsogram:

    @pytest.mark.parametrize(
        "word, expected",
        [
            ("look", False),
            ("playgrounds", True),
            ("", True),
            ("kobold", False),
            ("kobOld", False)
        ],
        ids=[
            "not isogram",
            "isogram",
            "empty string",
            "non consecutive repeat",
            "repeat with diferent cases"
        ]
    )
    def test_is_isogram(self, word: str, expected: bool) -> None:
        assert is_isogram(word) == expected
